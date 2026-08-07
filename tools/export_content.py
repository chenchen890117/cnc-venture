# -*- coding: utf-8 -*-
"""One-time migration: turn the Python content modules into the /content tree.

After this runs, /content is the source of truth and scripts/build-content.js is
the renderer. This file exists so the migration is reproducible and auditable —
it is not part of the normal build.

Run:  python3 tools/export_content.py
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

from content_pages import PAGES, UI  # noqa: E402

OUT = os.path.join(ROOT, 'content')
LANGS = ('en', 'zh-tw')

# ── taxonomy ────────────────────────────────────────────────────────────────
# Three article categories, extensible: add an entry here and the build picks
# up the listing page, the category nav and the sitemap automatically.
CATEGORIES = [
    {'slug': 'news',    'en': 'News & Events',
     'zh-tw': '最新活動消息',
     'blurb_en': 'What we are doing, where we are going, and who is coming with us.',
     'blurb_zh': '我們正在做的事、要去的地方，以及一起同行的人。'},
    {'slug': 'stories', 'en': 'Expansion Stories',
     'zh-tw': '創業案例分享',
     'blurb_en': 'Companies in the middle of the work — reported as they stand.',
     'blurb_zh': '正在路上的公司——如實記錄，不加修飾。'},
    {'slug': 'market',  'en': 'Local Market Insights',
     'zh-tw': '在地知識分享',
     'blurb_en': 'Market overviews, city guides and the practical detail behind each decision.',
     'blurb_zh': '市場觀察、城市指南，以及每個決定背後的實務細節。'},
]

# Which category each existing page belongs to.
CATEGORY_OF = {
    'arizona-gateway-for-taiwanese-companies': 'market',
    'phoenix-metro-market-guide': 'market',
    'first-steps-before-us-expansion': 'market',
    'opening-a-restaurant-in-arizona': 'market',
    'taiwanese-restaurant-group-exploring-phoenix': 'stories',
    'taiwan-startup-delegation-arizona': 'stories',
    'taiwanese-consumer-brand-us-market-entry': 'stories',
}

# Display order inside a listing (lower first). Kept explicit so the editorial
# running order does not depend on dict insertion or on filesystem order.
ORDER = {s: i for i, s in enumerate(PAGES)}


def inline(t):
    """HTML in the source becomes Markdown so an author never meets a tag."""
    t = re.sub(r'<strong>(.*?)</strong>', r'**\1**', t, flags=re.S)
    t = re.sub(r'<em>(.*?)</em>', r'*\1*', t, flags=re.S)
    t = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', t, flags=re.S)
    return t.strip()


def to_markdown(blocks):
    out = []
    for kind, *rest in blocks:
        if kind == 'h2':
            out.append(f'## {inline(rest[0])}')
        elif kind == 'h3':
            out.append(f'### {inline(rest[0])}')
        elif kind == 'p':
            out.append(inline(rest[0]))
        elif kind == 'ul':
            out.append('\n'.join(f'- {inline(i)}' for i in rest[0]))
        elif kind == 'ol':
            out.append('\n'.join(f'{n}. {inline(i)}' for n, i in enumerate(rest[0], 1)))
        elif kind == 'pull':
            body = '\n'.join(f'> {l}' for l in inline(rest[0]).split('\n'))
            if len(rest) > 1 and rest[1]:
                body += f'\n> — {inline(rest[1])}'
            out.append(body)
        elif kind == 'panel':
            label, title, items = rest[0], rest[1], rest[2]
            lines = [':::callout', f'Label: {inline(label)}', f'Title: {inline(title)}']
            lines += [f'- {inline(i)}' for i in items]
            if len(rest) > 3 and rest[3]:
                lines.append(f'Note: {inline(rest[3])}')
            lines.append(':::')
            out.append('\n'.join(lines))
        elif kind == 'fig':
            lines = [f':::image {rest[0]}', f'Alt: {inline(rest[1])}']
            if len(rest) > 2 and rest[2]:
                lines.append(f'Caption: {inline(rest[2])}')
            lines.append('Size: standard')
            lines.append(':::')
            out.append('\n'.join(lines))
        elif kind == 'advisory':
            out.append(':::advisory\n' + inline(rest[0]) + '\n:::')
        else:
            raise ValueError(kind)
    return '\n\n'.join(out) + '\n'


FM_ORDER = ['title', 'standfirst', 'description', 'cardBlurb', 'crumb',
            'heroAlt', 'heroCaption', 'readingTime', 'dateLabel',
            'status', 'statusShort', 'industry']


def frontmatter(rec, is_project):
    lines = ['---']
    src = {
        'title': rec.get('title'), 'standfirst': rec.get('standfirst'),
        'description': rec.get('desc'), 'cardBlurb': rec.get('cardBlurb'),
        'crumb': rec.get('crumb'), 'heroAlt': rec.get('heroAlt'),
        'heroCaption': rec.get('heroCaption'), 'readingTime': rec.get('readingTime'),
        'dateLabel': rec.get('dateLabel'), 'status': rec.get('status'),
        'statusShort': rec.get('statusShort'), 'industry': rec.get('industry'),
    }
    for k in FM_ORDER:
        v = src.get(k)
        if v:
            lines.append(f'{k}: {inline(v)}')
    if is_project and rec.get('facts'):
        lines.append('facts:')
        for k, v in rec['facts']:
            lines.append(f'  {k} | {v}')
    lines.append('---')
    return '\n'.join(lines) + '\n\n'


def run():
    # This was a one-time migration. /content is the source of truth now — a
    # second run would overwrite hand-edited Markdown and _config.json with
    # whatever is still frozen in content_pages.py.
    if os.path.isdir(OUT) and '--force' not in sys.argv:
        raise SystemExit('/content already exists. This is a one-time migration; '
                         'pass --force only if you mean to discard it.')
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    for slug, page in PAGES.items():
        cat = CATEGORY_OF[slug]
        d = os.path.join(OUT, cat, slug)
        os.makedirs(os.path.join(d, 'images'), exist_ok=True)
        is_project = page['type'] == 'project'
        en = page['en']
        meta = {
            'type': page['type'],
            'category': cat,
            'hero': page['hero'],
            'published': en.get('published', '2026-08-06'),
            'updated': en.get('updated', en.get('published', '2026-08-06')),
            'order': ORDER[slug],
            'related': page.get('related', []),
        }
        with open(os.path.join(d, 'meta.json'), 'w') as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
            f.write('\n')
        for lang in LANGS:
            rec = page[lang]
            doc = frontmatter(rec, is_project) + to_markdown(rec['body'])
            with open(os.path.join(d, f'{lang}.md'), 'w') as f:
                f.write(doc)
        # Keep the images folder in git even when a piece has no local images.
        open(os.path.join(d, 'images', '.gitkeep'), 'w').close()
        print(f'  content/{cat}/{slug}/  '
              f'{os.path.getsize(os.path.join(d, "en.md"))/1024:5.1f} KB en  '
              f'{os.path.getsize(os.path.join(d, "zh-tw.md"))/1024:5.1f} KB zh')

    cfg = {
        'domain': 'https://cncventure.org',
        'cta': 'https://www.surveycake.com/s/3qKZN',
        'languages': list(LANGS),
        'categories': CATEGORIES,
        'ui': {l: {k: v for k, v in UI[l].items()} for l in LANGS},
    }
    with open(os.path.join(OUT, '_config.json'), 'w') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'\n{len(PAGES)} pieces exported + content/_config.json')


if __name__ == '__main__':
    run()
