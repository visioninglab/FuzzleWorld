#!/usr/bin/env python3
"""FuzzleWorld sheet generator.
Reads species definitions from species_data.py and emits, per species:
  out/<key>_instructions.html   (6-panel Style-A instruction sheet)
  out/<key>_cutting.html        (4-panel Style-A cutting template)
All content is plain HTML + inline SVG so the output stays editable.
"""
import os, pathlib
from species_data import SPECIES

OUT = pathlib.Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- shared CSS
CSS = """
@page { size:297mm 210mm; margin:0; }
html,body{width:297mm; height:210mm; overflow:hidden;}
:root{
  --pink:#ffe0e0; --blue:#e0f0ff; --yellow:#fff5cc; --green:#e8ffe0;
  --red:#e63946; --hblue:#2a6fdb; --purple:#7b2ff7; --hgreen:#3fae4a; --amber:#e8930c;
  --ink:#3a3a3a; --muted:#5a5a5a;
  --b1:#e63946; --b2:#2a6fdb; --b3:#3fae4a; --b4:#e94b9c; --b5:#f4a400; --b6:#7b2ff7;
}
*{box-sizing:border-box; margin:0; padding:0;}
html,body{background:#fff;}
.sheet{width:297mm; height:210mm; background:#fff; position:relative; overflow:hidden;
  font-family:'Nunito',sans-serif; color:var(--ink); -webkit-font-smoothing:antialiased;}
.grid6{display:grid; grid-template-columns:1fr 1fr 1fr; grid-template-rows:1fr 1fr; gap:1.4mm;}
.grid4{display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:1.4mm;}
.panel{padding:6.5mm 7mm; position:relative; overflow:hidden;}
.p-pink{background:var(--pink);} .p-blue{background:var(--blue);}
.p-yellow{background:var(--yellow);} .p-green{background:var(--green);}
h2{font-family:'Fredoka',sans-serif; font-weight:600; font-size:20pt; line-height:1.05; letter-spacing:.2px;}
.h-red{color:var(--red);} .h-blue{color:var(--hblue);} .h-purple{color:var(--purple);}
.h-green{color:var(--hgreen);} .h-amber{color:var(--amber);}
.star{position:absolute; top:6mm; right:7mm; font-size:15pt;}
p,li{font-size:10.5pt; line-height:1.34;}
.sub{font-weight:700; font-size:11pt; margin-top:1mm;}
.muted{color:var(--muted);}
.spacer{height:2.4mm;} .small{height:1.6mm;}
/* instruction panel 1 */
.photo{position:absolute; top:6mm; right:6.5mm; width:33mm; height:24mm; object-fit:cover;
  border-radius:2mm; box-shadow:0 0 0 1px rgba(0,0,0,.06);}
.title{font-family:'Fredoka',sans-serif; font-weight:600; font-size:14pt; line-height:1.12; color:#2f2f2f; margin-top:15mm;}
.need{list-style:none;} .need li{position:relative; padding-left:5mm;}
.need li:before{content:"•"; position:absolute; left:1mm; color:var(--red); font-weight:700;}
/* steps */
.steps{list-style:none; display:flex; flex-direction:column; gap:2.9mm; margin-top:1mm;}
.steps li{display:flex; gap:3mm; align-items:flex-start;}
.num{flex:0 0 auto; width:7.5mm; height:7.5mm; border-radius:50%; color:#fff;
  font-family:'Fredoka',sans-serif; font-weight:600; font-size:11pt;
  display:flex; align-items:center; justify-content:center; margin-top:.2mm;}
.steps li:nth-child(1) .num{background:var(--b1);} .steps li:nth-child(2) .num{background:var(--b2);}
.steps li:nth-child(3) .num{background:var(--b3);} .steps li:nth-child(4) .num{background:var(--b4);}
.steps li:nth-child(5) .num{background:var(--b5);} .steps li:nth-child(6) .num{background:var(--b6);}
.steps .txt{font-weight:600; font-size:10.5pt; padding-top:.6mm;}
/* facts */
.facts{list-style:none; display:flex; flex-direction:column; gap:2.6mm; margin-top:1mm;}
.facts li{font-weight:600;}
/* pieces */
.swatches{display:inline-flex; gap:2mm; vertical-align:middle; margin-left:3mm;}
.sw{width:5mm; height:5mm; border-radius:1.2mm; border:1px solid rgba(0,0,0,.25);}
.piecelist{margin-top:1mm;} .piecelist div{font-size:10.5pt; line-height:1.42;}
.piecelist b{font-weight:800;}
.total{font-weight:800; margin-top:2mm;}
.finlist p{margin-bottom:2.2mm; font-weight:600;}
/* panel 6 */
.p6{display:flex; gap:0; padding:0; background:var(--yellow);}
.cover-col{flex:1 1 52%; display:flex; flex-direction:column; align-items:center;
  padding:5mm 4mm; text-align:center; background:var(--yellow);}
.cover-card{background:#fff; border-radius:3mm; width:100%; padding:0 0 4mm; overflow:hidden;
  box-shadow:0 1px 4px rgba(0,0,0,.12);}
.cover-tab{height:4mm;}
.cover-card img{width:74%; margin:3mm auto 1mm; display:block;}
.cover-mk{font-weight:800; font-size:10.5pt; margin-top:1mm;}
.cover-sp{font-size:10pt; color:var(--muted);}
.cover-foot{font-weight:700; font-size:9.5pt; line-height:1.35; margin-top:3.5mm; color:#4a4a4a;}
.fuzzle-col{flex:1 1 48%; background:var(--pink); padding:4.5mm 4mm; text-align:center;
  display:flex; flex-direction:column; align-items:center;}
.fuzzle-col img{width:82%; margin-bottom:.5mm;}
.fuzzle-tag{font-style:italic; font-size:9.5pt; color:var(--muted);}
.fuzzle-col .themes{font-weight:800; font-size:9.5pt; margin-top:2.5mm; line-height:1.4;}
.fuzzle-col .setlist{font-weight:700; font-size:9pt; margin-top:2.5mm; line-height:1.45; color:#444;}
.credit{font-size:8pt; color:#7a6b6b; margin-top:3mm; line-height:1.4;}
/* cutting */
.cpanel{padding:7mm 8mm 12mm; display:flex; flex-direction:column;}
.art{flex:1 1 auto; display:flex; align-items:center; justify-content:center; min-height:0;}
.cap{font-size:10.5pt; line-height:1.35;} .cap b{font-weight:800;}
.footer{position:absolute; left:0; right:0; bottom:2mm; text-align:center;
  font-family:'Fredoka',sans-serif; font-weight:600; font-size:12.5pt; color:var(--red);}
svg{display:block; overflow:visible;}
.fcard{border-radius:5mm; padding:5mm 6mm; display:flex; align-items:center; gap:5mm;}
.fcard .txt{font-size:11pt; font-weight:600; line-height:1.4;}
"""

def head(extra=""):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<link rel="stylesheet" href="../fonts_local.css"><style>{CSS}{extra}</style>'
            f'</head><body>')

TAB = {"meadow":"#3fae4a", "aquatic":"#2a6fdb", "underground":"#8a5a2b"}
MAT = {"meadow":"#8bb74e", "aquatic":"#8fc0e0", "underground":"#b07a44"}
MAT_TXT = {"meadow":"#22331a", "aquatic":"#12303f", "underground":"#3a2410"}

def instructions(s):
    needs = "".join(f"<li>{x}</li>" for x in s["needs"])
    steps = "".join(f'<li><span class="num">{i+1}</span><span class="txt">{t}</span></li>'
                    for i,t in enumerate(s["steps"]))
    facts = "".join(f"<li>{x}</li>" for x in s["facts"])
    sw = "".join(f'<span class="sw" style="background:{c}"></span>' for c in s["swatches"])
    pieces = "".join(f"<div><b>{b}</b> {d}</div>" for b,d in s["pieces"])
    note = f'<p class="muted">{s["pieces_note"]}</p>' if s.get("pieces_note") else ""
    fin = "".join(f"<p>{x}</p>" for x in s["finished_lines"])
    tab = TAB[s["theme"]]
    return head() + f"""
<div class="sheet grid6">
  <section class="panel p-pink">
    <h2 class="h-red">Make your own!</h2>
    <img class="photo" src="../assets/{s['photo']}" alt="{s['cover_name']}">
    <div class="title">{s['name']}<br>Felt Puzzle</div>
    <div class="spacer"></div>
    <p class="muted">A Giant Insect World puzzle<br>build it &middot; take it apart &middot; build it again</p>
    <div class="spacer"></div>
    <p class="sub">You will need:</p>
    <ul class="need">{needs}</ul>
  </section>
  <section class="panel p-blue">
    <h2 class="h-blue">How to build it</h2>
    <ol class="steps">{steps}</ol>
  </section>
  <section class="panel p-yellow">
    <span class="star">&#11088;</span>
    <h2 class="h-purple">Did you know?</h2>
    <ul class="facts">{facts}</ul>
  </section>
  <section class="panel p-green">
    <span class="star">&#11088;</span>
    <h2 class="h-red">The pieces</h2>
    <p class="sub">Find these colours in felt or paper <span class="swatches">{sw}</span></p>
    <p class="muted">{s['find_colours']}</p>
    <div class="small"></div>
    <p class="sub">Using the template, cut out:</p>
    <div class="piecelist">{pieces}</div>
    <p class="total">{s['total_text']}</p>
    {note}
  </section>
  <section class="panel p-yellow">
    <span class="star">&#11088;</span>
    <h2 class="h-green">Finished!</h2>
    <div class="finlist">{fin}</div>
  </section>
  <section class="panel p6">
    <div class="cover-col">
      <div class="cover-card">
        <div class="cover-tab" style="background:{tab}"></div>
        <img src="../assets/logo_giantinsectworld.png" alt="Giant Insect World">
        <div class="cover-mk">Make your own</div>
        <div class="cover-sp">{s['cover_name']}</div>
        <div class="cover-sp">Instructions</div>
      </div>
      <div class="cover-foot">A Giant Insect World felt puzzle<br>build it &middot; take it apart &middot; build it again</div>
    </div>
    <div class="fuzzle-col">
      <img src="../assets/logo_fuzzleworld.png" alt="FuzzleWorld">
      <div class="fuzzle-tag">Collect the set</div>
      <div class="themes">Meadow &middot; Aquatic &middot; Underground</div>
      <div class="setlist">{s['setlist']}</div>
      <div class="credit">Species: <i>{s['latin']}</i><br>Photo &copy; {s['photo_credit']}<br>Logo &copy; Giant Insect World</div>
    </div>
  </section>
</div></body></html>"""

CUT_HCLASS = ["h-red","h-blue","h-amber"]
CUT_BG = ["p-pink","p-blue","p-yellow"]

def cutting(s):
    mat = MAT[s["theme"]]; mtx = MAT_TXT[s["theme"]]
    cells = ""
    for i,pnl in enumerate(s["cut_panels"]):
        cap = pnl["cap"]
        cells += f"""
  <section class="panel cpanel {CUT_BG[i]}">
    <h2 class="{CUT_HCLASS[i]}">{pnl['heading']}</h2>
    <div class="art">{pnl['svg']}</div>
    <div class="cap">{cap}</div>
  </section>"""
    fcap = "<br>".join(s["finished_caption"])
    cells += f"""
  <section class="panel cpanel p-green">
    <h2 class="h-green">Finished! &#11088;</h2>
    <div class="art">
      <div class="fcard" style="background:{mat}">
        {s['finished_svg']}
        <div class="txt" style="color:{mtx}">{fcap}</div>
      </div>
    </div>
  </section>"""
    return head() + f"""
<div class="sheet grid4">{cells}
  <div class="footer">&#9986; Cut along the solid lines!</div>
</div></body></html>"""

def main():
    for key,s in SPECIES.items():
        (OUT/f"{key}_instructions.html").write_text(instructions(s), encoding="utf-8")
        (OUT/f"{key}_cutting.html").write_text(cutting(s), encoding="utf-8")
        print("wrote", key)

if __name__ == "__main__":
    main()
