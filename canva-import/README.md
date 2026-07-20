# canva-import — Style-A kit sheets for editing in Canva

SVG versions of the 9 Style-A kits (instruction + cutting sheet each = 18 files),
sized as **A4 landscape** vector so they scale perfectly for print. Import into Canva,
make your edits, then export a print PDF from Canva (Canva adds bleed + crop marks on
export — choose **PDF Print** with crop marks & bleed).

## Two versions

- **`vector-svg/`** — the exact layouts as vector. Every shape, colour, photo and element
  is editable; **text is outlined** (crisp, print-perfect, but not re-typeable). Use this
  for graphics / colour / layout tweaks. **Ready now.**
- **`editable-svg/`** — the same sheets rebuilt with **live, editable text** (Fredoka +
  Nunito, both available in Canva) so you can retype wording too. _(being added)_

Pick whichever suits the edit; they're the same design.

## Import into Canva

1. Canva → **Create a design** → A4 (or any) → **Uploads → Upload files** → drop the `.svg`.
   (SVG upload needs Canva Pro. If you're on Free, use the PDFs in
   `../kit-builder/pdf_home/` via **Create a design → Import PDF** instead.)
2. Drag the uploaded SVG onto the page; resize to fill.
3. Edit. In `vector-svg/` the shapes/photos/colours are all selectable elements.
4. **Export:** Share → Download → **PDF Print**, tick **Crop marks and bleed** → send that
   file to the printer. Keep the scale at 100%.

## Fonts

Headings **Fredoka**, body **Nunito** — both are in Canva's font list, so the live-text
version (`editable-svg/`) matches without extra setup.

## Source

These are generated from `../kit-builder/` (see its README). To change the design itself
(not just a one-off Canva tweak), edit `kit-builder/species_data.py` and regenerate.
