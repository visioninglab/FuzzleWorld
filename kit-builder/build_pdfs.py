#!/usr/bin/env python3
"""Render every out/*.html to a home PDF (A4) and a print PDF (3mm bleed + crop marks + boxes)."""
import os, subprocess, pathlib, fitz

BASE = pathlib.Path(__file__).parent
OUT  = BASE / "out"
HOME = BASE / "pdf_home"
PRINT= BASE / "pdf_print"
HOME.mkdir(exist_ok=True); PRINT.mkdir(exist_ok=True)
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
MM = 2.834645669

def render_home(html, pdf):
    url = "file:///" + str(html).replace("\\","/").replace(" ","%20")
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-pdf-header-footer",
                    "--virtual-time-budget=3000", f"--print-to-pdf={pdf}", url],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def make_print(home_pdf, out_pdf):
    src = fitz.open(home_pdf)
    doc = fitz.open()
    W, H = 313*MM, 226*MM
    page = doc.new_page(width=W, height=H)
    bleed = fitz.Rect(5*MM,5*MM,308*MM,221*MM)     # 303x216, artwork bleeds to here
    trim  = fitz.Rect(8*MM,8*MM,305*MM,218*MM)      # 297x210 A4
    page.show_pdf_page(bleed, src, 0)               # underlay: fills 3mm bleed ring
    page.show_pdf_page(trim, src, 0)                # crisp 100% artwork at trim
    # crop marks (L at each trim corner, in the outer margin)
    L=3*MM
    marks=[((8*MM,0),(8*MM,L)),((0,8*MM),(L,8*MM)),
           ((305*MM,0),(305*MM,L)),((313*MM-L,8*MM),(313*MM,8*MM)),
           ((8*MM,226*MM-L),(8*MM,226*MM)),((0,218*MM),(L,218*MM)),
           ((305*MM,226*MM-L),(305*MM,226*MM)),((313*MM-L,218*MM),(313*MM,218*MM))]
    for a,b in marks:
        page.draw_line(fitz.Point(*a), fitz.Point(*b), color=(0,0,0), width=0.3)
    page.set_bleedbox(bleed); page.set_trimbox(trim)
    doc.save(out_pdf, garbage=3, deflate=True)
    doc.close(); src.close()

def main():
    htmls = sorted(OUT.glob("*.html"))
    for h in htmls:
        name = h.stem
        home = HOME/f"{name}.pdf"
        render_home(h, str(home))
        make_print(str(home), str(PRINT/f"{name}.pdf"))
        print("built", name)
    print(f"done: {len(htmls)} home + {len(htmls)} print")

if __name__ == "__main__":
    main()
