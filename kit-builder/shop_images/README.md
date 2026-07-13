# shop_images — Shopify variant images (Style-A cutting sheets)

High-res JPG renders of the **cutting sheets** (`../out/<slug>_cutting.html`), used as the
per-variant product images on the Shopify **"Make-Your-Own Felt Minibeast Kit"** product
(`shop.giantinsectworld.com`, variant = "Choose your British bug").

- 2246×1588 px, rendered from the HTML via headless Chrome (`--force-device-scale-factor=2
  --window-size=1123,794`, the sheet's exact 297×210 mm), then flattened to JPG. No
  Ghostscript needed (can't rasterise the PDFs without it).
- **9 of 18 species** so far (the Style-A set). The other 9 shop variants still use the
  older single-sheet previews in `../../docs/images/previews/` until they're built in
  Style-A. As each new species is added, render its cutting sheet the same way and swap the
  matching variant image.

## slug → shop variant name
ladybird → 7-spot Ladybird · ant → Garden Ant · woodlouse → Woodlouse ·
riverskater → River Skater · bellspider → Diving Bell Spider ·
grasshopper → Meadow Grasshopper · earthworm → Earthworm ·
dragonfly → Common Darter Dragonfly · butterfly → Small Tortoiseshell Butterfly

## Regenerate one
```
# after editing species_data.py + gen.py:
chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1123,794 --screenshot=shop_images/<slug>_cutting.png out/<slug>_cutting.html
magick shop_images/<slug>_cutting.png -background white -flatten -quality 90 shop_images/<slug>_cutting.jpg
```
