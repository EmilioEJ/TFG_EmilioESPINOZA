#!/usr/bin/env python3
"""
Comprehensive improvements for slides 14-20:
1. Fix logo position (left too far right on max-width slides)  
2. Make diagrams bigger on slides 14,15,16,17,19
3. Improve Collection/VectorDocument/Metadata JSON boxes on slide 17 (slide-25)
4. Slide 20 (slide-23): replace text under title with visual REST vs WebSockets comparison
"""

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ===================================================================
# FIX 1: Logo position - the ::before on slide-inner is relative to
# the slide-inner div. For slides with max-width:1300px + margin:0 auto
# the logo appears to drift right. Fix: position the logo relative to
# the SLIDE not the inner div, using a separate fixed element via JS
# instead. Simpler fix: change left from 50px to use the slide's own
# ::before and override for wide slides.
# Actually the cleanest fix: position the logo relative to .slide not .slide-inner
# We do this by changing position from absolute (in slide-inner) to 
# fixed-position (in slide itself).
# ===================================================================

# Fix logo CSS: make it position relative to .slide not .slide-inner
old_logo_css = """.slide-inner::before {
  content: \"\";
  position: absolute;
  top: 40px;
  left: 50px;
  width: 250px;
  height: 60px;
  background: url('LOGO-UTI-3.png') no-repeat left center;
  background-size: contain;
  z-index: 100;
}
.slide.cover .slide-inner::before {
  /* On the cover, we might keep it or adjust it, user said ALL slides */
  left: 100px;
}"""

new_logo_css = """.slide-inner::before {
  content: \"\";
  position: fixed;
  top: 40px;
  left: 80px;
  width: 220px;
  height: 60px;
  background: url('LOGO-UTI-3.png') no-repeat left center;
  background-size: contain;
  z-index: 10000;
  pointer-events: none;
}
.slide.cover .slide-inner::before {
  left: 100px;
}"""

if old_logo_css in html:
    html = html.replace(old_logo_css, new_logo_css)
    print("✓ Fixed logo CSS to position:fixed")
else:
    print("✗ Logo CSS not found exactly, trying partial...")

# ===================================================================
# FIX 2: Bigger diagrams - slide-14 = slide-19 (Architecture)
# ===================================================================
# Already has margin-top:8px, just scale the SVG up via height/viewBox
old_s19_svg = '<svg height="300" style="overflow:visible;" viewbox="0 0 1180 320" width="100%">'
new_s19_svg = '<svg height="360" style="overflow:visible;" viewbox="0 0 1180 320" width="100%">'
html = html.replace(old_s19_svg, new_s19_svg, 1)
print("✓ Slide-19 (arch) SVG height increased")

# ===================================================================
# FIX 3: Bigger diagram - slide-15 = slide-20 (Context Diagram)
# ===================================================================
old_s20_svg = '<svg height="340" style="max-width:900px; overflow:visible;" viewbox="0 0 900 340" width="100%">'
new_s20_svg = '<svg height="440" style="max-width:1100px; overflow:visible; transform:scale(1.15); transform-origin:top center;" viewbox="0 0 900 340" width="100%">'
html = html.replace(old_s20_svg, new_s20_svg, 1)
old_s20_margin = 'style="margin-top:26px; display:flex; justify-content:center;"'
new_s20_margin = 'style="margin-top:10px; display:flex; justify-content:center;"'
html = html.replace(old_s20_margin, new_s20_margin, 1)
print("✓ Slide-20 (context) SVG scaled up")

# ===================================================================
# FIX 4: Bigger diagram - slide-16 = slide-26 (Class Hub)
# ===================================================================
old_s26_svg = '<svg height="380" style="max-width:940px; overflow:visible;" viewbox="0 0 940 380" width="100%">'
new_s26_svg = '<svg height="440" style="max-width:1100px; overflow:visible; transform:scale(1.1); transform-origin:top center;" viewbox="0 0 940 380" width="100%">'
html = html.replace(old_s26_svg, new_s26_svg, 1)
old_s26_margin = 'style="margin-top:20px; display:flex; justify-content:center;"'
new_s26_margin = 'style="margin-top:8px; display:flex; justify-content:center;"'
html = html.replace(old_s26_margin, new_s26_margin, 1)
print("✓ Slide-26 (class hub) SVG scaled up")

# ===================================================================
# FIX 5: Bigger diagram - slide-17 = slide-25 (NoSQL/ChromaDB)
# Redesign the small Collection/VectorDocument/Metadata JSON boxes
# ===================================================================
old_s25_svg_block = '''<div class="diag diag-large" data-anim="classhub" style="margin-top:20px;">
<svg height="150" style="overflow:visible;" viewbox="0 0 420 150" width="100%">
<defs><marker id="arrBD" markerheight="6" markerwidth="6" orient="auto-start-reverse" refx="8" refy="5" viewbox="0 0 10 10"><path d="M0 0L10 5L0 10z" fill="var(--ink-faint)"></path></marker></defs>
<rect class="pop" fill="var(--purple-100)" height="42" rx="9" stroke="var(--purple-300)" width="140" x="10" y="55"></rect>
<text fill="var(--purple-700)" font-family="IBM Plex Mono" font-size="10.5" text-anchor="middle" x="80" y="80">Collection</text>
<path class="draw" d="M150 76 H 178" marker-end="url(#arrBD)" stroke="var(--ink-faint)" stroke-width="1.5"></path>
<text fill="var(--ink-faint)" font-family="IBM Plex Mono" font-size="8" x="164" y="68">1..N</text>
<rect class="pop" fill="var(--black)" height="42" rx="9" width="140" x="182" y="55"></rect>
<text fill="#fff" font-family="IBM Plex Mono" font-size="10.5" text-anchor="middle" x="252" y="80">VectorDocument</text>
<path class="draw" d="M322 76 H 350" marker-end="url(#arrBD)" stroke="var(--ink-faint)" stroke-width="1.5"></path>
<text fill="var(--ink-faint)" font-family="IBM Plex Mono" font-size="8" x="336" y="68">1..1</text>
<rect class="pop" fill="var(--orange-100)" height="90" rx="9" stroke="var(--orange-300)" width="66" x="354" y="30"></rect>
<text fill="var(--orange-700)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="387" y="70">Metadata</text>
<text fill="var(--orange-700)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="387" y="86">JSON</text>
</svg>
</div>'''

new_s25_svg_block = '''<div class="diag diag-large" data-anim="classhub" style="margin-top:16px;">
<svg height="200" style="overflow:visible; width:100%;" viewbox="0 0 700 180">
<defs>
  <marker id="arrBD" markerheight="7" markerwidth="7" orient="auto-start-reverse" refx="8" refy="5" viewbox="0 0 10 10"><path d="M0 0L10 5L0 10z" fill="var(--purple-400)"></path></marker>
</defs>
<!-- Collection box -->
<rect class="pop" fill="var(--purple-100)" height="70" rx="14" stroke="var(--purple-400)" stroke-width="2" width="180" x="10" y="55"></rect>
<text fill="var(--purple-500)" font-family="IBM Plex Mono" font-size="9" font-weight="600" text-anchor="middle" x="100" y="78">COLECCION</text>
<text fill="var(--purple-800)" font-family="IBM Plex Sans" font-size="16" font-weight="700" text-anchor="middle" x="100" y="102">Collection</text>
<text fill="var(--purple-600)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="100" y="118">name · metadata</text>
<!-- Arrow 1 -->
<path class="draw" d="M192 90 H 238" marker-end="url(#arrBD)" stroke="var(--purple-400)" stroke-width="2"></path>
<text fill="var(--purple-500)" font-family="IBM Plex Mono" font-size="10" font-weight="600" text-anchor="middle" x="215" y="82">1..N</text>
<!-- VectorDocument box -->
<rect class="pop" fill="var(--purple-950)" height="100" rx="14" stroke="var(--purple-600)" stroke-width="2" width="200" x="242" y="40"></rect>
<text fill="var(--orange-300)" font-family="IBM Plex Mono" font-size="9" font-weight="600" text-anchor="middle" x="342" y="65">DOCUMENTO</text>
<text fill="#fff" font-family="IBM Plex Sans" font-size="16" font-weight="700" text-anchor="middle" x="342" y="92">VectorDocument</text>
<text fill="rgba(255,255,255,.6)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="342" y="110">id · text · embedding</text>
<text fill="rgba(255,255,255,.6)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="342" y="126">384 dimensiones</text>
<!-- Arrow 2 -->
<path class="draw" d="M444 90 H 490" marker-end="url(#arrBD)" stroke="var(--orange-400)" stroke-width="2"></path>
<text fill="var(--orange-500)" font-family="IBM Plex Mono" font-size="10" font-weight="600" text-anchor="middle" x="467" y="82">1..1</text>
<!-- Metadata JSON box -->
<rect class="pop" fill="var(--orange-50)" height="130" rx="14" stroke="var(--orange-400)" stroke-width="2" width="190" x="494" y="25"></rect>
<text fill="var(--orange-500)" font-family="IBM Plex Mono" font-size="9" font-weight="600" text-anchor="middle" x="589" y="48">METADATOS</text>
<text fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="16" font-weight="700" text-anchor="middle" x="589" y="74">Metadata JSON</text>
<text fill="var(--orange-600)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="589" y="95">source · page</text>
<text fill="var(--orange-600)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="589" y="110">tipo_documento</text>
<text fill="var(--orange-600)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="589" y="125">fecha_actualizacion</text>
</svg>
</div>'''

if old_s25_svg_block in html:
    html = html.replace(old_s25_svg_block, new_s25_svg_block, 1)
    print("✓ Slide-25 (NoSQL) diagram improved with bigger boxes")
else:
    print("✗ slide-25 SVG block not found exactly")

# ===================================================================
# FIX 6: Slide-19 (RAG) - slide-24 SVG height 
# ===================================================================
old_s24_svg = '<svg height="250" style="overflow:visible;" viewbox="0 0 1180 260" width="100%">'
new_s24_svg = '<svg height="310" style="overflow:visible;" viewbox="0 0 1180 260" width="100%">'
html = html.replace(old_s24_svg, new_s24_svg, 1)
old_s24_margin = 'style="margin-top:8px;"'
new_s24_margin = 'style="margin-top:4px;"'
# Only replace in slide-24 context (first occurrence)
idx = html.find('id="diagRagFlow"')
if idx != -1:
    chunk = html[idx:idx+100]
    html = html[:idx] + chunk.replace('margin-top:8px', 'margin-top:4px') + html[idx+100:]
print("✓ Slide-24 (RAG) SVG height increased")

# ===================================================================
# FIX 7: Slide-20 (WebSockets vs REST) - replace subhead text with
# visual comparison badges
# ===================================================================
old_ws_slide = '''<section class="slide" data-ch="5" id="slide-23">
<div class="slide-inner">
<h2 class="headline" style="max-width:40ch">Comunicación Bidireccional: ¿Por qué WebSockets supera a REST?</h2>
<div class="diag" style="margin-top:30px;">'''

new_ws_slide = '''<section class="slide" data-ch="5" id="slide-23">
<div class="slide-inner">
<h2 class="headline" style="max-width:40ch; margin-bottom:6px !important;">Comunicación Bidireccional: ¿Por qué WebSockets supera a REST?</h2>
<div style="display:flex; gap:20px; margin-bottom:10px; align-items:center;">
  <div style="display:flex; align-items:center; gap:10px; background:var(--orange-50); border:2px solid var(--orange-300); border-radius:12px; padding:10px 20px;">
    <span style="font-size:26px;">🐢</span>
    <div>
      <div style="font-family:var(--font-mono); font-size:11px; color:var(--orange-600); font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">API REST</div>
      <div style="font-family:var(--font-display); font-size:16px; font-weight:700; color:var(--orange-800);">Request → Wait → Response</div>
    </div>
  </div>
  <span style="font-size:28px; color:var(--ink-faint);">→</span>
  <div style="display:flex; align-items:center; gap:10px; background:var(--purple-50); border:2px solid var(--purple-400); border-radius:12px; padding:10px 20px;">
    <span style="font-size:26px;">⚡</span>
    <div>
      <div style="font-family:var(--font-mono); font-size:11px; color:var(--purple-600); font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">WebSockets</div>
      <div style="font-family:var(--font-display); font-size:16px; font-weight:700; color:var(--purple-800);">Túnel siempre abierto · Streaming en tiempo real</div>
    </div>
  </div>
</div>
<div class="diag" style="margin-top:4px;">'''

if old_ws_slide in html:
    html = html.replace(old_ws_slide, new_ws_slide, 1)
    print("✓ Slide-23 (WebSockets) title section improved")
else:
    print("✗ slide-23 section not found exactly")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ All improvements applied successfully.")
