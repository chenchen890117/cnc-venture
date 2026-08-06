# CnC Venture

**Expand Beyond Borders.** Marketing site for CnC Venture — a business expansion
platform helping ambitious companies launch, build, and grow in the United States.

Live: https://cnc-venture.netlify.app

---

## Repository layout

```
public/          Published to the web. Nothing else is.
  index.html     The homepage — single file, all CSS and JS inline.
  img/           21 images. Currently generated placeholders.
docs/
  wix-build-spec.html   Design system + section-by-section spec.
tools/
  generate-placeholder-images.py   Regenerates public/img/. Needs Pillow.
netlify.toml     Publish directory and headers. No build step.
```

## Editing

Everything visual lives in `public/index.html`. There is no build, no bundler,
no dependencies — open it in a browser and it works.

**Colours** are defined once, in the `:root` block at the top of the file:

```css
--ink:        #02383D   /* primary */
--warm-white: #FBF8F3
--sand:       #E8DCC8
--sunset:     #D9773F
```

Change one there and it changes everywhere. Do not hardcode a hex anywhere else.

**Type scale** is fixed in the `.d-xl` / `.d-l` / `.d-m` / `.d-s` classes. The
design depends on the gap between body (17px) and headline (78px); adding an
intermediate size will flatten the hierarchy. See `docs/wix-build-spec.html`
section B.

**Spacing** — `--sec-y` controls the vertical rhythm of every section. It is
deliberately large. When something feels unfinished, increase spacing before
adding an element.

## Replacing the placeholder images

Every image is a plain `<img>` with a `src` pointing at `public/img/`. To swap
one in, drop the new file in and update the `src` — or keep the filename and
just replace the file.

Ratios to match are listed in `docs/wix-build-spec.html` section F, along with
a shot brief for each slot.

## Deploying

Connected to Netlify. Any push to the default branch deploys automatically.
Pull requests get a Deploy Preview URL.

## Content still to replace

- The three Expansion Stories are structural placeholders, not real clients.
- All images are generated placeholders.
- Every CTA links to `#book`; there is no booking system wired up yet.
