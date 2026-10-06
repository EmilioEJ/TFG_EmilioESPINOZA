import re

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Slide 20 (slide-23): Move interactive cards to the bottom and make diagram labels bigger
old_ws_badges = """<div style="display:flex; gap:24px; margin-bottom:14px; align-items:stretch;">"""

old_ws_slide_start = """<section class="slide" data-ch="5" id="slide-23">
<div class="slide-inner">
<h2 class="headline" style="max-width:40ch; margin-bottom:6px !important;">Comunicación Bidireccional: ¿Por qué WebSockets supera a REST?</h2>"""

idx_start = html.find(old_ws_slide_start)
if idx_start != -1:
    idx_badges = html.find(old_ws_badges, idx_start)
    idx_diag = html.find('<div class="diag"', idx_start)
    
    if idx_badges != -1 and idx_diag != -1:
        badges_content = html[idx_badges:idx_diag]
        # Remove badges from top
        html = html[:idx_badges] + html[idx_diag:]
        
        # Insert badges at the bottom (before closing div of slide-inner)
        idx_end = html.find('</div>\n</section>', idx_badges)
        if idx_end != -1:
            html = html[:idx_end] + badges_content + html[idx_end:]
            print("✓ Moved WS badges to bottom")

# Make WS diagram text bigger
html = html.replace('font-size="14" font-weight="600" x="0" y="24"', 'font-size="18" font-weight="700" x="0" y="24"')
html = html.replace('font-size="14" font-weight="600" x="0" y="164"', 'font-size="18" font-weight="700" x="0" y="164"')
html = html.replace('font-size="13" font-weight="600" text-anchor="middle"', 'font-size="15" font-weight="600" text-anchor="middle"')
html = html.replace('font-size="13" font-style="italic"', 'font-size="15" font-style="italic"')


# 2. Delete slide 16 (slide-26 - Orquestador) entirely
old_slide_26_start = '<section class="slide" data-ch="5" id="slide-26">'
old_slide_26_end = '</section>\n<section class="slide" data-ch="5" id="slide-25">'
if old_slide_26_start in html and old_slide_26_end in html:
    idx_start = html.find(old_slide_26_start)
    idx_end = html.find(old_slide_26_end)
    html = html[:idx_start] + html[idx_end:]
    print("✓ Deleted slide-26")


# 3. Slide 17 (slide-25) ChromaDB diagram: remove right JSON box, make diagram boxes brighter and bigger
# We need to change the grid-2 to a single column or adjust the layout
# Remove the <div class="slide-inner grid-2"> and replace with normal inner, remove JSON box
html = html.replace('<div class="slide-inner grid-2">\n<div>\n<h2 class="headline" style="max-width:40ch">Base de datos vectorial (NoSQL): Diseño del conocimiento en tres capas.</h2>', 
                    '<div class="slide-inner" style="max-width: 1000px; margin: 0 auto;">\n<h2 class="headline" style="max-width:40ch">Base de datos vectorial (NoSQL): Diseño del conocimiento en tres capas.</h2>')

# Remove the JSON card
json_card = """</div>
<div class="card pop" style="background:var(--black); border:none; font-family:var(--font-mono); font-size:12px; line-height:1.85; color:#D8CFF0; overflow:auto;">
<div class="card-eyebrow" style="color:var(--orange-300);">DOCUMENTO ALMACENADO</div>
<pre style="margin:0; white-space:pre-wrap;">{
  "id": "Reglamento_Titulacion_2024
        .pdf_chunk_42",
  "document": "Art. 15.- Las
    modalidades de titulación...",
  "embedding": [0.0124, -0.0453,
    0.8921, "...(384 dim)"],
  "metadata": {
    "source": "Reglamento_Titulacion
      _2024.pdf",
    "page": 12,
    "tipo_documento":
      "Normativa Institucional"
  }
}</pre>
</div>
</div>
</section>"""
if json_card in html:
    html = html.replace(json_card, '</div>\n</div>\n</section>')
    print("✓ Removed JSON card from slide-25")
else:
    # Try alternate match if the first one fails
    idx = html.find('<div class="card pop" style="background:var(--black)')
    if idx != -1:
        idx_end = html.find('</section>', idx)
        html = html[:idx-6] + '</div>\n</section>' + html[idx_end+10:]
        print("✓ Removed JSON card using alternate method")


# Replace the diagram with a brighter, bigger one
old_s25_diag = """<svg height="200" style="overflow:visible; width:100%;" viewbox="0 0 700 180">
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
</svg>"""

new_s25_diag = """<svg height="300" style="overflow:visible; width:100%; max-width: 900px; margin: 0 auto; display: block;" viewbox="0 0 800 250">
<defs>
  <marker id="arrBD_new" markerheight="7" markerwidth="7" orient="auto-start-reverse" refx="8" refy="5" viewbox="0 0 10 10"><path d="M0 0L10 5L0 10z" fill="var(--purple-500)"></path></marker>
</defs>
<!-- Collection box -->
<rect class="pop" fill="#f3e8ff" height="100" rx="18" stroke="#a855f7" stroke-width="3" width="220" x="10" y="75"></rect>
<text fill="#a855f7" font-family="IBM Plex Mono" font-size="12" font-weight="700" text-anchor="middle" x="120" y="105">COLECCIÓN</text>
<text fill="#6b21a8" font-family="IBM Plex Sans" font-size="22" font-weight="800" text-anchor="middle" x="120" y="140">Collection</text>
<text fill="#9333ea" font-family="IBM Plex Mono" font-size="12" text-anchor="middle" x="120" y="160">name · metadata</text>

<!-- Arrow 1 -->
<path class="draw" d="M232 125 H 285" marker-end="url(#arrBD_new)" stroke="#a855f7" stroke-width="3"></path>
<text fill="#9333ea" font-family="IBM Plex Mono" font-size="14" font-weight="700" text-anchor="middle" x="258" y="115">1..N</text>

<!-- VectorDocument box (brighter purple instead of black) -->
<rect class="pop" fill="#6b21a8" height="140" rx="18" stroke="#d8b4fe" stroke-width="3" width="240" x="295" y="55"></rect>
<text fill="#fbd38d" font-family="IBM Plex Mono" font-size="12" font-weight="700" text-anchor="middle" x="415" y="90">DOCUMENTO</text>
<text fill="#ffffff" font-family="IBM Plex Sans" font-size="22" font-weight="800" text-anchor="middle" x="415" y="125">VectorDocument</text>
<text fill="#e9d5ff" font-family="IBM Plex Mono" font-size="12" text-anchor="middle" x="415" y="150">id · text · embedding</text>
<text fill="#e9d5ff" font-family="IBM Plex Mono" font-size="12" text-anchor="middle" x="415" y="170">384 dimensiones</text>

<!-- Arrow 2 -->
<path class="draw" d="M537 125 H 590" marker-end="url(#arrBD_new)" stroke="#f6ad55" stroke-width="3"></path>
<text fill="#ed8936" font-family="IBM Plex Mono" font-size="14" font-weight="700" text-anchor="middle" x="563" y="115">1..1</text>

<!-- Metadata JSON box (brighter orange) -->
<rect class="pop" fill="#fffaf0" height="180" rx="18" stroke="#f6ad55" stroke-width="3" width="210" x="600" y="35"></rect>
<text fill="#ed8936" font-family="IBM Plex Mono" font-size="12" font-weight="700" text-anchor="middle" x="705" y="70">METADATOS</text>
<text fill="#dd6b20" font-family="IBM Plex Sans" font-size="22" font-weight="800" text-anchor="middle" x="705" y="105">Metadata JSON</text>
<text fill="#dd6b20" font-family="IBM Plex Mono" font-size="13" text-anchor="middle" x="705" y="135">source</text>
<text fill="#dd6b20" font-family="IBM Plex Mono" font-size="13" text-anchor="middle" x="705" y="155">page</text>
<text fill="#dd6b20" font-family="IBM Plex Mono" font-size="13" text-anchor="middle" x="705" y="175">tipo_documento</text>
<text fill="#dd6b20" font-family="IBM Plex Mono" font-size="13" text-anchor="middle" x="705" y="195">fecha_actualizacion</text>
</svg>"""

if old_s25_diag in html:
    html = html.replace(old_s25_diag, new_s25_diag)
    print("✓ Replaced slide-25 diagram with brighter, larger version")
else:
    print("✗ Could not find exact slide-25 diagram to replace")


# 4. Enlarge diagram on slide 19 (which is slide-24 in HTML) - user requested "agrandalo como el de la slide 14"
# Currently it's height 370. Let's make it bigger using scale transform like the others.
old_s24_svg = '<svg height="370" style="overflow:visible;" viewbox="0 0 1180 260" width="100%">'
new_s24_svg = '<svg height="420" style="overflow:visible; transform:scale(1.15); transform-origin:top center;" viewbox="0 0 1180 260" width="100%">'
if old_s24_svg in html:
    html = html.replace(old_s24_svg, new_s24_svg)
    print("✓ Enlarged slide-24 diagram")


with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
