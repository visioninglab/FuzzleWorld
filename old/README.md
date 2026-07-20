# old/ — archived Style-A kit set (v1)

Archived **2026-07-13** to make way for a new set of 9 templates + instructions.
These are the previous **Style-A** rendered outputs and species photos — superseded,
kept here for reference / rollback. Nothing here is live.

```
old/
├── kit-builder/
│   ├── out/                 18 HTML sheets
│   ├── pdf_home/            18 A4 home PDFs
│   ├── pdf_print/           18 print PDFs (3 mm bleed + crop marks)
│   ├── pdf_combined/        9 combined home PDFs (instructions + cutting)
│   ├── pdf_combined_print/  9 combined print PDFs
│   └── assets/              9 species reference photos
└── canva-import/
    ├── pdf/                 18 Canva PDF-route sheets
    ├── vector-svg/          18 Canva SVG-route sheets
    └── GIW-felt-kits-editable-master.pdf   18-page combined (Canva "Import PDF")
```

## Kept live (NOT archived)

- **Generators / source of truth:** `kit-builder/species_data.py`, `gen.py`,
  `build_pdfs.py`, `fonts/`, `fonts_local.css`, and the **logos** in `kit-builder/assets/`.
- **`canva-import/refresh.py`** + `README.md`.
- **`kit-builder/shop_images/`** — the 9 cutting-sheet images still used by the live
  Shopify product. Archive these too only when the new set's shop images are ready.
- The live website (`../docs/`, `../website/`, and the separate `giant-insect-world-vision`
  site) and its hosted PDFs are untouched.

## Rebuilding the current-folder outputs from a new design

1. Update `kit-builder/species_data.py`, add new `assets/photo_<species>.jpg`.
2. `python kit-builder/gen.py && python kit-builder/build_pdfs.py`  → recreates `out/`, `pdf_home/`, `pdf_print/`.
3. `python canva-import/refresh.py`  → recreates `canva-import/pdf/`, `vector-svg/`, and the combined master PDF.
