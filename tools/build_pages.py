"""Render the Journal articles and Expansion project pages, both languages.

One renderer, one stylesheet, one script. Every page is a static HTML file with
its own URL, title, canonical and hreflang pair — no modal-only content, no
framework, nothing to build on Netlify.

Run:  python3 tools/build_pages.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
DOMAIN = 'https://cncventure.org'
CTA = 'https://www.surveycake.com/s/3qKZN'

import assets  # noqa: E402
from content_pages import PAGES, UI  # noqa: E402

VMAP = assets.build_map(os.path.join(ROOT, 'img'))

FONTS_EN = ('https://fonts.googleapis.com/css2?'
            'family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..600'
            '&family=Inter:wght@300;400;500;600&display=swap')
FONTS_ZH = (FONTS_EN.replace('&display=swap', '')
            + '&family=Noto+Sans+TC:wght@400;500;700;800;900&display=swap')

LANGS = {
    'en':    dict(code='en',          slug='en',    oglocale='en_US', ogalt='zh_TW', fonts=FONTS_EN),
    'zh-tw': dict(code='zh-Hant-TW',  slug='zh-tw', oglocale='zh_TW', ogalt='en_US', fonts=FONTS_ZH),
}

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='12' fill='%2302383D'/%3E%3Ctext x='32' y='43' "
           "font-family='Georgia,serif' font-size='30' fill='%23FBF8F3' text-anchor='middle'%3EC"
           "%3C/text%3E%3C/svg%3E")


# ── blocks ───────────────────────────────────────────────────────────────────
def render_blocks(blocks):
    out = []
    for kind, *rest in blocks:
        if kind == 'h2':
            out.append(f'<h2>{rest[0]}</h2>')
        elif kind == 'h3':
            out.append(f'<h3>{rest[0]}</h3>')
        elif kind == 'p':
            out.append(f'<p>{rest[0]}</p>')
        elif kind == 'ul':
            items = ''.join(f'<li>{i}</li>' for i in rest[0])
            out.append(f'<ul>{items}</ul>')
        elif kind == 'ol':
            items = ''.join(f'<li>{i}</li>' for i in rest[0])
            out.append(f'<ol>{items}</ol>')
        elif kind == 'pull':
            who = f'<div class="who">{rest[1]}</div>' if len(rest) > 1 and rest[1] else ''
            out.append(f'<blockquote class="pull"><p class="serif">{rest[0]}</p>{who}</blockquote>')
        elif kind == 'panel':
            label, title, items = rest[0], rest[1], rest[2]
            foot = f'<div class="cnote">{rest[3]}</div>' if len(rest) > 3 and rest[3] else ''
            li = ''.join(f'<li>{i}</li>' for i in items)
            out.append(f'<aside class="callout"><div><div class="lbl">{label}</div>'
                       f'<h3 class="serif">{title}</h3></div>'
                       f'<div><ul>{li}</ul>{foot}</div></aside>')
        elif kind == 'fig':
            cap = f'<figcaption>{rest[2]}</figcaption>' if len(rest) > 2 and rest[2] else ''
            out.append(f'<figure class="docfig"><img src="/img/{rest[0]}" alt="{rest[1]}" '
                       f'loading="lazy">{cap}</figure>')
        elif kind == 'advisory':
            out.append(f'<aside class="advisory">{rest[0]}</aside>')
        else:
            raise ValueError(f'unknown block: {kind}')
    return '\n        '.join(out)


def chrome_head(lang, page, slug, path):
    L = LANGS[lang]
    ui = UI[lang]
    url = f'{DOMAIN}/{L["slug"]}/{path}'
    alt_en = f'{DOMAIN}/en/{path}'
    alt_zh = f'{DOMAIN}/zh-tw/{path}'
    og_img = f'{DOMAIN}/img/{page["hero"]}'
    ld = ''
    if page.get('type') == 'article':
        # Article structured data, limited to what is actually known. No author
        # credentials, no publisher claims that cannot be substantiated.
        ld = f'''
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article",
"headline":{page['title']!r},
"description":{page['desc']!r},
"inLanguage":"{L['code']}",
"image":"{og_img}",
"datePublished":"{page['published']}","dateModified":"{page['updated']}",
"mainEntityOfPage":{{"@type":"WebPage","@id":"{url}"}},
"publisher":{{"@type":"Organization","name":"CnC Venture"}}}}
</script>'''.replace("'", '"')
    return f'''<!DOCTYPE html>
<html lang="{L['code']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{page['title']} | CnC Venture</title>
<meta name="description" content="{page['desc']}">

<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="zh-Hant-TW" href="{alt_zh}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">

<meta name="theme-color" content="#02383D">

<meta property="og:type" content="article">
<meta property="og:site_name" content="CnC Venture">
<meta property="og:locale" content="{L['oglocale']}">
<meta property="og:locale:alternate" content="{L['ogalt']}">
<meta property="og:title" content="{page['title']}">
<meta property="og:description" content="{page['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:alt" content="{page['heroAlt']}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{page['title']}">
<meta name="twitter:description" content="{page['desc']}">
<meta name="twitter:image" content="{og_img}">

<link rel="icon" href="{FAVICON}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{L['fonts']}" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">{ld}
</head>
<body>
'''


def nav(lang, path):
    ui = UI[lang]
    s = LANGS[lang]['slug']
    other = 'zh-tw' if lang == 'en' else 'en'
    links = ''.join(
        f'<a href="{h.format(s=s)}">{t}</a>' for t, h in ui['nav'])
    mob = ''.join(
        f'<li><a href="{h.format(s=s)}">{t}</a></li>' for t, h in ui['nav'])
    en_cur = ' aria-current="true"' if lang == 'en' else ''
    zh_cur = ' aria-current="true"' if lang == 'zh-tw' else ''
    # The language switch points at this page's counterpart, not the homepage.
    lang_block = (f'<div class="lang" role="group" aria-label="{ui["langLabel"]}">'
                  f'<a href="/en/{path}" lang="en"{en_cur}>EN</a>'
                  f'<span class="bar" aria-hidden="true"></span>'
                  f'<a href="/zh-tw/{path}" lang="zh-Hant"{zh_cur}>繁中</a></div>')
    return f'''<a class="skip-link" href="#main">{ui['skip']}</a>

<header class="nav always-solid stuck" id="nav">
  <a class="mark" href="/{s}/"><b>CnC</b><span class="v serif">Venture</span></a>
  <nav class="nav-links" aria-label="{ui['navLabel']}">{links}</nav>
  <div class="nav-right">
    {lang_block}
    <a class="btn btn-solid" href="{CTA}" target="_blank" rel="noopener noreferrer">{ui['cta']} <span class="arw" aria-hidden="true">→</span></a>
    <button class="nav-toggle" id="navToggle" type="button"
            aria-label="{ui['open']}" aria-expanded="false" aria-controls="mobileNav"
            data-label-open="{ui['open']}" data-label-close="{ui['close']}">
      <i aria-hidden="true"></i><i aria-hidden="true"></i>
    </button>
  </div>
</header>

<div class="mobile-nav" id="mobileNav" data-open="false" aria-hidden="true">
  <div class="mobile-nav-top">
    <a class="mark" href="/{s}/"><b>CnC</b><span class="v serif">Venture</span></a>
    <button class="close-btn" id="navClose" type="button" aria-label="{ui['close']}"><span aria-hidden="true">✕</span></button>
  </div>
  <nav aria-label="{ui['navLabelMobile']}"><ul>{mob}</ul></nav>
  <div class="mobile-nav-foot">
    {lang_block}
    <a class="btn btn-solid" href="{CTA}" target="_blank" rel="noopener noreferrer">{ui['ctaLong']} <span class="arw" aria-hidden="true">→</span></a>
  </div>
</div>
'''


def footer(lang):
    ui = UI[lang]
    s = LANGS[lang]['slug']
    cols = ''
    for head, items in ui['footer']:
        li = ''.join(
            (f'<li><a href="{h.format(s=s)}"' +
             (' target="_blank" rel="noopener noreferrer"' if h.startswith('http') else '') +
             f'>{t}</a></li>') if h else f'<li><span>{t}</span></li>'
            for t, h in items)
        cols += f'<div><h3>{head}</h3><ul>{li}</ul></div>'
    return f'''
<footer class="foot">
  <div class="wrap">
    <div class="foot-top">
      <div>
        <a class="mark" href="/{s}/"><b>CnC</b><span class="v serif">Venture</span></a>
        <div class="tagline serif">{ui['tagline']}</div>
      </div>
      {cols}
    </div>
    <div class="foot-bot">
      <span>{ui['copyright']}</span>
      <div class="lang" role="group" aria-label="{ui['langLabel']}">
        <a href="/en/" lang="en">English</a>
        <span class="bar" aria-hidden="true"></span>
        <a href="/zh-tw/" lang="zh-Hant">繁體中文</a>
      </div>
      <span>{ui['route']}</span>
    </div>
  </div>
</footer>

<script src="/js/main.js" defer></script>
</body>
</html>
'''


def related_block(lang, slugs):
    ui = UI[lang]
    s = LANGS[lang]['slug']
    cards = ''
    for sl in slugs:
        r = PAGES[sl][lang]
        folder = 'insights' if PAGES[sl]['type'] == 'article' else 'projects'
        m = r['readingTime'] if PAGES[sl]['type'] == 'article' else r['statusShort']
        cards += f"""
      <a class="rel reveal" href="/{s}/{folder}/{sl}/">
        <div class="frame"><img src="/img/{PAGES[sl]['hero']}" alt="{r['heroAlt']}" loading="lazy"></div>
        <div class="kicker"><span class="cat">{r['category']}</span><span class="sep" aria-hidden="true"></span><span class="m">{m}</span></div>
        <h3 class="serif">{r['title']}</h3>
        <p>{r['cardBlurb']}</p>
      </a>"""
    return f"""
<section class="related">
  <div class="wrap">
    <div class="hd reveal">
      <h2 class="serif">{ui['related']}</h2>
      <span class="note">{ui['relatedNote']}</span>
    </div>
    <div class="rel-grid">{cards}
    </div>
  </div>
</section>
"""


def closing_cta(lang):
    ui = UI[lang]
    return f"""
<section class="doc-cta">
  <div class="wrap">
    <div class="label reveal">{ui['ctaLabel']}</div>
    <h2 class="serif reveal" style="--d:80ms">{ui['docCtaHead']}</h2>
    <p class="reveal" style="--d:160ms">{ui['docCtaBody']}</p>
    <a class="btn btn-solid reveal" style="--d:240ms" href="{CTA}" target="_blank" rel="noopener noreferrer">{ui['docCtaBtn']} <span class="arw" aria-hidden="true">→</span></a>
  </div>
</section>
"""


def build_page(slug, lang):
    meta = PAGES[slug]
    # hero image lives on the shared record; both languages use the same file
    p = dict(meta[lang], hero=meta['hero'], type=meta['type'])
    ui = UI[lang]
    s = LANGS[lang]['slug']
    folder = 'insights' if meta['type'] == 'article' else 'projects'
    path = f'{folder}/{slug}/'

    crumb_root = ui['journal'] if meta['type'] == 'article' else ui['projects']
    crumbs = (f'<nav class="crumbs" aria-label="{ui["breadcrumb"]}">'
              f'<a href="/{s}/">{ui["home"]}</a><span class="sep" aria-hidden="true">/</span>'
              f'<a href="/{s}/#{"insights" if meta["type"]=="article" else "stories"}">{crumb_root}</a>'
              f'<span class="sep" aria-hidden="true">/</span>'
              f'<span aria-current="page">{p["crumb"]}</span></nav>')

    # Article metadata appears exactly once. Projects get the information
    # panel; articles get the meta rule. Neither repeats the other.
    if meta['type'] == 'article':
        status_pill = ''
        meta_row = (f'<span>{ui["catLabel"]}: {p["category"]}</span>'
                    f'<span>{p["readingTime"]}</span>'
                    f'<span>{ui["updatedLabel"]}: {p["dateLabel"]}</span>')
        infocard = ''
    else:
        status_pill = f'<span class="status"><span class="dot" aria-hidden="true"></span>{p["statusShort"]}</span>'
        meta_row = (f'<span>{ui["industryLabel"]}: {p["industry"]}</span>'
                    f'<span>{ui["updatedLabel"]}: {p["dateLabel"]}</span>')
        rows = ''
        for i, (k, v) in enumerate(p['facts']):
            live = ' live' if i == 0 else ''
            rows += f'<div class="row{live}"><dt>{k}</dt><dd>{v}</dd></div>'
        infocard = (f'<section class="infocard reveal" aria-label="{ui["infoLabel"]}">'
                    f'<div class="hd">{ui["infoLabel"]}</div><dl>{rows}</dl></section>')

    doc = f'''{chrome_head(lang, p, slug, path)}{nav(lang, path)}
<main id="main">
<article class="doc on-light">

  <div class="wide doc-opening reveal">
    <figure>
      <img src="/img/{meta['hero']}" alt="{p['heroAlt']}">
      {f'<figcaption>{p["heroCaption"]}</figcaption>' if p.get('heroCaption') else ''}
    </figure>
  </div>

  {crumbs}

  <div class="doc-eyebrow reveal">
    <span class="cat">{p['category']}</span>
    {status_pill}
  </div>

  <h1 class="serif reveal" style="--d:60ms">{p['title']}</h1>
  <p class="doc-standfirst reveal" style="--d:130ms">{p['standfirst']}</p>
  <div class="doc-meta reveal" style="--d:200ms">{meta_row}</div>

  {infocard}

  <div class="prose">
    {render_blocks(p['body'])}
  </div>

  <div class="doc-end">
    <a class="backlink" href="/{s}/{folder}/"><span class="arw" aria-hidden="true">←</span> {ui['back'] if meta['type']=='article' else ui['backProjects']}</a>
  </div>

</article>
{related_block(lang, meta['related'])}{closing_cta(lang)}</main>
{footer(lang)}'''

    out_dir = os.path.join(ROOT, s, folder, slug)
    os.makedirs(out_dir, exist_ok=True)
    doc = assets.version(doc, VMAP)
    open(os.path.join(out_dir, 'index.html'), 'w').write(doc)
    return len(doc)


if __name__ == '__main__':
    total = 0
    for slug in PAGES:
        for lang in ('en', 'zh-tw'):
            n = build_page(slug, lang)
            total += n
            print(f'  /{LANGS[lang]["slug"]}/'
                  f'{"insights" if PAGES[slug]["type"]=="article" else "projects"}/{slug}/'
                  f'  {n/1024:5.1f} KB')
    print(f'\n{len(PAGES)*2} pages, {total/1024:.0f} KB total')


# ── Section index pages ─────────────────────────────────────────────────────
INDEX_META = {
    'insights': {
        'en': dict(title='The Expansion Journal',
                   desc='A business magazine on building in America — market reports, city '
                        'guides, and the considerations behind each decision.',
                   stand='Market overviews, city guides and practical playbooks for companies '
                         'building a presence in the United States.',
                   crumb='The Expansion Journal', hero='insight-lead.jpg',
                   heroAlt='The Arizona landscape at midday'),
        'zh-tw': dict(title='拓展誌',
                      desc='一本關於「在美國落地」的商業誌——市場觀察、城市指南，'
                           '以及每個決定背後的真實考量。',
                      stand='給正在美國建立據點的企業：市場觀察、城市指南與實務指引。',
                      crumb='拓展誌', hero='insight-lead.jpg',
                      heroAlt='正午時分的亞利桑那地景'),
    },
    'projects': {
        'en': dict(title='Expansion in Progress',
                   desc='Live engagements, reported as they stand. These are ongoing '
                        'projects, not finished case studies.',
                   stand='Live engagements, reported as they stand. We will publish outcomes '
                         'when there are outcomes to publish.',
                   crumb='Expansion in Progress', hero='hero-startup-project.jpg',
                   heroAlt='Office towers in downtown Phoenix'),
        'zh-tw': dict(title='進行中的專案',
                      desc='進行中的合作，如實呈現。這些是正在進行的專案，不是完成的案例。',
                      stand='進行中的合作，如實呈現。有成果的時候，我們再談成果。',
                      crumb='進行中的專案', hero='hero-startup-project.jpg',
                      heroAlt='Phoenix 市中心的辦公大樓'),
    },
}


def build_index(folder, lang):
    ui = UI[lang]
    s = LANGS[lang]['slug']
    m = INDEX_META[folder][lang]
    page = dict(m, title=m['title'], desc=m['desc'], heroAlt=m['heroAlt'],
                hero=m['hero'], type='index')
    slugs = [k for k, v in PAGES.items()
             if v['type'] == ('article' if folder == 'insights' else 'project')]
    cards = ''
    for sl in slugs:
        r = PAGES[sl][lang]
        meta = r['readingTime'] if folder == 'insights' else r['statusShort']
        cards += f'''
      <a class="rel reveal" href="/{s}/{folder}/{sl}/">
        <div class="frame"><img src="/img/{PAGES[sl]['hero']}" alt="{r['heroAlt']}" loading="lazy"></div>
        <div class="kicker"><span class="cat">{r['category']}</span><span class="sep" aria-hidden="true"></span><span class="m">{meta}</span></div>
        <h3 class="serif">{r['title']}</h3>
        <p>{r['cardBlurb']}</p>
      </a>'''
    crumbs = (f'<nav class="crumbs" aria-label="{ui["breadcrumb"]}">'
              f'<a href="/{s}/">{ui["home"]}</a><span class="sep" aria-hidden="true">/</span>'
              f'<span aria-current="page">{m["crumb"]}</span></nav>')
    doc = f'''{chrome_head(lang, page, folder, folder + "/")}{nav(lang, folder + "/")}
<main id="main">
<section class="doc on-light" style="padding-top:clamp(96px,12vh,140px)">
  {crumbs}
  <h1 class="serif reveal">{m['title']}</h1>
  <p class="doc-standfirst reveal" style="--d:120ms">{m['stand']}</p>
</section>
<section class="related" style="background:var(--warm-white)">
  <div class="wrap">
    <div class="rel-grid" style="margin-top:0">{cards}
    </div>
  </div>
</section>
{closing_cta(lang)}</main>
{footer(lang)}'''
    out = os.path.join(ROOT, s, folder)
    os.makedirs(out, exist_ok=True)
    doc = assets.version(doc, VMAP)
    open(os.path.join(out, 'index.html'), 'w').write(doc)
    print(f'  /{s}/{folder}/  {len(doc)/1024:5.1f} KB')


for _f in ('insights', 'projects'):
    for _l in ('en', 'zh-tw'):
        build_index(_f, _l)
