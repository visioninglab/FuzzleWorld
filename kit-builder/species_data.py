# -*- coding: utf-8 -*-
"""Per-species content + felt-piece shapes for FuzzleWorld sheets.
Shapes are mm-accurate inline SVG (1 user unit = 1 mm) so they print true size.
Edit freely: text is plain, shapes are simple SVG paths/ellipses.
"""

# felt colours
BLK="#1c1c1c"; RED="#e23320"
GREY="#9a9a9a"; DGREY="#5f5f5f"
TAN="#dcc9a0"; MBROWN="#8a5a2b"; GOLD="#d9a441"; MAROON="#5e2b2b"
DBROWN="#4a3524"; SILVER="#cdd6da"
GREEN="#6ab04a"; WTAN="#d8c48f"
RBROWN="#a8552f"; PORANGE="#e0a86a"
ORANGE="#e8801f"; CREAM="#efe6c8"
OL="#333"  # cut outline

import math

def legs_row(defs, color, w=1.8):
    """defs: list of (x1,y1,x2,y2,x3,y3) bent legs (stroked)."""
    s=f'<g fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">'
    for d in defs: s+=f'<path d="M{d[0]} {d[1]} L{d[2]} {d[3]} L{d[4]} {d[5]}"/>'
    return s+"</g>"

def _taper(x1,y1,x2,y2,w):
    """One separate tapered leg piece: base width w at (x1,y1) -> point at (x2,y2)."""
    dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy) or 1
    px,py=-dy/L*w/2, dx/L*w/2
    return f'M{x1+px:.1f} {y1+py:.1f} L{x1-px:.1f} {y1-py:.1f} L{x2:.1f} {y2:.1f} Z'

def sep_legs(color, segs, w=3.0):
    """Group of individually-cuttable tapered legs. segs: list of (x1,y1,x2,y2)."""
    body="".join(f'<path d="{_taper(*s,w)}"/>' for s in segs)
    return f'<g fill="{color}" stroke="{OL}" stroke-width="0.4">{body}</g>'

def bent_antenna(x1,y1,x2,y2,x3,y3,color,w=2.2,club=2.4):
    """One separate elbowed antenna with a little club at the outer tip."""
    return (f'<g fill="{color}" stroke="{color}"><path fill="none" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round" d="M{x1} {y1} L{x2} {y2} L{x3} {y3}"/>'
            f'<circle cx="{x3}" cy="{y3}" r="{club}"/></g>')

SPECIES = {}

# ================================================================= LADYBIRD
SPECIES["ladybird"] = {
 "name":"7-spot Ladybird", "cover_name":"7-spot Ladybird",
 "theme":"meadow", "photo":"photo_ladybird.jpg",
 "latin":"Coccinella septempunctata", "photo_credit":"Alfie Felton, CC0",
 "setlist":"butterfly &middot; ladybird &middot; grasshopper<br>river skater &middot; dragonfly &middot; more&hellip;",
 "needs":["Red, black &amp; white felt or paper","Scissors","This instruction sheet and template",
          "The green felt mat for insect habitat (optional)"],
 "steps":["Trace each shape onto the right felt colour.","Cut out all 17 pieces carefully.",
          "Lay the green mat down &mdash; that's your meadow!","Place the red body, then the black head and antennae.",
          "Tuck 6 legs under &mdash; three each side.","Dot on the 7 spots. Done!"],
 "facts":["The 7-spot ladybird is Britain's most common!","It eats hundreds of aphids &mdash; gardeners love it.",
          "Bright red warns birds it tastes horrible!","It can ooze yucky yellow blood from its knees!",
          "They hibernate in big groups over winter."],
 "find_colours":"Red &middot; Black &middot; White", "swatches":[RED,BLK,"#ffffff"],
 "pieces":[("Body &times;1","&mdash; red"),("Head &times;1","&mdash; black (2 white cheek dots)"),
           ("Legs &times;6","&mdash; black (pointy ends)"),("Antennae &times;2","&mdash; black (round ends)"),
           ("Spots &times;7","&mdash; black (small circles)")],
 "total_text":"That's 17 shapes in total!", "pieces_note":"Plus 2 white cheek dots (optional).",
 "finished_lines":["Your ladybird is about 7 &times; 6 cm.","Take it apart and build it again!",
    "Move the spots around &mdash; every ladybird can be different!",
    '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Meadow: butterfly, ladybird, grasshopper"],
 "cut_panels":[
   {"heading":"Body &times;1","cap":"<b>Red felt &middot; cut 1</b><br>Dashed line = centre (don't cut!)",
    "svg":f'<svg width="66mm" height="66mm" viewBox="0 0 66 66"><circle cx="33" cy="33" r="31.5" fill="{RED}" stroke="#111" stroke-width="0.5"/><line x1="33" y1="4" x2="33" y2="62" stroke="#8a8a8a" stroke-width="0.5" stroke-dasharray="2 2"/></svg>'},
   {"heading":"Head, legs &amp; antennae","cap":"<b>Black felt &middot; cut 1 head + 6 legs + 2 antennae</b><br>All separate pieces &middot; legs taper to a point",
    "svg":f'''<svg width="118mm" height="52mm" viewBox="0 0 118 52">
      <path d="M8 34 A13 13 0 0 1 34 34 Z" fill="{BLK}"/>
      <circle cx="15" cy="30" r="2.6" fill="#fff"/><circle cx="27" cy="30" r="2.6" fill="#fff"/>
      {sep_legs(BLK,[(50,12,38,10),(50,25,37,24),(50,38,38,40),(64,12,76,10),(64,25,77,24),(64,38,76,40)],3.0)}
      {bent_antenna(88,40,94,26,100,23,BLK,2.2,2.4)}{bent_antenna(104,40,110,26,116,23,BLK,2.2,2.4)}</svg>'''},
   {"heading":"Spots &times;7","cap":"<b>Black felt &middot; cut 7 circles</b><br>1 top-centre + 3 on each side",
    "svg":f'''<svg width="96mm" height="42mm" viewBox="0 0 96 42"><g fill="{BLK}">
      <circle cx="14" cy="12" r="5.5"/><circle cx="36" cy="12" r="5.5"/><circle cx="58" cy="12" r="5.5"/><circle cx="80" cy="12" r="5.5"/>
      <circle cx="25" cy="30" r="5.5"/><circle cx="47" cy="30" r="5.5"/><circle cx="69" cy="30" r="5.5"/></g></svg>'''},
 ],
 "finished_caption":["This is what it","looks like!","About 7 &times; 6 cm","when done"],
 "finished_svg":f'''<svg width="42mm" height="46mm" viewBox="0 0 120 130">
   <g stroke="#111" stroke-width="2.4" stroke-linecap="round"><path d="M40 66 L14 52"/><path d="M40 80 L12 80"/><path d="M40 94 L16 108"/><path d="M80 66 L106 52"/><path d="M80 80 L108 80"/><path d="M80 94 L104 108"/></g>
   <g stroke="#111" stroke-width="2.4" stroke-linecap="round"><path d="M52 30 L44 12" fill="none"/><path d="M68 30 L76 12" fill="none"/></g>
   <circle cx="43" cy="11" r="3.2" fill="#111"/><circle cx="77" cy="11" r="3.2" fill="#111"/>
   <ellipse cx="60" cy="78" rx="34" ry="40" fill="{RED}" stroke="#111" stroke-width="2"/>
   <line x1="60" y1="42" x2="60" y2="116" stroke="#111" stroke-width="2"/>
   <path d="M42 44 A18 18 0 0 1 78 44 Z" fill="#141414"/>
   <circle cx="52" cy="40" r="3.6" fill="#fff"/><circle cx="68" cy="40" r="3.6" fill="#fff"/>
   <g fill="#141414"><circle cx="60" cy="56" r="5"/><circle cx="45" cy="70" r="5.5"/><circle cx="75" cy="70" r="5.5"/><circle cx="42" cy="90" r="5.5"/><circle cx="78" cy="90" r="5.5"/><circle cx="52" cy="104" r="5"/><circle cx="68" cy="104" r="5"/></g></svg>''',
}

# ================================================================= ANT
SPECIES["ant"] = {
 "name":"Black Garden Ant", "cover_name":"Black Garden Ant",
 "theme":"underground", "photo":"photo_ant.jpg",
 "latin":"Lasius niger", "photo_credit":"Alfie Felton, CC-BY",
 "setlist":"woodlouse &middot; earthworm &middot; ant<br>butterfly &middot; dragonfly &middot; more&hellip;",
 "needs":["Black felt or paper","Scissors","This instruction sheet and template",
          "The brown felt mat for soil habitat (optional)"],
 "steps":["Trace each shape onto the black felt.","Cut out all 11 pieces carefully.",
          "Lay the brown mat down &mdash; that's your soil!","Place head, thorax and gaster in a line &mdash; leave a thin waist.",
          "Add 6 legs from the thorax, three each side.","Add 2 bent antennae on the head. Done!"],
 "facts":["Ants live in huge colonies ruled by one big queen.","They \"talk\" with smells and little touches.",
          "An ant can lift 50&times; its own body weight!","On warm days, winged ants fly off to start new nests.",
          "Its 3 parts: head, thorax and gaster (the big rear)."],
 "find_colours":"Black", "swatches":[BLK],
 "pieces":[("Head &times;1","&mdash; black"),("Thorax &times;1","&mdash; black"),("Gaster &times;1","&mdash; black (big rear)"),
           ("Legs &times;6","&mdash; black (bent in middle)"),("Antennae &times;2","&mdash; black (bent)")],
 "total_text":"That's 11 shapes in total!", "pieces_note":"Just one colour &mdash; the simplest kit in the set!",
 "finished_lines":["Your ant is about 8 &times; 5 cm.","Take it apart and build it again!",
   "Make a whole colony and line them up in a trail!",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Underground: woodlouse, earthworm, ant"],
 "cut_panels":[
   {"heading":"Body parts &times;3","cap":"<b>Black felt &middot; cut 1 head + 1 thorax + 1 gaster</b><br>Leave thin gaps between them",
    "svg":f'''<svg width="100mm" height="46mm" viewBox="0 0 100 46">
      <circle cx="14" cy="23" r="9" fill="{BLK}"/><ellipse cx="40" cy="23" rx="9" ry="11" fill="{BLK}"/><ellipse cx="76" cy="23" rx="17" ry="19" fill="{BLK}"/></svg>'''},
   {"heading":"Legs &times;6","cap":"<b>Black felt &middot; cut 6 legs</b><br>Bent in the middle, like a real ant leg",
    "svg":f'''<svg width="108mm" height="52mm" viewBox="0 0 108 52">'''+legs_row([
      (4,10,20,16,34,8),(40,10,56,16,70,8),(76,10,92,16,106,8),
      (4,44,20,38,34,46),(40,44,56,38,70,46),(76,44,92,38,106,46)],BLK,2.2)+'</svg>'},
   {"heading":"Antennae &times;2","cap":"<b>Black felt &middot; cut 2 antennae</b><br>Bent, with a little club on the end",
    "svg":f'''<svg width="86mm" height="40mm" viewBox="0 0 86 40">'''+
      bent_antenna(8,32,24,14,40,17,BLK,2.6,2.6)+bent_antenna(48,32,64,14,80,17,BLK,2.6,2.6)+'</svg>'},
 ],
 "finished_caption":["This is what it","looks like!","About 8 &times; 5 cm","when done"],
 "finished_svg":f'''<svg width="34mm" height="48mm" viewBox="0 0 70 100">
   <g stroke="#111" stroke-width="2" fill="none" stroke-linecap="round"><path d="M35 40 L14 28"/><path d="M35 48 L10 46"/><path d="M35 56 L14 66"/><path d="M35 40 L56 28"/><path d="M35 48 L60 46"/><path d="M35 56 L56 66"/></g>
   <g stroke="#111" stroke-width="2" fill="none" stroke-linecap="round"><path d="M30 20 L22 6"/><path d="M40 20 L48 6"/></g>
   <ellipse cx="35" cy="78" rx="18" ry="20" fill="{BLK}"/><ellipse cx="35" cy="50" rx="9" ry="11" fill="{BLK}"/><circle cx="35" cy="24" r="9" fill="{BLK}"/></svg>''',
}

# ================================================================= WOODLOUSE
SPECIES["woodlouse"] = {
 "name":"Common Shiny Woodlouse", "cover_name":"Shiny Woodlouse",
 "theme":"underground", "photo":"photo_woodlouse.jpg",
 "latin":"Oniscus asellus", "photo_credit":"Stuart Fraser, CC-BY",
 "setlist":"woodlouse &middot; earthworm &middot; ant<br>butterfly &middot; dragonfly &middot; more&hellip;",
 "needs":["Grey &amp; dark-grey felt or paper","Scissors","This instruction sheet and template",
          "The brown felt mat for soil habitat (optional)"],
 "steps":["Trace each shape onto the right felt colour.","Cut out all 10 pieces carefully.",
          "Lay the brown mat down &mdash; that's your soil!","Place the grey body, then add the head at the front.",
          "Tuck 6 legs under and add 2 antennae.","The lines show its armour segments. Done!"],
 "facts":["It's a crustacean &mdash; more closely related to crabs!","It breathes through gills and needs damp places.",
          "It recycles rotting leaves, helping make new soil.","Also called a roly-poly, cheeselog or pill bug.",
          "When scared it can roll up into a tiny ball."],
 "find_colours":"Grey &middot; Dark grey", "swatches":[GREY,DGREY],
 "pieces":[("Body &times;1","&mdash; grey (segmented oval)"),("Head &times;1","&mdash; grey"),
           ("Legs &times;6","&mdash; dark grey"),("Antennae &times;2","&mdash; grey")],
 "total_text":"That's 10 shapes in total!", "pieces_note":None,
 "finished_lines":["Your woodlouse is about 5 &times; 3 cm.","Take it apart and build it again!",
   "Real woodlice can roll into a ball!",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Underground: woodlouse, earthworm, ant"],
 "cut_panels":[
   {"heading":"Body &times;1","cap":"<b>Grey felt &middot; cut 1</b><br>Thin lines = armour segments (don't cut)",
    "svg":f'''<svg width="90mm" height="40mm" viewBox="0 0 90 40">
      <ellipse cx="45" cy="20" rx="43" ry="17" fill="{GREY}" stroke="{OL}" stroke-width="0.5"/>
      <g stroke="#6f6f6f" stroke-width="0.7" fill="none"><path d="M22 5 Q20 20 22 35"/><path d="M35 4 Q33 20 35 36"/><path d="M48 4 Q46 20 48 36"/><path d="M61 5 Q59 20 61 35"/></g></svg>'''},
   {"heading":"Head &amp; antennae","cap":"<b>Grey felt &middot; cut 1 head + 2 antennae</b><br>Separate pieces",
    "svg":f'''<svg width="90mm" height="42mm" viewBox="0 0 90 42">
      <ellipse cx="20" cy="21" rx="13" ry="10" fill="{GREY}" stroke="{OL}" stroke-width="0.5"/>'''+
      sep_legs(GREY,[(46,16,86,10),(46,26,86,30)],3.0)+'</svg>'},
   {"heading":"Legs &times;6","cap":"<b>Dark grey felt &middot; cut 6 legs</b><br>Three each side &mdash; separate",
    "svg":f'''<svg width="100mm" height="46mm" viewBox="0 0 100 46">'''+sep_legs(DGREY,[
      (46,11,10,6),(54,11,90,6),(46,23,8,23),(54,23,92,23),(46,35,10,40),(54,35,90,40)],3.2)+'</svg>'},
 ],
 "finished_caption":["This is what it","looks like!","About 5 &times; 3 cm","when done"],
 "finished_svg":f'''<svg width="46mm" height="30mm" viewBox="0 0 92 60">
   <g stroke="#6f6f6f" stroke-width="2" stroke-linecap="round"><path d="M30 30 L14 20"/><path d="M40 32 L26 40"/><path d="M50 30 L40 20"/><path d="M60 32 L52 42"/><path d="M70 30 L62 20"/><path d="M78 33 L72 42"/></g>
   <ellipse cx="52" cy="30" rx="34" ry="16" fill="{GREY}" stroke="{OL}" stroke-width="1"/>
   <g stroke="#6f6f6f" stroke-width="1" fill="none"><path d="M34 16 Q32 30 34 44"/><path d="M46 15 Q44 30 46 45"/><path d="M58 15 Q56 30 58 45"/><path d="M70 16 Q68 30 70 44"/></g>
   <ellipse cx="16" cy="30" rx="11" ry="9" fill="{GREY}" stroke="{OL}" stroke-width="1"/>
   <g fill="none" stroke="{GREY}" stroke-width="2" stroke-linecap="round"><path d="M8 26 L0 20"/><path d="M8 34 L0 40"/></g></svg>''',
}

# ================================================================= RIVER SKATER
SPECIES["riverskater"] = {
 "name":"River Skater", "cover_name":"River Skater",
 "theme":"aquatic", "photo":"photo_riverskater.jpg",
 "latin":"Aquarius najas", "photo_credit":"Alfie Felton, CC0",
 "setlist":"river skater &middot; dragonfly &middot; bell spider<br>butterfly &middot; ladybird &middot; more&hellip;",
 "needs":["Pale tan, mid-brown, golden &amp; dark-maroon felt","Scissors","This instruction sheet and template",
          "The blue felt mat for pond habitat (optional)"],
 "steps":["Trace each shape onto the right felt colour.","Cut out all 13 pieces carefully.",
          "Lay the blue mat down &mdash; that's your pond!","Place the underbody, then the back on top.",
          "Add the golden head, 2 eyes and 2 antennae.","Tuck 6 legs under &mdash; splayed out wide. Done!"],
 "facts":["It skates on the surface film of ponds and rivers.","Water-repellent leg hairs trap air, so it never sinks.",
          "It feels ripples in the water to find food.","The long middle legs row; the back legs steer.",
          "One of Britain's largest pond skaters."],
 "find_colours":"Pale tan &middot; Mid brown &middot; Golden &middot; Dark maroon", "swatches":[TAN,MBROWN,GOLD,MAROON],
 "pieces":[("Underbody &times;1","&mdash; pale tan"),("Back &times;1","&mdash; mid brown"),("Head &times;1","&mdash; golden tan"),
           ("Eyes &times;2","&mdash; dark maroon"),("Legs &times;6","&mdash; mid brown"),("Antennae &times;2","&mdash; dark maroon")],
 "total_text":"That's 13 shapes in total!", "pieces_note":None,
 "finished_lines":["Your river skater is about 11 &times; 9 cm.","Take it apart and build it again!",
   "Slender body, legs splayed wide &mdash; the middle pair longest.",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Aquatic: river skater, dragonfly, bell spider"],
 "cut_panels":[
   {"heading":"Underbody &amp; back","cap":"<b>Pale-tan underbody &times;1 + mid-brown back &times;1</b><br>Dashed = centre guide (don't cut)",
    "svg":f'''<svg width="100mm" height="46mm" viewBox="0 0 100 46">
      <path d="M3 16 Q50 2 97 16 Q50 30 3 16 Z" fill="{TAN}" stroke="{OL}" stroke-width="0.5"/>
      <line x1="12" y1="16" x2="88" y2="16" stroke="#9a8a60" stroke-width="0.5" stroke-dasharray="2 2"/>
      <path d="M14 37 Q50 27 86 37 Q50 45 14 37 Z" fill="{MBROWN}" stroke="{OL}" stroke-width="0.5"/></svg>'''},
   {"heading":"Head, eyes &amp; antennae","cap":"<b>Golden head &times;1 &middot; 2 dark-maroon eyes &middot; 2 antennae</b>",
    "svg":f'''<svg width="90mm" height="42mm" viewBox="0 0 90 42">
      <ellipse cx="22" cy="21" rx="13" ry="10" fill="{GOLD}" stroke="{OL}" stroke-width="0.5"/>
      <circle cx="44" cy="14" r="4.5" fill="{MAROON}"/><circle cx="44" cy="28" r="4.5" fill="{MAROON}"/>'''+
      sep_legs(MAROON,[(58,15,88,9),(58,27,88,33)],2.8)+'</svg>'},
   {"heading":"Legs &times;6","cap":"<b>Mid-brown felt &middot; cut 6 legs</b><br>2 short front &middot; 2 long middle &middot; 2 hind &mdash; separate",
    "svg":f'''<svg width="118mm" height="58mm" viewBox="0 0 118 58">'''+sep_legs(MBROWN,[
      (56,10,26,4),(62,10,92,4),(56,29,4,24),(62,29,114,24),(56,49,22,56),(62,49,96,56)],3.0)+'</svg>'},
 ],
 "finished_caption":["This is what it","looks like!","About 11 &times; 9 cm","when done"],
 "finished_svg":f'''<svg width="52mm" height="42mm" viewBox="0 0 104 84">
   <g fill="none" stroke="{MBROWN}" stroke-width="2" stroke-linecap="round"><path d="M52 40 L24 18"/><path d="M52 40 L80 18"/><path d="M52 42 L4 8"/><path d="M52 42 L100 8"/><path d="M52 44 L22 76"/><path d="M52 44 L82 76"/></g>
   <ellipse cx="52" cy="42" rx="30" ry="7" fill="{TAN}" stroke="{OL}" stroke-width="1"/><ellipse cx="52" cy="42" rx="26" ry="4.5" fill="{MBROWN}"/>
   <ellipse cx="52" cy="24" rx="8" ry="6" fill="{GOLD}" stroke="{OL}" stroke-width="1"/>
   <circle cx="47" cy="20" r="2.6" fill="{MAROON}"/><circle cx="57" cy="20" r="2.6" fill="{MAROON}"/></svg>''',
}

# ================================================================= BELL SPIDER
SPECIES["bellspider"] = {
 "name":"Diving Bell Spider", "cover_name":"Bell Spider",
 "theme":"aquatic", "photo":"photo_bellspider.jpg",
 "latin":"Argyroneta aquatica", "photo_credit":"mark-sundown, CC-BY",
 "setlist":"river skater &middot; dragonfly &middot; bell spider<br>butterfly &middot; ladybird &middot; more&hellip;",
 "needs":["Dark-brown &amp; pale-silver felt","Scissors","This instruction sheet and template",
          "The blue felt mat for pond habitat (optional)"],
 "steps":["Trace each shape onto the right felt colour.","Cut out all 11 pieces carefully.",
          "Lay the blue mat down &mdash; that's your pond!","Place the pale air bubble &mdash; its diving bell.",
          "Round body at top, big abdomen on the bubble.","Add 8 legs &mdash; 4 each side, spread wide. Done!"],
 "facts":["The only spider that lives its whole life underwater.","It spins a silk \"bell\" and fills it with air from above.",
          "It breathes the trapped air like a tiny aqualung.","Britain's only underwater spider.",
          "It hunts water insects and tiny pond creatures."],
 "find_colours":"Dark brown &middot; Pale silver", "swatches":[DBROWN,SILVER],
 "pieces":[("Cephalothorax &times;1","&mdash; dark brown (front body)"),("Abdomen &times;1","&mdash; dark brown (round rear)"),
           ("Legs &times;8","&mdash; dark brown"),("Air bubble &times;1","&mdash; pale silver")],
 "total_text":"That's 11 shapes in total!", "pieces_note":None,
 "finished_lines":["Your bell spider is about 8 &times; 8 cm.","Take it apart and build it again!",
   "Body sits on its air bubble, 8 legs out wide.",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Aquatic: river skater, dragonfly, bell spider"],
 "cut_panels":[
   {"heading":"Body &times;2","cap":"<b>Dark-brown felt &middot; cut 1 cephalothorax + 1 abdomen</b>",
    "svg":f'''<svg width="94mm" height="46mm" viewBox="0 0 94 46">
      <circle cx="20" cy="23" r="14" fill="{DBROWN}" stroke="{OL}" stroke-width="0.5"/>
      <circle cx="66" cy="23" r="21" fill="{DBROWN}" stroke="{OL}" stroke-width="0.5"/></svg>'''},
   {"heading":"Legs &times;8","cap":"<b>Dark-brown felt &middot; cut 8 legs</b><br>Four each side &mdash; separate pieces",
    "svg":f'''<svg width="120mm" height="58mm" viewBox="0 0 120 58">'''+sep_legs(DBROWN,[
      (54,10,8,5),(54,24,4,23),(54,38,4,41),(54,52,8,55),
      (66,10,112,5),(66,24,116,23),(66,38,116,41),(66,52,112,55)],3.6)+'</svg>'},
   {"heading":"Air bubble &times;1","cap":"<b>Pale-silver felt &middot; cut 1</b><br>Its diving bell &mdash; sits behind the body",
    "svg":f'''<svg width="54mm" height="54mm" viewBox="0 0 54 54"><circle cx="27" cy="27" r="25" fill="{SILVER}" stroke="#9aa6ad" stroke-width="0.8"/></svg>'''},
 ],
 "finished_caption":["This is what it","looks like!","About 8 &times; 8 cm","when done"],
 "finished_svg":f'''<svg width="44mm" height="44mm" viewBox="0 0 88 88">
   <circle cx="44" cy="50" r="26" fill="{SILVER}" opacity="0.85"/>
   <g fill="none" stroke="{DBROWN}" stroke-width="2.2" stroke-linecap="round"><path d="M44 44 L8 20"/><path d="M44 44 L4 38"/><path d="M44 44 L4 54"/><path d="M44 44 L10 72"/><path d="M44 44 L80 20"/><path d="M44 44 L84 38"/><path d="M44 44 L84 54"/><path d="M44 44 L78 72"/></g>
   <circle cx="44" cy="54" r="18" fill="{DBROWN}" stroke="{OL}" stroke-width="1"/><circle cx="44" cy="30" r="11" fill="{DBROWN}" stroke="{OL}" stroke-width="1"/></svg>''',
}

# ================================================================= GRASSHOPPER
SPECIES["grasshopper"] = {
 "name":"Meadow Grasshopper", "cover_name":"Meadow Grasshopper",
 "theme":"meadow", "photo":"photo_grasshopper.jpg",
 "latin":"Pseudochorthippus parallelus", "photo_credit":"Susan Marley, CC-BY",
 "setlist":"butterfly &middot; ladybird &middot; grasshopper<br>river skater &middot; dragonfly &middot; more&hellip;",
 "needs":["Green, tan &amp; black felt or paper","Scissors","This instruction sheet and template",
          "The green felt mat for meadow habitat (optional)"],
 "steps":["Trace each shape onto the right felt colour.","Cut out all 9 pieces carefully.",
          "Lay the green mat down &mdash; that's your meadow!","Place the body, head to the left; wing on its back.",
          "Add the big hind leg: femur, then thin tibia.","Add 2 front legs, the eye and 2 antennae. Done!"],
 "facts":["It \"sings\" by rubbing its legs against its wings.","Its big back legs can jump 20&times; its body length.",
          "Green or brown, to hide among the grass.","Listen for its soft \"rrr-rrr\" on warm summer days.",
          "It eats grass and basks in the sun."],
 "find_colours":"Green &middot; Tan &middot; Black", "swatches":[GREEN,WTAN,BLK],
 "pieces":[("Body &times;1","&mdash; green"),("Wing &times;1","&mdash; tan"),("Hind femur &times;1 + tibia &times;1","&mdash; green"),
           ("Front legs &times;2","&mdash; green"),("Eye &times;1","&mdash; black"),("Antennae &times;2","&mdash; green")],
 "total_text":"That's 9 shapes in total!", "pieces_note":None,
 "finished_lines":["Your grasshopper is about 11 &times; 6 cm.","Take it apart and build it again!",
   "Bend the hind leg into a Z &mdash; ready to spring!",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Meadow: butterfly, ladybird, grasshopper"],
 "cut_panels":[
   {"heading":"Body &amp; wing","cap":"<b>Green body &times;1 + tan wing &times;1</b><br>Body has the head at the left",
    "svg":f'''<svg width="108mm" height="52mm" viewBox="0 0 108 52">
      <path d="M6 30 Q8 15 26 17 Q62 19 100 27 Q64 39 26 41 Q8 43 6 30 Z" fill="{GREEN}" stroke="{OL}" stroke-width="0.5"/>
      <path d="M16 9 Q56 1 98 9 Q56 17 16 9 Z" fill="{WTAN}" stroke="{OL}" stroke-width="0.5"/></svg>'''},
   {"heading":"Hind leg (2 parts)","cap":"<b>Green felt &middot; 1 hind femur + 1 hind tibia</b><br>Two separate pieces &mdash; bend into a Z",
    "svg":f'''<svg width="94mm" height="54mm" viewBox="0 0 94 54">
      <path d="M6 46 Q8 12 42 16 Q56 21 47 40 Q33 50 16 49 Q9 49 6 46 Z" fill="{GREEN}" stroke="{OL}" stroke-width="0.5"/>'''+
      sep_legs(GREEN,[(54,18,90,48)],5.5)+'</svg>'},
   {"heading":"Front legs, eye &amp; antennae","cap":"<b>2 front legs (green) &middot; 1 eye (black) &middot; 2 antennae (green)</b>",
    "svg":f'''<svg width="98mm" height="44mm" viewBox="0 0 98 44">'''+
      sep_legs(GREEN,[(10,8,20,34),(28,8,38,34)],4.0)+
      f'<circle cx="56" cy="21" r="6" fill="{BLK}"/>'+
      sep_legs(GREEN,[(74,34,96,8),(82,36,98,14)],2.6)+'</svg>'},
 ],
 "finished_caption":["This is what it","looks like!","About 11 &times; 6 cm","when done"],
 "finished_svg":f'''<svg width="40mm" height="46mm" viewBox="0 0 90 104">
   <g fill="none" stroke="{GREEN}" stroke-linecap="round" stroke-linejoin="round">
     <path d="M40 66 L13 53 L23 93" stroke-width="6"/><path d="M50 66 L77 53 L67 93" stroke-width="6"/></g>
   <g fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round">
     <path d="M37 34 L15 26"/><path d="M53 34 L75 26"/><path d="M36 48 L13 47"/><path d="M54 48 L77 47"/></g>
   <path d="M45 22 Q57 30 54 60 Q51 88 45 95 Q39 88 36 60 Q33 30 45 22 Z" fill="{GREEN}" stroke="{OL}" stroke-width="1"/>
   <path d="M45 30 Q54 56 45 86 Q36 56 45 30 Z" fill="{WTAN}" stroke="{OL}" stroke-width="1"/>
   <ellipse cx="45" cy="16" rx="9" ry="8" fill="{GREEN}" stroke="{OL}" stroke-width="1"/>
   <circle cx="41" cy="14" r="2.4" fill="{BLK}"/><circle cx="49" cy="14" r="2.4" fill="{BLK}"/>
   <g fill="none" stroke="{GREEN}" stroke-width="2" stroke-linecap="round"><path d="M42 9 Q37 4 32 1"/><path d="M48 9 Q53 4 58 1"/></g></svg>''',
}

# ================================================================= EARTHWORM
SPECIES["earthworm"] = {
 "name":"Common Earthworm", "cover_name":"Common Earthworm",
 "theme":"underground", "photo":"photo_earthworm.jpg",
 "latin":"Lumbricus terrestris", "photo_credit":"Daniel Buczkiewicz, CC-BY",
 "setlist":"woodlouse &middot; earthworm &middot; ant<br>butterfly &middot; dragonfly &middot; more&hellip;",
 "needs":["Reddish-brown &amp; pale-orange felt","Scissors","This instruction sheet and template",
          "The brown felt mat for soil habitat (optional)"],
 "steps":["Trace each shape onto the reddish-brown felt.","Cut out all 3 pieces carefully.",
          "Lay the brown mat down &mdash; that's your soil!","Place the front body, pointed head at the top.",
          "Add the rear body below; curve them into an S.","Lay the pale saddle over the join. Done!"],
 "facts":["No eyes, ears or bones &mdash; it breathes through its skin.","It eats its way through soil, recycling dead leaves.",
          "Its tunnels let air and water into the ground.","Charles Darwin studied worms for 39 years!",
          "Tiny bristles grip the soil so it can pull itself along."],
 "find_colours":"Reddish brown &middot; Pale orange", "swatches":[RBROWN,PORANGE],
 "pieces":[("Front body &times;1","&mdash; reddish brown"),("Rear body &times;1","&mdash; reddish brown"),
           ("Saddle &times;1","&mdash; pale orange")],
 "total_text":"That's 3 shapes in total!", "pieces_note":"The simplest kit in the set &mdash; a great first puzzle.",
 "finished_lines":["Your earthworm is about 12 &times; 4 cm.","Take it apart and build it again!",
   "Wiggle it into any shape you like &mdash; worms are bendy!",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Underground: woodlouse, earthworm, ant"],
 "cut_panels":[
   {"heading":"Front body &times;1","cap":"<b>Reddish-brown felt &middot; cut 1</b><br>Pointed end = head &middot; lines = segment rings",
    "svg":f'''<svg width="118mm" height="34mm" viewBox="0 0 118 34">
      <path d="M4 17 Q30 5 116 12 Q116 22 4 17 Z" fill="{RBROWN}" stroke="{OL}" stroke-width="0.5"/>
      <g stroke="#7a3d22" stroke-width="0.7" fill="none"><path d="M40 9 Q39 15 40 21"/><path d="M58 8 Q57 15 58 22"/><path d="M76 9 Q75 15 76 21"/><path d="M94 10 Q93 15 94 20"/></g></svg>'''},
   {"heading":"Rear body &times;1","cap":"<b>Reddish-brown felt &middot; cut 1</b><br>Joins the front body in the middle",
    "svg":f'''<svg width="118mm" height="34mm" viewBox="0 0 118 34">
      <path d="M4 12 Q80 6 114 17 Q80 28 4 22 Q0 17 4 12 Z" fill="{RBROWN}" stroke="{OL}" stroke-width="0.5"/>
      <g stroke="#7a3d22" stroke-width="0.7" fill="none"><path d="M30 10 Q29 17 30 24"/><path d="M50 9 Q49 17 50 25"/><path d="M70 9 Q69 17 70 25"/><path d="M90 11 Q89 17 90 23"/></g></svg>'''},
   {"heading":"Saddle &times;1","cap":"<b>Pale-orange felt &middot; cut 1</b><br>The \"saddle\" &mdash; sits over the join",
    "svg":f'''<svg width="60mm" height="30mm" viewBox="0 0 60 30"><ellipse cx="30" cy="15" rx="28" ry="12" fill="{PORANGE}" stroke="{OL}" stroke-width="0.5"/></svg>'''},
 ],
 "finished_caption":["This is what it","looks like!","About 12 &times; 4 cm","when done"],
 "finished_svg":f'''<svg width="46mm" height="46mm" viewBox="0 0 92 92">
   <path d="M20 8 Q70 20 60 46 Q52 66 78 84" fill="none" stroke="{RBROWN}" stroke-width="16" stroke-linecap="round"/>
   <ellipse cx="62" cy="42" rx="10" ry="8" fill="{PORANGE}" transform="rotate(20 62 42)"/></svg>''',
}

# ================================================================= DRAGONFLY
SPECIES["dragonfly"] = {
 "name":"Common Darter Dragonfly", "cover_name":"Dragonfly",
 "theme":"aquatic", "photo":"photo_dragonfly.jpg",
 "latin":"Sympetrum striolatum", "photo_credit":"Sheelagh Halsey, CC-BY",
 "setlist":"river skater &middot; dragonfly &middot; bell spider<br>butterfly &middot; ladybird &middot; more&hellip;",
 "needs":["Orange, pale-cream &amp; dark-brown felt","Scissors","This instruction sheet and template",
          "The blue felt mat for pond habitat (optional)"],
 "steps":["Trace each shape onto the right felt colour.","Cut out all 7 pieces carefully.",
          "Lay the blue mat down &mdash; that's your pond!","Place the long orange body down the middle.",
          "Add 2 wings each side &mdash; spread them out wide.","Add the 2 dark eyes at the top (the head). Done!"],
 "facts":["One of the last dragonflies still flying in autumn.","Its 4 wings beat separately &mdash; it can fly backwards.",
          "Huge eyes see almost all the way around.","A fierce hunter, catching midges in mid-air.",
          "It starts life underwater as a nymph."],
 "find_colours":"Orange &middot; Pale cream &middot; Dark brown", "swatches":[ORANGE,CREAM,DBROWN],
 "pieces":[("Body &times;1","&mdash; orange"),("Wings &times;4","&mdash; pale cream"),("Eyes &times;2","&mdash; dark brown")],
 "total_text":"That's 7 shapes in total!", "pieces_note":None,
 "finished_lines":["Your dragonfly is about 9 &times; 8 cm.","Take it apart and build it again!",
   "Long body down the centre, 4 wings out wide.",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Aquatic: river skater, dragonfly, bell spider"],
 "cut_panels":[
   {"heading":"Body &times;1","cap":"<b>Orange felt &middot; cut 1</b><br>Long body &mdash; the head end is fatter",
    "svg":f'''<svg width="100mm" height="34mm" viewBox="0 0 100 34">
      <path d="M4 17 Q16 6 30 12 Q60 15 98 17 Q60 19 30 22 Q16 28 4 17 Z" fill="{ORANGE}" stroke="{OL}" stroke-width="0.5"/></svg>'''},
   {"heading":"Wings &times;4","cap":"<b>Pale-cream felt &middot; cut 4 wings</b><br>Long &amp; narrow &mdash; all the same",
    "svg":f'''<svg width="116mm" height="50mm" viewBox="0 0 116 50"><g fill="{CREAM}" stroke="{OL}" stroke-width="0.5">
      <ellipse cx="30" cy="13" rx="28" ry="7"/><ellipse cx="86" cy="13" rx="28" ry="7"/>
      <ellipse cx="30" cy="37" rx="28" ry="7"/><ellipse cx="86" cy="37" rx="28" ry="7"/></g></svg>'''},
   {"heading":"Eyes &times;2","cap":"<b>Dark-brown felt &middot; cut 2 eyes</b>",
    "svg":f'''<svg width="60mm" height="30mm" viewBox="0 0 60 30"><circle cx="20" cy="15" r="10" fill="{DBROWN}"/><circle cx="42" cy="15" r="10" fill="{DBROWN}"/></svg>'''},
 ],
 "finished_caption":["This is what it","looks like!","About 9 &times; 8 cm","when done"],
 "finished_svg":f'''<svg width="46mm" height="42mm" viewBox="0 0 92 84">
   <g fill="{CREAM}" stroke="{OL}" stroke-width="1"><ellipse cx="26" cy="30" rx="26" ry="7" transform="rotate(-12 26 30)"/><ellipse cx="66" cy="30" rx="26" ry="7" transform="rotate(12 66 30)"/><ellipse cx="24" cy="46" rx="24" ry="6" transform="rotate(10 24 46)"/><ellipse cx="68" cy="46" rx="24" ry="6" transform="rotate(-10 68 46)"/></g>
   <path d="M46 16 Q52 20 50 44 Q48 70 46 80 Q44 70 42 44 Q40 20 46 16 Z" fill="{ORANGE}" stroke="{OL}" stroke-width="1"/>
   <circle cx="41" cy="16" r="6" fill="{DBROWN}"/><circle cx="51" cy="16" r="6" fill="{DBROWN}"/></svg>''',
}

# ================================================================= BUTTERFLY
SPECIES["butterfly"] = {
 "name":"Small Tortoiseshell", "cover_name":"Small Tortoiseshell",
 "theme":"meadow", "photo":"photo_butterfly.jpg",
 "latin":"Aglais urticae", "photo_credit":"newright, CC-BY",
 "setlist":"butterfly &middot; ladybird &middot; grasshopper<br>river skater &middot; dragonfly &middot; more&hellip;",
 "needs":["Orange, black &amp; dark-brown felt","Scissors","This instruction sheet and template",
          "The green felt mat for meadow habitat (optional)"],
 "steps":["Trace each shape onto the right felt colour.","Cut out all 9 pieces carefully.",
          "Lay the green mat down &mdash; that's your meadow!","Place the 2 hindwings, then 2 forewings on top.",
          "Lay the body down the centre, over the wings.","Add a marking to each forewing and 2 antennae. Done!"],
 "facts":["One of Britain's most common, colourful butterflies.","Adults hibernate over winter, often in sheds.",
          "Its caterpillars eat only stinging nettles.","It basks with wings open to warm up in the sun.",
          "The blue crescents on the wing edge warn off birds."],
 "find_colours":"Orange &middot; Black &middot; Dark brown", "swatches":[ORANGE,BLK,DBROWN],
 "pieces":[("Forewings &times;2","&mdash; orange (one mirrored)"),("Hindwings &times;2","&mdash; orange (one mirrored)"),
           ("Markings &times;2","&mdash; black"),("Body &times;1","&mdash; dark brown"),("Antennae &times;2","&mdash; dark brown")],
 "total_text":"That's 9 shapes in total!", "pieces_note":"Optional: white wingtip dots &amp; blue edge dots.",
 "finished_lines":["Your butterfly is about 13 &times; 9 cm.","Take it apart and build it again!",
   "Forewings over hindwings, body down the centre.",
   '<span class="sub" style="margin-top:3mm">Collect the set:</span>',"Meadow: butterfly, ladybird, grasshopper"],
 "cut_panels":[
   {"heading":"Forewings &times;2","cap":"<b>Orange felt &middot; cut 2 forewings</b><br>The big upper wings (one mirrored)",
    "svg":f'''<svg width="116mm" height="54mm" viewBox="0 0 116 54"><g fill="{ORANGE}" stroke="{OL}" stroke-width="0.5">
      <path d="M56 50 Q10 50 6 14 Q40 4 56 24 Z"/><path d="M60 50 Q106 50 110 14 Q76 4 60 24 Z"/></g></svg>'''},
   {"heading":"Hindwings &times;2","cap":"<b>Orange felt &middot; cut 2 hindwings</b><br>Rounded &mdash; sit below the forewings",
    "svg":f'''<svg width="112mm" height="52mm" viewBox="0 0 112 52"><g fill="{ORANGE}" stroke="{OL}" stroke-width="0.5">
      <path d="M54 6 Q10 8 8 34 Q12 50 40 48 Q54 44 54 26 Z"/><path d="M58 6 Q102 8 104 34 Q100 50 72 48 Q58 44 58 26 Z"/></g></svg>'''},
   {"heading":"Body, markings &amp; antennae","cap":"<b>1 body + 2 antennae (dark brown) &middot; 2 markings (black)</b>",
    "svg":f'''<svg width="100mm" height="50mm" viewBox="0 0 100 50">
      <ellipse cx="18" cy="25" rx="6" ry="20" fill="{DBROWN}" stroke="{OL}" stroke-width="0.5"/>
      <g fill="{BLK}"><path d="M40 8 Q54 12 64 6 Q54 18 40 16 Z"/><path d="M40 42 Q54 38 64 44 Q54 32 40 34 Z"/></g>
      <g fill="none" stroke="{DBROWN}" stroke-width="2.2" stroke-linecap="round"><path d="M80 26 Q90 12 96 6"/><path d="M84 26 Q94 18 100 14"/></g></svg>'''},
 ],
 "finished_caption":["This is what it","looks like!","About 13 &times; 9 cm","when done"],
 "finished_svg":f'''<svg width="52mm" height="38mm" viewBox="0 0 104 76">
   <g fill="{ORANGE}" stroke="{OL}" stroke-width="1"><path d="M50 40 Q8 34 6 8 Q34 2 50 22 Z"/><path d="M54 40 Q96 34 98 8 Q70 2 54 22 Z"/>
     <path d="M50 40 Q14 44 12 66 Q34 74 50 58 Z"/><path d="M54 40 Q90 44 92 66 Q70 74 54 58 Z"/></g>
   <g fill="{BLK}"><path d="M24 12 Q34 10 40 14 Q32 20 24 18 Z"/><path d="M80 12 Q70 10 64 14 Q72 20 80 18 Z"/></g>
   <ellipse cx="52" cy="40" rx="5" ry="20" fill="{DBROWN}"/>
   <g fill="none" stroke="{DBROWN}" stroke-width="1.6" stroke-linecap="round"><path d="M50 20 Q44 10 40 6"/><path d="M54 20 Q60 10 64 6"/></g></svg>''',
}
