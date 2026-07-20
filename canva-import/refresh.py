#!/usr/bin/env python3
"""Regenerate the Canva-import files from the authoritative kit-builder output.

Run this after the design changes in ../kit-builder (e.g. someone edits
species_data.py and reruns gen.py + build_pdfs.py). It:
  1. copies kit-builder/pdf_home/*.pdf  -> canva-import/pdf/        (PDF-import route)
  2. converts each of those PDFs        -> canva-import/vector-svg/  (SVG-upload route)
  3. bundles every sheet               -> GIW-felt-kits-editable-master.pdf
                                          (one multi-page PDF: Canva "Import PDF" once)

kit-builder is the single source of truth; this folder is just the two
Canva-friendly export formats derived from it. Requires: pip install pymupdf
"""
import pathlib, shutil, glob
import fitz  # PyMuPDF

HERE = pathlib.Path(__file__).resolve().parent
SRC  = HERE.parent / "kit-builder" / "pdf_home"
PDF  = HERE / "pdf"
SVG  = HERE / "vector-svg"
PDF.mkdir(exist_ok=True); SVG.mkdir(exist_ok=True)

pdfs = sorted(glob.glob(str(SRC / "*.pdf")))
if not pdfs:
    raise SystemExit(f"No PDFs in {SRC} — run kit-builder/build_pdfs.py first.")

for p in pdfs:
    name = pathlib.Path(p).stem
    shutil.copy2(p, PDF / f"{name}.pdf")                       # PDF route
    svg = fitz.open(p)[0].get_svg_image(text_as_path=True)     # SVG route (text outlined)
    (SVG / f"{name}.svg").write_text(svg, encoding="utf-8")
    print("ok", name)

# 3. bundle every sheet into one multi-page PDF for Canva's "Import PDF" route
ORDER = ["butterfly", "ladybird", "grasshopper", "riverskater", "dragonfly",
         "bellspider", "woodlouse", "earthworm", "ant"]
present = sorted({pathlib.Path(p).stem.rsplit("_", 1)[0] for p in pdfs})
species = [s for s in ORDER if s in present] + [s for s in present if s not in ORDER]
merged = fitz.open()
n = 0
for sp in species:
    for suffix in ("instructions", "cutting"):
        f = PDF / f"{sp}_{suffix}.pdf"
        if f.exists():
            merged.insert_pdf(fitz.open(str(f))); n += 1
combined = HERE / "GIW-felt-kits-editable-master.pdf"
merged.save(str(combined)); merged.close()

print(f"\nDone: {len(pdfs)} sheets -> pdf/ + vector-svg/  |  {n}-page combined -> {combined.name}")
