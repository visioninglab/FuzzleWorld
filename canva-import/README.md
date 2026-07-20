# canva-import — Style-A kit sheets for editing in Canva

Canva-ready exports of the 9 Style-A kits (instruction + cutting sheet each = 18 sheets),
sized **A4 landscape** so they scale perfectly for print. Edit in Canva, then export a
print PDF from Canva (it adds bleed + crop marks on export).

> These are **derived** from `../kit-builder/` (the source of truth). If the design
> changes there, run **`python refresh.py`** to rebuild this folder.

## Two routes — pick by what you're editing

| Folder | Canva action | Best for | Text |
|--------|--------------|----------|------|
| **`vector-svg/`** | Uploads → Upload files → drop the `.svg` (needs Canva **Pro**) | graphics, colours, shapes, layout | outlined (crisp, not re-typeable) |
| **`pdf/`** | Create a design → **Import PDF** (works on **Free**) | changing **wording** | Canva extracts it into **editable text boxes** |

Same design in both — use whichever fits the edit. For a sheet where you need both, import
the PDF (for text) and, if a shape needs finessing, grab it from the matching SVG.

## Steps

1. **Import** (see table). One file = one A4-landscape sheet.
2. **Edit.** Fonts are **Fredoka** (headings) + **Nunito** (body) — both in Canva's font
   list, so text matches.
3. **Export for the printer:** Share → Download → **PDF Print**, tick **Crop marks and
   bleed**, keep scale **100%**. Send that file to the printer.

## Files

```
canva-import/
├── vector-svg/   18 A4-landscape SVGs (graphics editing)
├── pdf/          18 A4-landscape PDFs (text editing via Canva PDF import)
├── refresh.py    regenerate both from ../kit-builder after design changes
└── README.md
```

## Note on "live-text" SVG

True editable-text **SVG** isn't produced here on purpose: headless-Chrome PDFs embed the
web-fonts as Type3, so a clean text-SVG can't be extracted mechanically — and hand-
rebuilding the layout as native SVG would fork from `kit-builder` (the authoritative
source). The **PDF-import route above gives editable text in Canva** without that risk.
If you specifically need native live-text SVGs, that's a separate build — just ask.
