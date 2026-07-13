# kit-builder — Style-A felt-kit sheets (generator)

A self-contained toolchain that generates the **Style-A** version of the FuzzleWorld
kits: a colour-panel design split into **two A4-landscape sheets per species** —

- an **instruction sheet** (6 pastel panels: Make your own / How to build it / Did you
  know? / The pieces / Finished! / cover + FuzzleWorld back), and
- a **cutting sheet** (Body / pieces panels + a "Finished!" preview on the themed mat,
  with all felt pieces drawn at true **actual size**, 1 SVG unit = 1 mm).

This is a **newer design direction** and is intentionally kept separate from the
existing `../templates/` kits (which are the older single-sheet "6×2 booklet" design).
Nothing here overwrites those — this folder is additive.

Everything is plain **HTML + inline SVG** so it stays fully editable, and it renders to
PDF via headless Chrome + PyMuPDF.

## Status — 9 of the 18 species done

Built and reviewed: **ladybird, ant, woodlouse, river skater, bell spider, grasshopper,
earthworm, dragonfly, butterfly.**

Still to do in this style (already in the collection elsewhere): painted-lady,
manchester-bee, peppered-moth, longhorn-beetle, keeled-skimmer, highland-midge, maybug,
burying-beetle, glow-worm. Add each by appending an entry to `species_data.py`.

## Folder contents

```
kit-builder/
├── gen.py            # builds out/*.html from species_data.py + the template
├── species_data.py   # ALL per-species content + felt-piece SVG shapes (edit this)
├── build_pdfs.py     # renders out/*.html -> pdf_home/ and pdf_print/
├── fonts_local.css   # @font-face for Fredoka + Nunito (points at fonts/)
├── fonts/            # Fredoka + Nunito woff2 subsets (OFL, safe to redistribute)
├── assets/           # logo_giantinsectworld.png, logo_fuzzleworld.png, photo_<species>.jpg
├── out/              # 18 generated HTML sheets (<species>_instructions.html / _cutting.html)
├── pdf_home/         # 18 home PDFs — plain A4 landscape (print at 100%)
└── pdf_print/        # 18 commercial PDFs — 3 mm bleed, crop marks, TrimBox/BleedBox
```

## Regenerate

Requirements: Windows + Google Chrome, Python 3 with `pip install pymupdf`.
(If Chrome is installed elsewhere, edit the `CHROME` path at the top of `build_pdfs.py`.)

```bash
python gen.py          # species_data.py -> out/*.html
python build_pdfs.py   # out/*.html -> pdf_home/ + pdf_print/
```

Edit content or shapes in `species_data.py`, then rerun both. To edit one sheet directly,
edit its file in `out/` (it references `../fonts_local.css` and `../assets/…`).

## Design decisions baked in

- **Palette** (sampled from the original Style-A sheets): panels pink `#ffe0e0`,
  blue `#e0f0ff`, yellow `#fff5cc`, green `#e8ffe0`; headings red `#e63946`,
  blue `#2a6fdb`, purple `#7b2ff7`, green `#3fae4a`.
- **Fonts**: Fredoka (headings) + Nunito (body), embedded locally so Chrome subsets them
  into the PDFs — no network needed at build time.
- **Themes** drive the cover-tab colour and the "Finished!" mat colour:
  meadow = green, aquatic = blue, underground = brown.
- **Sizing**: "as big as possible" — each insect is locked to **one consistent scale**
  (so the pieces still assemble correctly) and that scale is pushed until the largest
  piece nearly fills its panel. Shapes are mm-accurate (1 unit = 1 mm) → true actual size.
- **Print geometry** (`pdf_print/`): MediaBox 313×226 mm, BleedBox 303×216 mm,
  TrimBox 297×210 mm (A4). Colour panels bleed to the trim; crop marks at the four
  corners. Home set is plain A4 (297×210).
- **Cutting rule**: every leg / antenna is an **individual cuttable piece** (never
  radiating from a shared point). Helpers `sep_legs()` / `bent_antenna()` in
  `species_data.py` enforce this.

## Fixes applied vs the earlier drafts

- Ladybird piece count corrected **15 → 17**; cover wording "Ladybug" → "Ladybird".
- The Style-B text glitches (`le�`, `o�en`, `butterfl es`, overlapping "Did you know?"
  titles) are gone because every sheet is regenerated from clean text.
- The two logos had opaque black boxes keyed out to transparent (`assets/logo_*.png`).
- Round-2 review fixes: separated the spider/skater/woodlouse legs and ant/woodlouse/
  skater antennae into individual pieces; grasshopper redrawn with a **top-down** finished
  illustration.

## Credits

Reference photos are the same iNaturalist CC0 / CC-BY images used elsewhere in the repo;
each sheet prints the species Latin name, photographer + licence, and logo credit.
Logos © Giant Insect World.
