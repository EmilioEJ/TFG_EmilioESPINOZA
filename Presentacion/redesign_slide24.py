#!/usr/bin/env python3
"""Apply same improvements to slide-24 (RAG engine, presentation slide 19):
- Title/diagram moved up (reduced margins)
- stepperRag chips redesigned as compact horizontal cards with numbered badges
"""

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '</section><section class="slide" data-ch="5" id="slide-24">'
end_marker   = '<section class="slide" data-ch="5" id="slide-23">'

idx_start = html.find(start_marker)
idx_end   = html.find(end_marker)

if idx_start == -1 or idx_end == -1:
    print(f"ERROR: markers not found. start={idx_start}, end={idx_end}")
    # Try alternate start
    start_marker2 = '<section class="slide" data-ch="5" id="slide-24">'
    idx_start2 = html.find(start_marker2)
    print(f"Alternate start: {idx_start2}")
    exit(1)

# We want to replace from </section><section id="slide-24"> up to the next section
# Keep the leading </section> closing the previous slide
new_slide = '''</section>
<section class="slide" data-ch="5" id="slide-24">
<div class="slide-inner" style="max-width:1300px;">
<h2 class="headline" style="max-width:40ch; margin-bottom:8px !important;">El motor cognitivo (RAG): El flujo obligatorio del conocimiento.</h2>
<div class="diag diag-large" data-anim="ragflow" id="diagRagFlow" style="margin-top:8px;">
<svg height="250" style="overflow:visible;" viewbox="0 0 1180 260" width="100%">
<defs><marker id="arrRF" markerheight="7" markerwidth="7" orient="auto" refx="8" refy="5" viewbox="0 0 10 10"><path d="M0 0L10 5L0 10z" fill="var(--purple-500)"></path></marker></defs>
<text fill="var(--purple-600)" font-family="IBM Plex Mono" font-size="10.5" x="0" y="24">INGESTA — proceso batch / offline</text>
<rect class="pop rf-box" fill="var(--paper-soft)" height="60" id="ing1" rx="10" stroke="var(--line-strong)" width="180" x="0" y="36"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="11.5" font-weight="600" text-anchor="middle" x="90" y="60">Documentos PDF</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="90" y="77">mallas · reglamentos</text>
<path d="M182 66 H 216" marker-end="url(#arrRF)" stroke="var(--line-strong)" stroke-width="2"></path>
<rect class="pop rf-box" fill="var(--paper-soft)" height="60" id="ing2" rx="10" stroke="var(--line-strong)" width="200" x="220" y="36"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="11.5" font-weight="600" text-anchor="middle" x="320" y="58">Extracción a Markdown</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="320" y="76">pymupdf4llm</text>
<path d="M422 66 H 456" marker-end="url(#arrRF)" stroke="var(--line-strong)" stroke-width="2"></path>
<rect class="pop rf-box" fill="var(--paper-soft)" height="60" id="ing3" rx="10" stroke="var(--line-strong)" width="200" x="460" y="36"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="11.5" font-weight="600" text-anchor="middle" x="560" y="58">División en Chunks</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="560" y="76">MarkdownTextSplitter</text>
<path d="M662 66 H 696" marker-end="url(#arrRF)" stroke="var(--line-strong)" stroke-width="2"></path>
<rect class="pop rf-box" fill="var(--paper-soft)" height="60" id="ing4" rx="10" stroke="var(--line-strong)" width="200" x="700" y="36"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="11.5" font-weight="600" text-anchor="middle" x="800" y="58">Vectorización</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="800" y="76">SentenceTransformer</text>
<path d="M902 66 C 940 66, 960 90, 972 108" fill="none" marker-end="url(#arrRF)" stroke="var(--purple-400)" stroke-width="2.2"></path>
<g class="pop zone-box" id="dbCyl">
<ellipse cx="1080" cy="160" fill="var(--purple-700)" rx="95" ry="13"></ellipse>
<rect fill="var(--purple-700)" height="90" width="190" x="985" y="70"></rect>
<ellipse cx="1080" cy="70" fill="var(--purple-600)" rx="95" ry="13"></ellipse>
<text fill="#fff" font-family="IBM Plex Sans" font-size="12.5" font-weight="600" text-anchor="middle" x="1080" y="112">ChromaDB</text>
<text fill="rgba(255,255,255,.7)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="1080" y="130">colección vectorial</text>
</g>
<text fill="var(--orange-600)" font-family="IBM Plex Mono" font-size="10.5" x="0" y="185">CONSULTA — tiempo real</text>
<rect class="pop rf-box" fill="var(--orange-100)" height="56" id="q1" rx="10" stroke="var(--orange-300)" width="180" x="0" y="197"></rect>
<text fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="11.5" font-weight="600" text-anchor="middle" x="90" y="220">Pregunta del usuario</text>
<text fill="var(--orange-700)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="90" y="236">texto transcrito</text>
<path d="M182 225 H 216" marker-end="url(#arrRF)" stroke="var(--orange-400)" stroke-width="2"></path>
<rect class="pop rf-box" fill="var(--orange-100)" height="56" id="q2" rx="10" stroke="var(--orange-300)" width="200" x="220" y="197"></rect>
<text fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="11.5" font-weight="600" text-anchor="middle" x="320" y="220">Vectorización</text>
<text fill="var(--orange-700)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="320" y="236">de la consulta</text>
<path d="M422 225 H 456" marker-end="url(#arrRF)" stroke="var(--orange-400)" stroke-width="2"></path>
<rect class="pop rf-box" fill="var(--orange-100)" height="56" id="q3" rx="10" stroke="var(--orange-300)" width="200" x="460" y="197"></rect>
<text fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="11.5" font-weight="600" text-anchor="middle" x="560" y="217">Similitud del coseno</text>
<text fill="var(--orange-700)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="560" y="234">consulta k-chunks</text>
<path d="M660 215 C 780 190, 880 170, 972 130" fill="none" marker-end="url(#arrRF)" stroke="var(--orange-400)" stroke-dasharray="5 4" stroke-width="2.2"></path>
</svg>
</div>

<!-- Redesigned compact step cards: 1 row x 7 columns (4 purple + 3 orange) -->
<div class="stepper" id="stepperRag" style="margin-top:10px; display:grid; grid-template-columns:repeat(7,1fr); gap:6px;">

  <div class="step-chip" data-target="ing1" style="display:flex; align-items:center; gap:7px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">1</span>
    <span>PDFs institucionales</span>
  </div>

  <div class="step-chip" data-target="ing2" style="display:flex; align-items:center; gap:7px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">2</span>
    <span>Extracción a Markdown</span>
  </div>

  <div class="step-chip" data-target="ing3" style="display:flex; align-items:center; gap:7px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">3</span>
    <span>Chunks de 1500 car.</span>
  </div>

  <div class="step-chip" data-target="ing4 dbCyl" style="display:flex; align-items:center; gap:7px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">4</span>
    <span>Vector → ChromaDB</span>
  </div>

  <div class="step-chip" data-target="q1" style="display:flex; align-items:center; gap:7px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">5</span>
    <span>Llega la pregunta</span>
  </div>

  <div class="step-chip" data-target="q2" style="display:flex; align-items:center; gap:7px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">6</span>
    <span>Vectoriza consulta</span>
  </div>

  <div class="step-chip" data-target="q3 dbCyl" style="display:flex; align-items:center; gap:7px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">7</span>
    <span>Coseno → contexto LLM</span>
  </div>

</div>
</div>
</section>
'''

html = html[:idx_start] + new_slide + html[idx_end:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done. Slide-24 (RAG engine, slide 19) redesigned successfully.")
