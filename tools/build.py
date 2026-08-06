"""Generate /en/index.html and /zh-tw/index.html from the approved page.

Both language versions share one stylesheet, one script and one image set.
This script exists so the two documents stay structurally identical: the
Chinese page is produced by substituting copy into the English DOM, never by
re-authoring the markup. If you change structure, change it once here.

Run:  python3 tools/build.py
"""
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = 'https://cncventure.com'

BODY = open(os.path.join(ROOT, 'src', '_body.html')).read()

# ── shared <head> ────────────────────────────────────────────────────────────
HEAD = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{title}</title>
<meta name="description" content="{desc}">

<link rel="canonical" href="{domain}/{slug}/">
<link rel="alternate" hreflang="en" href="{domain}/en/">
<link rel="alternate" hreflang="zh-Hant-TW" href="{domain}/zh-tw/">
<link rel="alternate" hreflang="x-default" href="{domain}/en/">

<meta name="theme-color" content="#02383D">

<meta property="og:type" content="website">
<meta property="og:site_name" content="CnC Venture">
<meta property="og:locale" content="{oglocale}">
<meta property="og:locale:alternate" content="{ogalt}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{domain}/{slug}/">
<meta property="og:image" content="{domain}/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{ogalttext}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{twdesc}">
<meta name="twitter:image" content="{domain}/img/og-image.jpg">

<!-- PLACEHOLDER FAVICON: replace with the final CnC Venture mark. -->
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%2302383D'/%3E%3Ctext x='32' y='43' font-family='Georgia,serif' font-size='30' fill='%23FBF8F3' text-anchor='middle'%3EC%3C/text%3E%3C/svg%3E">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">

<link rel="stylesheet" href="../css/style.css">
</head>
'''

FONTS_EN = ('https://fonts.googleapis.com/css2?'
            'family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..600'
            '&family=Inter:wght@300;400;500;600&display=swap')
# The Chinese page additionally loads Noto Serif TC / Noto Sans TC. These are
# large; they are deliberately NOT loaded on the English page.
FONTS_ZH = (FONTS_EN.replace('&display=swap', '')
            + '&family=Noto+Sans+TC:wght@300;400;500'
            + '&family=Noto+Serif+TC:wght@300;400;500;600&display=swap')

META = {
    'en': dict(
        lang='en', slug='en', oglocale='en_US', ogalt='zh_TW', fonts=FONTS_EN,
        title='CnC Venture | U.S. Business Expansion Platform',
        desc='CnC Venture helps companies explore, establish, and grow in the United '
             'States through market strategy, local resources, company setup, site '
             'selection, brand localization, and execution support.',
        twdesc='Helping ambitious companies launch, build, and grow in the United States.',
        ogalttext='Greater Phoenix at dusk',
    ),
    'zh-tw': dict(
        lang='zh-Hant-TW', slug='zh-tw', oglocale='zh_TW', ogalt='en_US', fonts=FONTS_ZH,
        title='CnC Venture｜企業美國市場拓展平台',
        desc='CnC Venture 協助企業探索、設立並在美國市場成長——從市場策略、在地資源、'
             '公司設立、選址、品牌在地化到落地執行，陪伴台灣企業建立下一個成長據點。',
        twdesc='從市場探索、公司設立到品牌落地，陪伴企業在美國建立下一個成長據點。',
        ogalttext='黃昏時分的大鳳凰城',
    ),
}


def localise_paths(doc, slug):
    """Point assets at the shared folders and prefix in-site links with /<slug>."""
    doc = doc.replace('src="img/', 'src="../img/')
    # Language-independent absolute links (/en/, /zh-tw/) are left alone.
    def prefix(m):
        path = m.group(1)
        if path.startswith(('en/', 'zh-tw/')):
            return m.group(0)
        return f'href="/{slug}/{path}"'
    doc = re.sub(r'href="/([^"#]*)"', prefix, doc)
    return doc


def set_language_switch(doc, slug):
    """Mark the active language and point the other one at its own tree."""
    doc = doc.replace('<a href="/en/" aria-current="true" lang="en">',
                      '<a href="/en/" lang="en">')
    if slug == 'zh-tw':
        doc = doc.replace('<a href="/zh-tw/" lang="zh-Hant">',
                          '<a href="/zh-tw/" aria-current="true" lang="zh-Hant">')
    else:
        doc = doc.replace('<a href="/en/" lang="en">',
                          '<a href="/en/" aria-current="true" lang="en">')
    return doc


def build(slug):
    meta = META[slug]
    doc = BODY
    if slug == 'zh-tw':
        from content_zh import REPLACEMENTS, ALT_TEXT
        for src, dst in REPLACEMENTS:
            if src not in doc:
                raise SystemExit(f'MISSING SOURCE STRING: {src[:70]!r}')
            doc = doc.replace(src, dst)
        for en, zh in ALT_TEXT.items():
            doc = doc.replace(f'alt="{en}"', f'alt="{zh}"')
    doc = localise_paths(doc, slug)
    doc = set_language_switch(doc, slug)
    page = HEAD.format(domain=DOMAIN, **meta) + doc.rstrip() + \
        '\n<script src="../js/main.js" defer></script>\n</body>\n</html>\n'
    out = os.path.join(ROOT, slug, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(page)
    print(f'{slug:6s} -> {out}  {len(page)/1024:.1f} KB')


if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.join(ROOT, 'src'))
    build('en')
    build('zh-tw')
