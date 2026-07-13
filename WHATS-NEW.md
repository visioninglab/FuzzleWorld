# What's new — handoff notes

_Last updated: 2026-07-13. The **`kit-builder/`** folder is the most current work._

## TL;DR for the other computer

Run `git pull`. Then read [`kit-builder/README.md`](kit-builder/README.md).
`kit-builder/` is a **new Style-A design direction** for the kits and is the latest,
authoritative version of that work. It is **additive** — it does not change the existing
`templates/`, `svgs/`, `editable-pdfs/`, `docs/`, or `website/`.

## What was added

A self-contained generator that produces the **Style-A** kit design: a colour-panel
layout split into **two A4-landscape sheets per species** (an instruction sheet + a
cutting sheet with felt pieces at true actual size). Everything is editable HTML + inline
SVG, rendered to PDF via headless Chrome + PyMuPDF.

```
kit-builder/
├── README.md          full docs — design decisions + how to regenerate
├── gen.py             species_data.py -> out/*.html
├── species_data.py    ALL per-species content + felt-piece SVG shapes (edit here)
├── build_pdfs.py      out/*.html -> pdf_home/ + pdf_print/
├── fonts_local.css, fonts/    Fredoka + Nunito, embedded
├── assets/            logos + 9 species photos
├── out/               18 editable HTML sheets
├── pdf_home/          18 A4 home PDFs (print at 100%)
└── pdf_print/         18 commercial PDFs (3 mm bleed, crop marks, TrimBox/BleedBox)
```

## Status

**Done (9 species):** ladybird, ant, woodlouse, river skater, bell spider, grasshopper,
earthworm, dragonfly, butterfly — each with an instruction sheet + a cutting sheet, in
both the home and print PDF sets.

**Not yet in this style (9 remaining):** painted-lady, manchester-bee, peppered-moth,
longhorn-beetle, keeled-skimmer, highland-midge, maybug, burying-beetle, glow-worm.
Add each by appending an entry to `kit-builder/species_data.py`, then rerun
`python gen.py && python build_pdfs.py`.

## How this differs from the existing `templates/`

The existing `templates/<theme>/<species>/` kits are the older **single-sheet** "6×2
booklet" design (fonts: Nunito + Source Serif 4). Style-A is a **two-sheet** redesign
(fonts: Fredoka + Nunito) with corrected content and cleaner cutting shapes. Nothing has
been merged/replaced — that's a design decision left open for you.

## Fixes baked into Style-A

- Ladybird piece count corrected **15 → 17**; cover "Ladybug" → "Ladybird".
- Old text glitches (`le�`, `o�en`, `butterfl es`, overlapping "Did you know?" titles) are
  gone — every sheet is regenerated from clean text.
- Logos had opaque black boxes keyed out to transparent.
- Every leg / antenna is an **individual cuttable piece** (not radiating from one point);
  grasshopper finished illustration redrawn as a **top-down** view.

## Requirements to regenerate

Windows + Google Chrome + Python 3 with `pip install pymupdf`. If Chrome is installed
elsewhere, edit the `CHROME` path near the top of `kit-builder/build_pdfs.py`.
