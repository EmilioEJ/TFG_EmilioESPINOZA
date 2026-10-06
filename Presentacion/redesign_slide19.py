#!/usr/bin/env python3
"""Redesign slide-19: move title/diagram up, make step-chips compact and beautiful."""

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find slide-19 start and end
start_marker = '<section class="slide" data-ch="5" id="slide-19">'
end_marker   = '<section class="slide" data-ch="5" id="slide-20">'

idx_start = html.find(start_marker)
idx_end   = html.find(end_marker)

if idx_start == -1 or idx_end == -1:
    print(f"ERROR: markers not found. start={idx_start}, end={idx_end}")
    exit(1)

new_slide = '''<section class="slide" data-ch="5" id="slide-19">
<div class="slide-inner" style="max-width:1300px;">
<h2 class="headline" style="max-width:40ch; margin-bottom:8px !important;">Arquitectura: Cliente-servidor totalmente desacoplado.</h2>
<div class="diag diag-large" data-anim="archflow" id="diagArch" style="margin-top:8px;">
<svg height="300" style="overflow:visible;" viewbox="0 0 1180 320" width="100%">
<defs>
<marker id="arrA" markerheight="7" markerwidth="7" orient="auto" refx="8" refy="5" viewbox="0 0 10 10"><path d="M0 0L10 5L0 10z" fill="var(--purple-500)"></path></marker>
<marker id="arrA2" markerheight="7" markerwidth="7" orient="auto" refx="8" refy="5" viewbox="0 0 10 10"><path d="M0 0L10 5L0 10z" fill="var(--orange-500)"></path></marker>
</defs>
<rect class="pop" fill="var(--paper-soft)" height="270" rx="14" stroke="var(--line)" stroke-dasharray="3 4" width="224" x="6" y="20"></rect>
<text fill="var(--purple-600)" font-family="IBM Plex Mono" font-size="10.5" x="22" y="40">01 · CLIENTE (navegador)</text>
<rect class="pop zone-box" fill="#fff" height="44" rx="9" stroke="var(--line-strong)" width="184" x="26" y="58"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="118" y="83">Interfaz de Usuario</text>
<rect class="pop zone-box" fill="#fff" height="46" id="boxCaptura" rx="9" stroke="var(--line-strong)" width="184" x="26" y="112"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="118" y="132">Módulo de Captura</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="118" y="148">micrófono + webcam</text>
<rect class="pop zone-box" fill="#fff" height="100" id="boxAvatar" rx="9" stroke="var(--line-strong)" width="184" x="26" y="168"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="118" y="205">Avatar 3D</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="118" y="222">WebGL — Three.js</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="118" y="237">Ready Player Me</text>
<path class="draw flow-arrow" d="M232 140 H 300" fill="none" id="arrToBackend" marker-end="url(#arrA)" stroke="var(--line-strong)" stroke-width="2.5"></path>
<path class="draw flow-arrow" d="M300 214 H 232" fill="none" id="arrToClient" marker-end="url(#arrA2)" stroke="var(--line-strong)" stroke-width="2.5"></path>
<text fill="var(--ink-faint)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="267" y="130">WebSocket</text>
<rect class="pop" fill="var(--purple-100)" height="270" rx="14" stroke="var(--purple-300)" stroke-dasharray="3 4" width="224" x="304" y="20"></rect>
<text fill="var(--purple-600)" font-family="IBM Plex Mono" font-size="10.5" x="320" y="40">02 · BACKEND — FastAPI</text>
<rect class="pop zone-box" fill="#fff" height="58" id="boxVision" rx="9" stroke="var(--purple-300)" width="184" x="324" y="68"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="416" y="93">Módulo de Visión</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="416" y="110">triggers de presencia</text>
<rect class="pop zone-box" fill="#fff" height="58" id="boxRAG" rx="9" stroke="var(--purple-300)" width="184" x="324" y="140"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="416" y="165">Gestor RAG</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="416" y="182">asyncio</text>
<path class="draw flow-arrow" d="M530 150 H 596" fill="none" id="arrToIA" marker-end="url(#arrA)" stroke="var(--line-strong)" stroke-width="2.5"></path>
<rect class="pop" fill="var(--purple-950)" height="270" rx="14" width="576" x="598" y="20"></rect>
<text fill="var(--orange-300)" font-family="IBM Plex Mono" font-size="10.5" x="614" y="40">03 · CAPA COGNITIVA — servicios IA</text>
<rect class="pop zone-box" fill="rgba(255,255,255,.05)" height="105" id="boxSTT" rx="10" stroke="rgba(255,255,255,.18)" width="260" x="618" y="60"></rect>
<text fill="#fff" font-family="IBM Plex Sans" font-size="12.5" font-weight="600" text-anchor="middle" x="748" y="100">Motor STT</text>
<text fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="748" y="118">Whisper-v3 (Groq)</text>
<text fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="748" y="134">audio → texto</text>
<g class="pop zone-box" id="boxChroma">
<ellipse cx="1028" cy="152" fill="var(--purple-700)" rx="128" ry="14"></ellipse>
<rect fill="var(--purple-700)" height="80" width="256" x="900" y="72"></rect>
<ellipse cx="1028" cy="72" fill="var(--purple-600)" rx="128" ry="14" stroke="rgba(255,255,255,.3)"></ellipse>
<text fill="#fff" font-family="IBM Plex Sans" font-size="12.5" font-weight="600" text-anchor="middle" x="1028" y="112">ChromaDB</text>
<text fill="rgba(255,255,255,.75)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="1028" y="130">base vectorial</text>
</g>
<rect class="pop zone-box" fill="rgba(255,255,255,.05)" height="98" id="boxLLM" rx="10" stroke="rgba(255,255,255,.18)" width="260" x="618" y="182"></rect>
<text fill="#fff" font-family="IBM Plex Sans" font-size="12.5" font-weight="600" text-anchor="middle" x="748" y="222">Motor LLM</text>
<text fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="748" y="240">Llama 3</text>
<text fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="748" y="256">contexto + query → respuesta</text>
<rect class="pop zone-box" fill="rgba(255,255,255,.05)" height="98" id="boxTTS" rx="10" stroke="rgba(255,255,255,.18)" width="256" x="900" y="182"></rect>
<text fill="#fff" font-family="IBM Plex Sans" font-size="12.5" font-weight="600" text-anchor="middle" x="1028" y="222">Motor TTS</text>
<text fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="1028" y="240">ElevenLabs</text>
<text fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="9.5" text-anchor="middle" x="1028" y="256">texto → audio + visemas</text>
</svg>
</div>

<!-- Redesigned compact step cards: 2 rows x 5 columns -->
<div class="stepper" id="stepperArch" style="margin-top:10px; display:grid; grid-template-columns:repeat(5,1fr); gap:6px;">

  <div class="step-chip" data-target="boxCaptura" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">1</span>
    <span>Rostro detectado → mic</span>
  </div>

  <div class="step-chip" data-target="arrToBackend" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">2</span>
    <span>Audio por WebSocket</span>
  </div>

  <div class="step-chip" data-target="boxSTT" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">3</span>
    <span>STT transcribe texto</span>
  </div>

  <div class="step-chip" data-target="boxRAG" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">4</span>
    <span>RAG recibe consulta</span>
  </div>

  <div class="step-chip" data-target="boxChroma" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--purple-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--purple-600); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">5</span>
    <span>Búsqueda ChromaDB</span>
  </div>

  <div class="step-chip" data-target="boxChroma boxLLM" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">6</span>
    <span>Fragmentos al LLM</span>
  </div>

  <div class="step-chip" data-target="boxLLM" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">7</span>
    <span>LLM genera respuesta</span>
  </div>

  <div class="step-chip" data-target="boxTTS" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">8</span>
    <span>TTS: audio + visemas</span>
  </div>

  <div class="step-chip" data-target="arrToClient" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">9</span>
    <span>Audio al cliente</span>
  </div>

  <div class="step-chip" data-target="boxAvatar" style="display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:10px; background:var(--paper-soft); border:1.5px solid var(--line); border-left:3px solid var(--orange-400); font-size:12px; line-height:1.3; cursor:pointer; transition:all 0.25s ease; min-height:0 !important;">
    <span style="display:inline-flex; align-items:center; justify-content:center; min-width:22px; height:22px; border-radius:50%; background:var(--orange-500); color:#fff; font-weight:700; font-size:11px; flex-shrink:0;">10</span>
    <span>Avatar lip-sync</span>
  </div>

</div>
</div>
</section>
'''

# Replace old slide-19 content
html = html[:idx_start] + new_slide + html[idx_end:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done. Slide-19 redesigned successfully.")
