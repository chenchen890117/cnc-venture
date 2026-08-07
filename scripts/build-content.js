#!/usr/bin/env node
/**
 * CnC Venture — static content build.
 *
 * Reads /content and writes finished HTML pages. Nothing to install, no
 * framework, no dependencies: Node's standard library only, so Netlify runs
 * `npm run build` and gets a plain static site out the other side.
 *
 *   /content/<category>/<slug>/meta.json   shared facts (dates, hero, related)
 *   /content/<category>/<slug>/en.md       English text
 *   /content/<category>/<slug>/zh-tw.md    Chinese text
 *   /content/<category>/<slug>/images/     photographs for that piece
 *
 * A piece may ship in one language only. When a translation is missing the
 * page for that language is simply not written, and — this is the part that
 * matters for SEO — the published language does not advertise an alternate
 * that does not exist.
 *
 * Run:  npm run build
 */
'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..');
const CONTENT = path.join(ROOT, 'content');
const IMG = path.join(ROOT, 'img');

const CFG = JSON.parse(fs.readFileSync(path.join(CONTENT, '_config.json'), 'utf8'));
const DOMAIN = CFG.domain.replace(/\/$/, '');
const CTA = CFG.cta;
const LANGS = CFG.languages;              // ['en', 'zh-tw']
const UI = CFG.ui;
const CATS = CFG.categories;
const CAT_BY_SLUG = Object.fromEntries(CATS.map((c) => [c.slug, c]));

const LANG_META = {
  'en':    { code: 'en',         slug: 'en',    oglocale: 'en_US', ogalt: 'zh_TW', hreflang: 'en' },
  'zh-tw': { code: 'zh-Hant-TW', slug: 'zh-tw', oglocale: 'zh_TW', ogalt: 'en_US', hreflang: 'zh-Hant-TW' },
};

const FONTS_EN =
  'https://fonts.googleapis.com/css2?' +
  'family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..600' +
  '&family=Inter:wght@300;400;500;600&display=swap';
const FONTS_ZH =
  FONTS_EN.replace('&display=swap', '') +
  '&family=Noto+Sans+TC:wght@400;500;700;800;900&display=swap';

const FAVICON =
  "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E" +
  "%3Crect width='64' height='64' rx='12' fill='%2302383D'/%3E%3Ctext x='32' y='43' " +
  "font-family='Georgia,serif' font-size='30' fill='%23FBF8F3' text-anchor='middle'%3EC" +
  '%3C/text%3E%3C/svg%3E';

/* ─────────────────────────────────────────────────────────────────────────
   Small helpers
   ───────────────────────────────────────────────────────────────────────── */

const esc = (s) =>
  String(s == null ? '' : s)
    .replace(/&(?![a-zA-Z#0-9]+;)/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

const attr = (s) => esc(s).replace(/"/g, '&quot;');

function walkDirs(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true })
    .filter((e) => e.isDirectory())
    .map((e) => e.name)
    .sort();
}

function write(file, body) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, body);
  return Buffer.byteLength(body);
}

/* Content-hash cache busting. /img is served with a long max-age, so a photo
   swapped under an existing filename would otherwise stay stale in browsers
   that already have it. The hash changes, the URL changes, the browser
   refetches — and unchanged files keep their cached copy. */
const VMAP = new Map();
function hashOf(rel) {
  if (VMAP.has(rel)) return VMAP.get(rel);
  const file = path.join(IMG, rel);
  let v = '';
  if (fs.existsSync(file)) {
    v = crypto.createHash('md5').update(fs.readFileSync(file)).digest('hex').slice(0, 8);
  }
  VMAP.set(rel, v);
  return v;
}
function imgUrl(rel) {
  const v = hashOf(rel);
  return `/img/${rel}${v ? `?v=${v}` : ''}`;
}

/* ─────────────────────────────────────────────────────────────────────────
   Markdown
   A deliberately small dialect. Everything an author needs, nothing that
   can produce a page we have not designed.
   ───────────────────────────────────────────────────────────────────────── */

function inlineMd(raw) {
  let t = esc(raw);
  t = t.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (m, txt, href) => {
    const ext = /^https?:/i.test(href);
    const rel = ext ? ' target="_blank" rel="noopener noreferrer"' : '';
    return `<a href="${attr(href)}"${rel}>${txt}</a>`;
  });
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  t = t.replace(/(^|[^*])\*([^*\n]+)\*/g, '$1<em>$2</em>');
  return t;
}

/** Split `---` front matter from the body. */
function parseFrontMatter(src) {
  const text = src.replace(/^﻿/, '').replace(/\r\n?/g, '\n');
  const m = text.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!m) return { data: {}, body: text.trim() };
  const data = {};
  let key = null;
  for (const line of m[1].split('\n')) {
    if (!line.trim()) continue;
    if (/^\s/.test(line) && key) {                 // indented continuation
      (data[key] = Array.isArray(data[key]) ? data[key] : []).push(line.trim());
      continue;
    }
    const kv = line.match(/^([A-Za-z][\w-]*)\s*:\s*(.*)$/);
    if (!kv) continue;
    key = kv[1];
    data[key] = kv[2].trim();                      // '' when a list follows
  }
  return { data, body: text.slice(m[0].length).trim() };
}

/** Body text -> an array of typed blocks. */
function parseBlocks(body) {
  const lines = body.split('\n');
  const blocks = [];
  let i = 0;

  const readDirective = (name, head) => {
    const fields = {};
    const items = [];
    const text = [];
    i++;
    while (i < lines.length && lines[i].trim() !== ':::') {
      const line = lines[i];
      const li = line.match(/^[-*]\s+(.*)$/);
      const kv = line.match(/^([A-Za-z][\w-]*)\s*:\s*(.*)$/);
      if (li) items.push(li[1].trim());
      else if (kv) fields[kv[1].toLowerCase()] = kv[2].trim();
      else if (line.trim()) text.push(line.trim());
      i++;
    }
    i++;                                            // consume the closing :::
    return { name, head, fields, items, text: text.join(' ') };
  };

  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }

    const dir = line.match(/^:::([a-z]+)\s*(.*)$/);
    if (dir) {
      const d = readDirective(dir[1], dir[2].trim());
      if (d.name === 'callout') {
        blocks.push({ t: 'callout', label: d.fields.label || '', title: d.fields.title || '',
                      items: d.items, note: d.fields.note || '', text: d.text });
      } else if (d.name === 'advisory') {
        blocks.push({ t: 'advisory', text: d.text || d.fields.text || '' });
      } else if (d.name === 'note') {
        blocks.push({ t: 'sidenote', text: d.text || '' });
      } else if (d.name === 'image') {
        const parts = d.head.split(/\s+/).filter(Boolean);
        blocks.push({
          t: 'image',
          files: (d.fields.file || parts[0] || '').split('|').map((s) => s.trim()).filter(Boolean),
          size: (d.fields.size || parts[1] || 'standard').toLowerCase(),
          alt: d.fields.alt || '',
          alt2: d.fields.alt2 || '',
          caption: d.fields.caption || '',
          credit: d.fields.credit || '',
        });
      } else {
        throw new Error(`unknown directive :::${d.name}`);
      }
      continue;
    }

    const h = line.match(/^(#{2,4})\s+(.*)$/);
    if (h) { blocks.push({ t: `h${h[1].length}`, text: h[2].trim() }); i++; continue; }

    if (/^>\s?/.test(line)) {
      const quote = [];
      let who = '';
      while (i < lines.length && /^>\s?/.test(lines[i])) {
        const t = lines[i].replace(/^>\s?/, '').trim();
        const a = t.match(/^(?:—|--|–)\s*(.+)$/);
        if (a) who = a[1].trim(); else if (t) quote.push(t);
        i++;
      }
      blocks.push({ t: 'quote', text: quote.join(' '), who });
      continue;
    }

    if (/^[-*]\s+/.test(line) || /^\d+\.\s+/.test(line)) {
      const ordered = /^\d+\.\s+/.test(line);
      const items = [];
      while (i < lines.length &&
             (ordered ? /^\d+\.\s+/ : /^[-*]\s+/).test(lines[i])) {
        items.push(lines[i].replace(ordered ? /^\d+\.\s+/ : /^[-*]\s+/, '').trim());
        i++;
      }
      blocks.push({ t: ordered ? 'ol' : 'ul', items });
      continue;
    }

    if (/^(---|___|\*\*\*)\s*$/.test(line)) { blocks.push({ t: 'hr' }); i++; continue; }

    const para = [];
    while (i < lines.length && lines[i].trim() &&
           !/^(:::|#{2,4}\s|>|[-*]\s|\d+\.\s|---\s*$)/.test(lines[i])) {
      para.push(lines[i].trim());
      i++;
    }
    blocks.push({ t: 'p', text: para.join(' ') });
  }
  return blocks;
}

/* ─────────────────────────────────────────────────────────────────────────
   Block rendering
   ───────────────────────────────────────────────────────────────────────── */

const SIZES = new Set(['standard', 'wide', 'feature', 'portrait', 'duo', 'full']);

function figure(b, resolve) {
  const size = SIZES.has(b.size) ? b.size : 'standard';
  const cap = [];
  if (b.caption) cap.push(inlineMd(b.caption));
  if (b.credit) cap.push(`<span class="credit">${inlineMd(b.credit)}</span>`);
  const caption = cap.length ? `<figcaption>${cap.join('')}</figcaption>` : '';

  if (size === 'duo') {
    const [a, c] = b.files;
    const imgs = [[a, b.alt], [c, b.alt2 || b.alt]]
      .filter(([f]) => f)
      .map(([f, alt]) =>
        `<img src="${attr(imgUrl(resolve(f)))}" alt="${attr(alt)}" loading="lazy" decoding="async">`)
      .join('');
    return `<figure class="docfig img-duo"><div class="pair">${imgs}</div>${caption}</figure>`;
  }
  const f = b.files[0];
  if (!f) return '';
  return `<figure class="docfig img-${size}">` +
    `<img src="${attr(imgUrl(resolve(f)))}" alt="${attr(b.alt)}" loading="lazy" decoding="async">` +
    `${caption}</figure>`;
}

function renderBlocks(blocks, resolve) {
  const out = [];
  for (const b of blocks) {
    switch (b.t) {
      case 'h2': out.push(`<h2>${inlineMd(b.text)}</h2>`); break;
      case 'h3': out.push(`<h3>${inlineMd(b.text)}</h3>`); break;
      case 'h4': out.push(`<h4>${inlineMd(b.text)}</h4>`); break;
      case 'p':  out.push(`<p>${inlineMd(b.text)}</p>`); break;
      case 'hr': out.push('<hr>'); break;
      case 'ul': out.push(`<ul>${b.items.map((i) => `<li>${inlineMd(i)}</li>`).join('')}</ul>`); break;
      case 'ol': out.push(`<ol>${b.items.map((i) => `<li>${inlineMd(i)}</li>`).join('')}</ol>`); break;
      case 'quote': {
        const who = b.who ? `<div class="who">${inlineMd(b.who)}</div>` : '';
        out.push(`<blockquote class="pull-quote"><p class="serif">${inlineMd(b.text)}</p>${who}</blockquote>`);
        break;
      }
      case 'callout': {
        const head = [];
        if (b.label) head.push(`<div class="lbl">${inlineMd(b.label)}</div>`);
        if (b.title) head.push(`<h3 class="serif">${inlineMd(b.title)}</h3>`);
        const body = [];
        if (b.items.length) body.push(`<ul>${b.items.map((i) => `<li>${inlineMd(i)}</li>`).join('')}</ul>`);
        if (b.text) body.push(`<p>${inlineMd(b.text)}</p>`);
        if (b.note) body.push(`<div class="cnote">${inlineMd(b.note)}</div>`);
        out.push(`<aside class="callout"><div>${head.join('')}</div><div>${body.join('')}</div></aside>`);
        break;
      }
      case 'advisory': out.push(`<aside class="advisory">${inlineMd(b.text)}</aside>`); break;
      case 'sidenote': out.push(`<aside class="sidenote">${inlineMd(b.text)}</aside>`); break;
      case 'image': out.push(figure(b, resolve)); break;
      default: throw new Error(`unrenderable block ${b.t}`);
    }
  }
  return out.join('\n        ');
}

/* ─────────────────────────────────────────────────────────────────────────
   Load /content
   ───────────────────────────────────────────────────────────────────────── */

function loadPieces() {
  const pieces = [];
  for (const cat of walkDirs(CONTENT)) {
    if (cat.startsWith('_') || cat.startsWith('.')) continue;
    if (!CAT_BY_SLUG[cat]) {
      console.warn(`  ! skipped /content/${cat}/ — not a category in _config.json`);
      continue;
    }
    for (const slug of walkDirs(path.join(CONTENT, cat))) {
      const dir = path.join(CONTENT, cat, slug);
      const metaFile = path.join(dir, 'meta.json');
      if (!fs.existsSync(metaFile)) {
        console.warn(`  ! skipped /content/${cat}/${slug}/ — no meta.json`);
        continue;
      }
      const meta = JSON.parse(fs.readFileSync(metaFile, 'utf8'));
      meta.category = meta.category || cat;
      meta.type = meta.type === 'project' ? 'project' : 'article';
      if (meta.draft === true) { console.log(`  – draft, not published: ${slug}`); continue; }

      // Photographs that live with the piece are copied into the shared image
      // folder under the slug, so an author only ever drops files in one place.
      const localImages = new Set();
      const imgDir = path.join(dir, 'images');
      if (fs.existsSync(imgDir)) {
        for (const f of fs.readdirSync(imgDir)) {
          if (f.startsWith('.')) continue;
          const dest = path.join(IMG, 'content', slug, f);
          fs.mkdirSync(path.dirname(dest), { recursive: true });
          fs.copyFileSync(path.join(imgDir, f), dest);
          localImages.add(f);
        }
      }
      const resolve = (f) =>
        localImages.has(f) ? `content/${slug}/${f}` : f;

      const langs = {};
      for (const lang of LANGS) {
        const file = path.join(dir, `${lang}.md`);
        if (!fs.existsSync(file)) continue;
        const { data, body } = parseFrontMatter(fs.readFileSync(file, 'utf8'));
        if (!data.title) {
          console.warn(`  ! ${cat}/${slug}/${lang}.md has no title — skipped`);
          continue;
        }
        langs[lang] = {
          ...data,
          facts: (Array.isArray(data.facts) ? data.facts : [])
            .map((r) => r.split('|').map((s) => s.trim()))
            .filter((p) => p.length >= 2),
          blocks: parseBlocks(body),
        };
      }
      if (!Object.keys(langs).length) {
        console.warn(`  ! ${cat}/${slug}/ has no usable translation — skipped`);
        continue;
      }
      pieces.push({ slug, meta, langs, resolve,
                    folder: meta.type === 'project' ? 'projects' : 'insights' });
    }
  }
  // Newest first inside a listing; `order` in meta.json breaks ties explicitly.
  pieces.sort((a, b) =>
    (b.meta.published || '').localeCompare(a.meta.published || '') ||
    (a.meta.order ?? 999) - (b.meta.order ?? 999));
  return pieces;
}

/* ─────────────────────────────────────────────────────────────────────────
   Page chrome
   ───────────────────────────────────────────────────────────────────────── */

function head(o) {
  const L = LANG_META[o.lang];
  const alts = o.alts
    .map((a) => `<link rel="alternate" hreflang="${LANG_META[a].hreflang}" href="${DOMAIN}/${LANG_META[a].slug}/${o.path}">`)
    .join('\n');
  // x-default points at English when English exists, otherwise at the only
  // language that does. Never at a URL this build did not write.
  const xdef = o.alts.includes('en') ? 'en' : o.alts[0];
  const ogImg = `${DOMAIN}${imgUrl(o.hero)}`;
  const ld = o.ld ? `\n<script type="application/ld+json">\n${JSON.stringify(o.ld)}\n</script>` : '';
  const robots = o.noindex ? '\n<meta name="robots" content="noindex, follow">' : '';
  return `<!DOCTYPE html>
<html lang="${L.code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>${attr(o.title)} | CnC Venture</title>
<meta name="description" content="${attr(o.desc)}">${robots}

<link rel="canonical" href="${DOMAIN}/${L.slug}/${o.path}">
${alts}
<link rel="alternate" hreflang="x-default" href="${DOMAIN}/${LANG_META[xdef].slug}/${o.path}">

<meta name="theme-color" content="#02383D">

<meta property="og:type" content="${o.ogType || 'website'}">
<meta property="og:site_name" content="CnC Venture">
<meta property="og:locale" content="${L.oglocale}">
<meta property="og:locale:alternate" content="${L.ogalt}">
<meta property="og:title" content="${attr(o.title)}">
<meta property="og:description" content="${attr(o.desc)}">
<meta property="og:url" content="${DOMAIN}/${L.slug}/${o.path}">
<meta property="og:image" content="${attr(ogImg)}">
<meta property="og:image:alt" content="${attr(o.heroAlt || '')}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${attr(o.title)}">
<meta name="twitter:description" content="${attr(o.desc)}">
<meta name="twitter:image" content="${attr(ogImg)}">

<link rel="icon" href="${FAVICON}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="${o.lang === 'zh-tw' ? FONTS_ZH : FONTS_EN}" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">${ld}
</head>
<body>
`;
}

function nav(lang, pagePath, alts) {
  const ui = UI[lang];
  const s = LANG_META[lang].slug;
  const links = ui.nav.map(([t, h]) => `<a href="${attr(h.replace('{s}', s))}">${esc(t)}</a>`).join('');
  const mob = ui.nav.map(([t, h]) => `<li><a href="${attr(h.replace('{s}', s))}">${esc(t)}</a></li>`).join('');

  // The switch offers the counterpart page only when it was actually written;
  // otherwise it goes to that language's homepage rather than a 404.
  const target = (l) => (alts.includes(l) ? `/${LANG_META[l].slug}/${pagePath}` : `/${LANG_META[l].slug}/`);
  const langBlock = (id) =>
    `<div class="lang" role="group" aria-label="${attr(ui.langLabel)}">` +
    `<a href="${attr(target('en'))}" lang="en"${lang === 'en' ? ' aria-current="true"' : ''}>EN</a>` +
    '<span class="bar" aria-hidden="true"></span>' +
    `<a href="${attr(target('zh-tw'))}" lang="zh-Hant"${lang === 'zh-tw' ? ' aria-current="true"' : ''}>繁中</a></div>`;

  return `<a class="skip-link" href="#main">${esc(ui.skip)}</a>

<header class="nav always-solid stuck" id="nav">
  <a class="mark" href="/${s}/"><b>CnC</b><span class="v serif">Venture</span></a>
  <nav class="nav-links" aria-label="${attr(ui.navLabel)}">${links}</nav>
  <div class="nav-right">
    ${langBlock()}
    <a class="btn btn-solid" href="${CTA}" target="_blank" rel="noopener noreferrer">${esc(ui.cta)} <span class="arw" aria-hidden="true">→</span></a>
    <button class="nav-toggle" id="navToggle" type="button"
            aria-label="${attr(ui.open)}" aria-expanded="false" aria-controls="mobileNav"
            data-label-open="${attr(ui.open)}" data-label-close="${attr(ui.close)}">
      <i aria-hidden="true"></i><i aria-hidden="true"></i>
    </button>
  </div>
</header>

<div class="mobile-nav" id="mobileNav" data-open="false" aria-hidden="true">
  <div class="mobile-nav-top">
    <a class="mark" href="/${s}/"><b>CnC</b><span class="v serif">Venture</span></a>
    <button class="close-btn" id="navClose" type="button" aria-label="${attr(ui.close)}"><span aria-hidden="true">✕</span></button>
  </div>
  <nav aria-label="${attr(ui.navLabelMobile)}"><ul>${mob}</ul></nav>
  <div class="mobile-nav-foot">
    ${langBlock()}
    <a class="btn btn-solid" href="${CTA}" target="_blank" rel="noopener noreferrer">${esc(ui.ctaLong)} <span class="arw" aria-hidden="true">→</span></a>
  </div>
</div>
`;
}

function footer(lang) {
  const ui = UI[lang];
  const s = LANG_META[lang].slug;
  const cols = ui.footer.map(([hd, items]) => {
    const li = items.map(([t, h]) => {
      if (!h) return `<li><span>${esc(t)}</span></li>`;
      const ext = /^https?:/.test(h) ? ' target="_blank" rel="noopener noreferrer"' : '';
      return `<li><a href="${attr(h.replace('{s}', s))}"${ext}>${esc(t)}</a></li>`;
    }).join('');
    return `<div><h3>${esc(hd)}</h3><ul>${li}</ul></div>`;
  }).join('');
  return `
<footer class="foot">
  <div class="wrap">
    <div class="foot-top">
      <div>
        <a class="mark" href="/${s}/"><b>CnC</b><span class="v serif">Venture</span></a>
        <div class="tagline serif">${esc(ui.tagline)}</div>
      </div>
      ${cols}
    </div>
    <div class="foot-bot">
      <span>${esc(ui.copyright)}</span>
      <div class="lang" role="group" aria-label="${attr(ui.langLabel)}">
        <a href="/en/" lang="en">English</a>
        <span class="bar" aria-hidden="true"></span>
        <a href="/zh-tw/" lang="zh-Hant">繁體中文</a>
      </div>
      <span>${esc(ui.route)}</span>
    </div>
  </div>
</footer>

<script src="/js/main.js" defer></script>
</body>
</html>
`;
}

function card(p, lang) {
  const s = LANG_META[lang].slug;
  const r = p.langs[lang];
  const cat = CAT_BY_SLUG[p.meta.category];
  const m = p.meta.type === 'project' ? (r.statusShort || '') : (r.readingTime || '');
  const sep = m ? '<span class="sep" aria-hidden="true"></span>' : '';
  return `
      <a class="rel reveal" href="/${s}/${p.folder}/${p.slug}/">
        <div class="frame"><img src="${attr(imgUrl(p.meta.hero))}" alt="${attr(r.heroAlt)}" loading="lazy" decoding="async"></div>
        <div class="kicker"><span class="cat">${esc(cat ? cat[lang] : '')}</span>${sep}<span class="m">${esc(m)}</span></div>
        <h3 class="serif">${esc(r.title)}</h3>
        <p>${esc(r.cardBlurb || '')}</p>
      </a>`;
}

function closingCta(lang) {
  const ui = UI[lang];
  return `
<section class="doc-cta">
  <div class="wrap">
    <div class="label reveal">${esc(ui.ctaLabel)}</div>
    <h2 class="serif reveal" style="--d:80ms">${esc(ui.docCtaHead)}</h2>
    <p class="reveal" style="--d:160ms">${esc(ui.docCtaBody)}</p>
    <a class="btn btn-solid reveal" style="--d:240ms" href="${CTA}" target="_blank" rel="noopener noreferrer">${esc(ui.docCtaBtn)} <span class="arw" aria-hidden="true">→</span></a>
  </div>
</section>
`;
}

function catNav(lang, current) {
  const s = LANG_META[lang].slug;
  const all = `<a href="/${s}/insights/"${!current ? ' aria-current="page"' : ''}>${esc(UI[lang].allLabel || (lang === 'en' ? 'All' : '全部'))}</a>`;
  const items = CATS.map((c) =>
    `<a href="/${s}/insights/${c.slug}/"${current === c.slug ? ' aria-current="page"' : ''}>${esc(c[lang])}</a>`).join('');
  return `<nav class="cat-nav" aria-label="${attr(UI[lang].catLabel)}">${all}${items}</nav>`;
}

/* ─────────────────────────────────────────────────────────────────────────
   Pages
   ───────────────────────────────────────────────────────────────────────── */

const urls = [];   // for sitemap.xml

function renderPiece(p, lang, siblings, byslug) {
  const ui = UI[lang];
  const s = LANG_META[lang].slug;
  const r = p.langs[lang];
  const cat = CAT_BY_SLUG[p.meta.category];
  const isProject = p.meta.type === 'project';
  const pagePath = `${p.folder}/${p.slug}/`;
  const alts = LANGS.filter((l) => p.langs[l]);

  const crumbRoot = isProject ? ui.projects : ui.journal;
  const crumbRootHref = isProject ? `/${s}/projects/` : `/${s}/insights/`;
  const crumbs =
    `<nav class="crumbs" aria-label="${attr(ui.breadcrumb)}">` +
    `<a href="/${s}/">${esc(ui.home)}</a><span class="sep" aria-hidden="true">/</span>` +
    `<a href="${crumbRootHref}">${esc(crumbRoot)}</a><span class="sep" aria-hidden="true">/</span>` +
    `<span aria-current="page">${esc(r.crumb || r.title)}</span></nav>`;

  const statusPill = isProject && r.statusShort
    ? `<span class="status"><span class="dot" aria-hidden="true"></span>${esc(r.statusShort)}</span>` : '';

  const metaRow = isProject
    ? `<span>${esc(ui.industryLabel)}: ${esc(r.industry || '')}</span>` +
      `<span>${esc(ui.updatedLabel)}: ${esc(r.dateLabel || '')}</span>`
    : `<span>${esc(ui.catLabel)}: ${esc(cat ? cat[lang] : '')}</span>` +
      (r.readingTime ? `<span>${esc(r.readingTime)}</span>` : '') +
      `<span>${esc(ui.updatedLabel)}: ${esc(r.dateLabel || '')}</span>`;

  // The project panel appears exactly once, and only on projects.
  let overview = '';
  if (isProject && r.facts.length) {
    const rows = r.facts.map(([k, v], n) =>
      `<div class="row${n === 0 ? ' live' : ''}"><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join('');
    overview = `<section class="overview reveal" aria-label="${attr(ui.infoLabel)}">` +
      `<div class="lbl">${esc(ui.infoLabel)}</div><dl>${rows}</dl></section>`;
  }

  // Previous / next runs inside the same section, in listing order.
  const idx = siblings.findIndex((x) => x.slug === p.slug);
  const pn = (dir, other) => {
    if (!other) return '<span></span>';
    const label = dir === 'prev' ? ui.prevLabel : ui.nextLabel;
    const arrow = dir === 'prev' ? '←' : '→';
    const inner = dir === 'prev'
      ? `<span class="arw" aria-hidden="true">${arrow}</span> ${esc(label)}`
      : `${esc(label)} <span class="arw" aria-hidden="true">${arrow}</span>`;
    return `<a class="pn ${dir}" href="/${s}/${other.folder}/${other.slug}/">` +
      `<span class="dir">${inner}</span>` +
      `<h3 class="serif">${esc(other.langs[lang].title)}</h3></a>`;
  };
  const prev = siblings[idx - 1];
  const next = siblings[idx + 1];
  const prevnext = (prev || next) ? `
<nav class="prevnext" aria-label="${attr(ui.pagerLabel)}">
  <div class="wrap"><div class="row">${pn('prev', prev)}${pn('next', next)}</div></div>
</nav>
` : '';

  // Related reading: explicit picks first, then same-category fallback, so a
  // new piece always has neighbours without anyone maintaining a list.
  const picked = (p.meta.related || [])
    .map((sl) => byslug[sl]).filter((x) => x && x.langs[lang] && x.slug !== p.slug);
  const fallback = siblings.filter((x) =>
    x.slug !== p.slug && !picked.some((y) => y.slug === x.slug));
  const related = [...picked, ...fallback].slice(0, 3);
  const relatedBlock = related.length ? `
<section class="related">
  <div class="wrap">
    <div class="hd reveal">
      <h2 class="serif">${esc(ui.related)}</h2>
      <span class="note">${esc(ui.relatedNote)}</span>
    </div>
    <div class="rel-grid${related.length === 3 ? ' three' : ''}">${related.map((x) => card(x, lang)).join('')}
    </div>
  </div>
</section>
` : '';

  const ld = {
    '@context': 'https://schema.org',
    '@type': isProject ? 'CreativeWork' : 'Article',
    headline: r.title,
    description: r.description || '',
    inLanguage: LANG_META[lang].code,
    image: `${DOMAIN}${imgUrl(p.meta.hero)}`,
    datePublished: p.meta.published,
    dateModified: p.meta.updated || p.meta.published,
    mainEntityOfPage: { '@type': 'WebPage', '@id': `${DOMAIN}/${s}/${pagePath}` },
    publisher: { '@type': 'Organization', name: 'CnC Venture' },
  };

  const doc = head({
    lang, path: pagePath, alts, title: r.title, desc: r.description || r.standfirst || '',
    hero: p.meta.hero, heroAlt: r.heroAlt, ogType: 'article', ld,
  }) + nav(lang, pagePath, alts) + `
<main id="main">
<article class="doc on-light">

  <div class="wide doc-opening reveal">
    <figure>
      <img src="${attr(imgUrl(p.meta.hero))}" alt="${attr(r.heroAlt)}" fetchpriority="high" decoding="async">
      ${r.heroCaption ? `<figcaption>${inlineMd(r.heroCaption)}</figcaption>` : ''}
    </figure>
  </div>

  ${crumbs}

  <div class="doc-eyebrow reveal">
    <span class="cat">${esc(cat ? cat[lang] : '')}</span>
    ${statusPill}
  </div>

  <h1 class="serif reveal" style="--d:60ms">${esc(r.title)}</h1>
  ${r.standfirst ? `<p class="doc-standfirst reveal" style="--d:130ms">${inlineMd(r.standfirst)}</p>` : ''}
  <div class="doc-meta reveal" style="--d:200ms">${metaRow}</div>

  ${overview}

  <div class="prose">
    ${renderBlocks(r.blocks, p.resolve)}
  </div>

  <div class="doc-end">
    <a class="backlink" href="${crumbRootHref}"><span class="arw" aria-hidden="true">←</span> ${esc(isProject ? ui.backProjects : ui.back)}</a>
  </div>

</article>
${prevnext}${relatedBlock}${closingCta(lang)}</main>
${footer(lang)}`;

  const bytes = write(path.join(ROOT, s, p.folder, p.slug, 'index.html'), doc);
  urls.push({ loc: `${DOMAIN}/${s}/${pagePath}`, lastmod: p.meta.updated || p.meta.published,
              alts, path: pagePath });
  return bytes;
}

function renderListing(o) {
  const { lang, pagePath, title, desc, stand, crumb, hero, heroAlt,
          pieces, current, showCatNav, empty, noindex } = o;
  const ui = UI[lang];
  const s = LANG_META[lang].slug;
  const alts = o.alts || LANGS;
  const crumbs =
    `<nav class="crumbs" aria-label="${attr(ui.breadcrumb)}">` +
    `<a href="/${s}/">${esc(ui.home)}</a><span class="sep" aria-hidden="true">/</span>` +
    (o.parent ? `<a href="${o.parent[1]}">${esc(o.parent[0])}</a><span class="sep" aria-hidden="true">/</span>` : '') +
    `<span aria-current="page">${esc(crumb)}</span></nav>`;

  const grid = pieces.length
    ? `<section class="related" style="background:var(--warm-white)">
  <div class="wrap">
    <div class="rel-grid three" style="margin-top:0">${pieces.map((p) => card(p, lang)).join('')}
    </div>
  </div>
</section>`
    : `<section class="listing empty on-light"><div class="wrap"><p class="doc-standfirst">${esc(empty || ui.emptyCategory)}</p></div></section>`;

  const doc = head({ lang, path: pagePath, alts, title, desc, hero, heroAlt, noindex }) +
    nav(lang, pagePath, alts) + `
<main id="main">
<section class="listing on-light">
  <div class="wrap">
    ${crumbs}
    <h1 class="serif reveal">${esc(title)}</h1>
    <p class="doc-standfirst reveal" style="--d:120ms">${esc(stand)}</p>
    ${showCatNav ? catNav(lang, current) : ''}
  </div>
</section>
${grid}
${closingCta(lang)}</main>
${footer(lang)}`;

  const bytes = write(path.join(ROOT, s, pagePath, 'index.html'), doc);
  if (!noindex) urls.push({ loc: `${DOMAIN}/${s}/${pagePath}`, alts, path: pagePath });
  return bytes;
}

function sitemap() {
  const seen = new Set();
  const rows = [];
  // The two homepages are written by tools/build.py; they belong in the map.
  for (const l of LANGS) {
    rows.push({ loc: `${DOMAIN}/${LANG_META[l].slug}/`, alts: LANGS, path: '' });
  }
  rows.push(...urls);
  const body = rows.filter((u) => !seen.has(u.loc) && seen.add(u.loc)).map((u) => {
    const links = u.alts.map((a) =>
      `\n    <xhtml:link rel="alternate" hreflang="${LANG_META[a].hreflang}" href="${DOMAIN}/${LANG_META[a].slug}/${u.path}"/>`).join('');
    const xdef = u.alts.includes('en') ? 'en' : u.alts[0];
    return `  <url>\n    <loc>${u.loc}</loc>` +
      (u.lastmod ? `\n    <lastmod>${u.lastmod}</lastmod>` : '') + links +
      `\n    <xhtml:link rel="alternate" hreflang="x-default" href="${DOMAIN}/${LANG_META[xdef].slug}/${u.path}"/>` +
      '\n  </url>';
  }).join('\n');
  write(path.join(ROOT, 'sitemap.xml'),
    '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n' +
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + '\n</urlset>\n');
  return seen.size;
}

/* ─────────────────────────────────────────────────────────────────────────
   Build
   ───────────────────────────────────────────────────────────────────────── */

function main() {
  const t0 = Date.now();
  console.log('\nCnC Venture — building /content\n');

  const pieces = loadPieces();
  const byslug = Object.fromEntries(pieces.map((p) => [p.slug, p]));

  // Guards. These are the two mistakes that produce a silently wrong site
  // rather than an error, so the build refuses to finish instead.
  const catSlugs = new Set(CATS.map((c) => c.slug));
  for (const p of pieces) {
    if (p.folder === 'insights' && catSlugs.has(p.slug)) {
      throw new Error(
        `slug "${p.slug}" collides with the category listing at /insights/${p.slug}/ — rename the folder`);
    }
    if (!fs.existsSync(path.join(IMG, p.meta.hero))) {
      throw new Error(`${p.slug}: hero image /img/${p.meta.hero} does not exist`);
    }
    for (const lang of LANGS) {
      const r = p.langs[lang];
      if (!r) continue;
      for (const b of r.blocks) {
        if (b.t !== 'image') continue;
        for (const f of b.files) {
          if (!fs.existsSync(path.join(IMG, p.resolve(f)))) {
            throw new Error(`${p.slug}/${lang}.md references a missing image: ${f}`);
          }
        }
        if (!b.alt) console.warn(`  ! ${p.slug}/${lang}.md — image ${b.files[0]} has no Alt:`);
      }
    }
    const missing = LANGS.filter((l) => !p.langs[l]);
    if (missing.length) console.log(`  · ${p.slug} — published in ${LANGS.filter((l) => p.langs[l]).join(', ')} only`);
  }

  let bytes = 0;
  let pages = 0;

  for (const lang of LANGS) {
    const live = pieces.filter((p) => p.langs[lang]);
    const articles = live.filter((p) => p.meta.type === 'article');
    const projects = live.filter((p) => p.meta.type === 'project');
    const s = LANG_META[lang].slug;
    const ui = UI[lang];

    for (const p of live) {
      const siblings = live.filter((x) =>
        x.meta.type === p.meta.type &&
        (p.meta.type === 'project' || x.meta.category === p.meta.category));
      bytes += renderPiece(p, lang, siblings, byslug);
      pages++;
      console.log(`  /${s}/${p.folder}/${p.slug}/`);
    }

    // Journal index — every article, whatever its category.
    bytes += renderListing({
      lang, pagePath: 'insights/', pieces: articles, showCatNav: true,
      title: ui.journal, crumb: ui.journal,
      desc: ui.journalDesc, stand: ui.journalStand,
      hero: 'insight-lead.jpg', heroAlt: ui.journalHeroAlt,
    });
    pages++;

    // One listing per category. An empty category still gets a page so the
    // navigation is never a dead link, but it stays out of the index.
    for (const c of CATS) {
      const inCat = live.filter((p) => p.meta.category === c.slug);
      bytes += renderListing({
        lang, pagePath: `insights/${c.slug}/`, pieces: inCat, showCatNav: true, current: c.slug,
        title: c[lang], crumb: c[lang],
        desc: lang === 'en' ? c.blurb_en : c.blurb_zh,
        stand: lang === 'en' ? c.blurb_en : c.blurb_zh,
        hero: inCat.length ? inCat[0].meta.hero : 'insight-lead.jpg',
        heroAlt: inCat.length ? inCat[0].langs[lang].heroAlt : ui.journalHeroAlt,
        parent: [ui.journal, `/${s}/insights/`],
        noindex: inCat.length === 0,
      });
      pages++;
    }

    // Expansion in Progress keeps its own section and its own URL.
    bytes += renderListing({
      lang, pagePath: 'projects/', pieces: projects,
      title: ui.projects, crumb: ui.projects,
      desc: ui.projectsDesc, stand: ui.projectsStand,
      hero: 'hero-startup-project.jpg', heroAlt: ui.projectsHeroAlt,
    });
    pages++;
    console.log(`  /${s}/insights/  /${s}/projects/  + ${CATS.length} category pages`);
  }

  const n = sitemap();
  console.log(`\n  sitemap.xml — ${n} URLs`);
  console.log(`\n${pages} pages, ${(bytes / 1024).toFixed(0)} KB, ${Date.now() - t0} ms\n`);
}

main();
