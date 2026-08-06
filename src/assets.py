# -*- coding: utf-8 -*-
"""Content-hashed image URLs.

Images are cached for a week (see netlify.toml). Filenames stay stable —
`city-tempe.jpg` is still `city-tempe.jpg` after the photograph is replaced —
so a browser that already holds the old file will not re-request it and the
new photograph never appears. Appending a hash of the file's contents to the
URL fixes that: change the photo, the URL changes, the browser refetches.
Nothing else has to be remembered at deploy time.
"""
import hashlib
import os
import re

IMG_DIR = None


def _hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def build_map(img_dir):
    """name -> 8-char content hash, for every file in the image directory."""
    global IMG_DIR
    IMG_DIR = img_dir
    return {n: _hash(os.path.join(img_dir, n))
            for n in os.listdir(img_dir) if not n.startswith('.')}


def version(doc, vmap):
    """Append ?v=<hash> to every /img/... reference in a document."""
    def sub(m):
        prefix, name = m.group(1), m.group(2)
        h = vmap.get(name)
        return f'{prefix}/img/{name}?v={h}' if h else m.group(0)
    # src="/img/x.jpg" and content="https://domain/img/x.jpg" (Open Graph)
    doc = re.sub(r'(src=")/img/([^"?]+)', lambda m: sub(m), doc)
    doc = re.sub(r'(content="https://[^"]*?)/img/([^"?]+)', lambda m: sub(m), doc)
    return doc
