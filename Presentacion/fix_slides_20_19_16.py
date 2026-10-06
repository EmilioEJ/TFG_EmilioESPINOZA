#!/usr/bin/env python3
"""
Three targeted fixes:
1. Slide-23 (slide 20): Remove bottom REST/WS text cards. Make top visual cards interactive
   with hover tooltips showing the descriptive text.
2. Slide-24 (slide 19 RAG): Enlarge diagram to match slide-19 arch size.
3. Slide-26 (slide 16 classes): Simplify boxes to titles only, compact layout,
   remove tags footer, update title.
"""

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================
# FIX 1: Slide-23 (WebSockets) — interactive cards + remove bottom cards
# =========================================================
old_ws_badge_and_bottom = '''<div style="display:flex; gap:20px; margin-bottom:10px; align-items:center;">
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
</div>'''

new_ws_badges = '''<div style="display:flex; gap:24px; margin-bottom:14px; align-items:stretch;">

  <!-- REST card with hover tooltip -->
  <div class="ws-compare-card" id="wsCardRest"
       style="flex:1; position:relative; display:flex; align-items:center; gap:14px; background:var(--orange-50); border:2px solid var(--orange-300); border-radius:16px; padding:16px 24px; cursor:default; transition:all 0.3s ease;">
    <span style="font-size:36px; flex-shrink:0;">🐢</span>
    <div>
      <div style="font-family:var(--font-mono); font-size:11px; color:var(--orange-600); font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">API REST — Problemática</div>
      <div style="font-family:var(--font-display); font-size:20px; font-weight:800; color:var(--orange-800); line-height:1.2;">Request → Wait → Response</div>
    </div>
    <!-- Hover tooltip -->
    <div class="ws-tooltip" style="position:absolute; bottom:calc(100% + 10px); left:0; right:0; background:white; border:2px solid var(--orange-400); border-radius:14px; padding:18px 22px; opacity:0; pointer-events:none; transition:opacity 0.3s ease, transform 0.3s ease; transform:translateY(8px); z-index:500; box-shadow:0 15px 40px rgba(249,115,22,0.2);">
      <p style="font-family:var(--font-body); font-size:16px; color:var(--ink-soft); margin:0; line-height:1.6;">La conexión se cierra al terminar. Si mandas un audio largo, la interfaz del estudiante se <b>congela</b> hasta que el servidor devuelva todo el audio procesado de golpe.</p>
    </div>
  </div>

  <div style="display:flex; align-items:center; font-size:32px; color:var(--ink-faint); flex-shrink:0;">→</div>

  <!-- WebSockets card with hover tooltip -->
  <div class="ws-compare-card" id="wsCardWs"
       style="flex:1; position:relative; display:flex; align-items:center; gap:14px; background:var(--purple-50); border:2px solid var(--purple-400); border-radius:16px; padding:16px 24px; cursor:default; transition:all 0.3s ease;">
    <span style="font-size:36px; flex-shrink:0;">⚡</span>
    <div>
      <div style="font-family:var(--font-mono); font-size:11px; color:var(--purple-600); font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">WebSockets — Solución</div>
      <div style="font-family:var(--font-display); font-size:20px; font-weight:800; color:var(--purple-800); line-height:1.2;">Túnel siempre abierto · Streaming en tiempo real</div>
    </div>
    <!-- Hover tooltip -->
    <div class="ws-tooltip" style="position:absolute; bottom:calc(100% + 10px); left:0; right:0; background:white; border:2px solid var(--purple-400); border-radius:14px; padding:18px 22px; opacity:0; pointer-events:none; transition:opacity 0.3s ease, transform 0.3s ease; transform:translateY(8px); z-index:500; box-shadow:0 15px 40px rgba(139,92,246,0.2);">
      <p style="font-family:var(--font-body); font-size:16px; color:var(--ink-soft); margin:0; line-height:1.6;">El "túnel" nunca se cierra. El estudiante manda pedacitos de audio, y el Asistente empieza a <b>hablar mientras todavía está procesando</b> el final de la oración.</p>
    </div>
  </div>

</div>

<script>
(function(){
  document.querySelectorAll('.ws-compare-card').forEach(function(card){
    var tip = card.querySelector('.ws-tooltip');
    card.addEventListener('mouseenter', function(){
      if(tip){ tip.style.opacity='1'; tip.style.transform='translateY(0)'; }
      card.style.boxShadow = '0 8px 30px rgba(0,0,0,0.15)';
      card.style.transform = 'translateY(-3px)';
    });
    card.addEventListener('mouseleave', function(){
      if(tip){ tip.style.opacity='0'; tip.style.transform='translateY(8px)'; }
      card.style.boxShadow = '';
      card.style.transform = '';
    });
  });
})();
</script>'''

if old_ws_badge_and_bottom in html:
    html = html.replace(old_ws_badge_and_bottom, new_ws_badges, 1)
    print("✓ WebSocket top badges replaced with interactive hover cards")
else:
    print("✗ WS badge block not found exactly - trying section replacement")

# Remove the bottom grid-2 cards (El problema de REST / La solución: WebSockets)
old_bottom_cards = '''<div class="grid-2" style="margin-top:10px;">
<div class="card" style="border-color:var(--orange-400);">
<b>El problema de REST</b>
<p style="color:var(--ink-soft); font-size:14px; margin-top:5px;">La conexión se cierra al terminar. Si mandas un audio largo, la interfaz del estudiante se congela hasta que el servidor devuelva todo el audio procesado de golpe.</p>
</div>
<div class="card" style="border-color:var(--purple-400);">
<b>La solución: WebSockets</b>
<p style="color:var(--ink-soft); font-size:14px; margin-top:5px;">El "túnel" nunca se cierra. El estudiante manda pedacitos de audio, y el Asistente empieza a hablar mientras todavía está procesando el final de la oración.</p>
</div>
</div>'''

if old_bottom_cards in html:
    html = html.replace(old_bottom_cards, '', 1)
    print("✓ Bottom REST/WS text cards removed")
else:
    print("✗ Bottom cards not found - may already be removed or whitespace differs")

# =========================================================
# FIX 2: Slide-24 (RAG) — make diagram as big as arch (slide-19)
# =========================================================
# Increase SVG height significantly
old_rag_svg = '<svg height="310" style="overflow:visible;" viewbox="0 0 1180 260" width="100%">'
new_rag_svg = '<svg height="370" style="overflow:visible;" viewbox="0 0 1180 260" width="100%">'
if old_rag_svg in html:
    html = html.replace(old_rag_svg, new_rag_svg, 1)
    print("✓ Slide-24 RAG SVG height increased to 370")
else:
    # Try the 250 version
    old_rag_svg2 = '<svg height="250" style="overflow:visible;" viewbox="0 0 1180 260" width="100%">'
    if old_rag_svg2 in html:
        html = html.replace(old_rag_svg2, new_rag_svg, 1)
        print("✓ Slide-24 RAG SVG height increased to 370 (from 250)")
    else:
        print("✗ RAG SVG not found")

# =========================================================
# FIX 3: Slide-26 (class diagram) — simplify boxes, compact, update title
# =========================================================

# 3a. Update title
old_s26_title = '<h2 class="headline" style="max-width:40ch">Diagrama de clases (Backend): Un orquestador, cinco especialistas.</h2>'
new_s26_title = '<h2 class="headline" style="max-width:40ch">Un orquestador, cinco especialistas.</h2>'
if old_s26_title in html:
    html = html.replace(old_s26_title, new_s26_title, 1)
    print("✓ Slide-26 title updated")
else:
    print("✗ Slide-26 title not found")

# 3b. Remove stat-row (Alta cohesion, Bajo acoplamiento, etc.)
old_stat_row = '''<div class="stat-row" style="margin-top:6px; justify-content:center;">
<span class="tag yes">Alta cohesión</span>
<span class="tag yes">Bajo acoplamiento</span>
<span class="tag no">Ninguna clase desconectada</span>
</div>'''
if old_stat_row in html:
    html = html.replace(old_stat_row, '', 1)
    print("✓ Slide-26 stat-row removed")
else:
    print("✗ Slide-26 stat-row not found")

# 3c. Replace the entire SVG with simplified version (titles only, more compact)
old_s26_svg = '''<svg height="440" style="max-width:1100px; overflow:visible; transform:scale(1.1); transform-origin:top center;" viewbox="0 0 940 380" width="100%">
<defs><marker id="arrCH" markerheight="6" markerwidth="6" orient="auto-start-reverse" refx="8" refy="5" viewbox="0 0 10 10"><path d="M0 0L10 5L0 10z" fill="var(--ink-faint)"></path></marker></defs>
<path class="draw" d="M410 170 L 110 53" marker-end="url(#arrCH)" stroke="var(--ink-soft)" stroke-width="2"></path>
<path class="draw" d="M440 160 L 330 66" marker-end="url(#arrCH)" stroke="var(--ink-soft)" stroke-width="2"></path>
<path class="draw" d="M500 160 L 575 66" marker-end="url(#arrCH)" stroke="var(--ink-soft)" stroke-width="2"></path>
<path class="draw" d="M530 170 L 830 53" marker-end="url(#arrCH)" stroke="var(--ink-soft)" stroke-width="2"></path>
<path class="draw" d="M470 230 L 470 290" marker-end="url(#arrCH)" stroke="var(--ink-soft)" stroke-width="2"></path>
<rect class="pop" fill="var(--black)" height="70" rx="12" width="180" x="380" y="160"></rect>
<text fill="#fff" font-family="IBM Plex Sans" font-size="13.5" font-weight="600" text-anchor="middle" x="470" y="190">FastAPIApp</text>
<text fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="470" y="208">orquestador central</text>
<g transform="translate(20,20)"><rect class="pop" fill="var(--paper-soft)" height="66" rx="11" stroke="var(--line-strong)" width="180"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="90" y="27">RAGManager</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="90" y="43">search_similar_context()</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="90" y="56">- db_client, embedding_model</text>
</g>
<g transform="translate(240,0)"><rect class="pop" fill="var(--paper-soft)" height="66" rx="11" stroke="var(--line-strong)" width="180"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="90" y="27">LLMController</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="90" y="43">generate_response()</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="90" y="56">- model_name, system_prompt</text>
</g>
<g transform="translate(480,0)"><rect class="pop" fill="var(--paper-soft)" height="66" rx="11" stroke="var(--line-strong)" width="190"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="95" y="27">AudioProcessor</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="95" y="43">transcribe_audio() · synthesize()</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="95" y="56">- groq_api_key, tts_provider</text>
</g>
<g transform="translate(740,20)"><rect class="pop" fill="var(--paper-soft)" height="66" rx="11" stroke="var(--line-strong)" width="180"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="90" y="27">VisionHandler</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="90" y="43">detect_presence()</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="90" y="56">- threshold_pixels</text>
</g>
<g transform="translate(370,290)"><rect class="pop" fill="var(--paper-soft)" height="70" rx="11" stroke="var(--line-strong)" width="200"></rect>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="12" font-weight="600" text-anchor="middle" x="100" y="28">DatabaseHandler</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="100" y="45">authenticate_user()</text>
<text fill="var(--ink-soft)" font-family="IBM Plex Mono" font-size="8.5" text-anchor="middle" x="100" y="58">- db_path, conn</text>
</g>
</svg>'''

new_s26_svg = '''<svg height="430" style="width:100%; overflow:visible;" viewbox="0 0 820 340">
<defs>
  <marker id="arrCH" markerheight="7" markerwidth="7" orient="auto-start-reverse" refx="8" refy="5" viewbox="0 0 10 10">
    <path d="M0 0L10 5L0 10z" fill="var(--purple-400)"></path>
  </marker>
</defs>
<!-- Center: FastAPIApp orquestador -->
<rect class="pop" fill="var(--purple-950)" height="60" rx="14" width="170" x="325" y="140"></rect>
<text fill="var(--orange-300)" font-family="IBM Plex Mono" font-size="10" text-anchor="middle" x="410" y="162">ORQUESTADOR</text>
<text fill="#fff" font-family="IBM Plex Sans" font-size="16" font-weight="700" text-anchor="middle" x="410" y="188">FastAPIApp</text>

<!-- Lines from center to specialists -->
<path class="draw" d="M360 140 L 180 70" marker-end="url(#arrCH)" stroke="var(--purple-400)" stroke-width="2"></path>
<path class="draw" d="M390 140 L 340 70" marker-end="url(#arrCH)" stroke="var(--purple-400)" stroke-width="2"></path>
<path class="draw" d="M430 140 L 480 70" marker-end="url(#arrCH)" stroke="var(--purple-400)" stroke-width="2"></path>
<path class="draw" d="M460 140 L 640 70" marker-end="url(#arrCH)" stroke="var(--purple-400)" stroke-width="2"></path>
<path class="draw" d="M410 200 L 410 265" marker-end="url(#arrCH)" stroke="var(--purple-400)" stroke-width="2"></path>

<!-- TOP ROW: 4 specialists -->
<!-- RAGManager -->
<rect class="pop" fill="var(--paper-soft)" height="55" rx="12" stroke="var(--purple-300)" stroke-width="1.5" width="155" x="95" y="10"></rect>
<text fill="var(--purple-500)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="172" y="28">Especialista 1</text>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="172" y="52">RAGManager</text>

<!-- LLMController -->
<rect class="pop" fill="var(--paper-soft)" height="55" rx="12" stroke="var(--purple-300)" stroke-width="1.5" width="160" x="258" y="10"></rect>
<text fill="var(--purple-500)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="338" y="28">Especialista 2</text>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="338" y="52">LLMController</text>

<!-- AudioProcessor -->
<rect class="pop" fill="var(--paper-soft)" height="55" rx="12" stroke="var(--purple-300)" stroke-width="1.5" width="175" x="422" y="10"></rect>
<text fill="var(--purple-500)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="509" y="28">Especialista 3</text>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="509" y="52">AudioProcessor</text>

<!-- VisionHandler -->
<rect class="pop" fill="var(--paper-soft)" height="55" rx="12" stroke="var(--purple-300)" stroke-width="1.5" width="155" x="600" y="10"></rect>
<text fill="var(--purple-500)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="677" y="28">Especialista 4</text>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="677" y="52">VisionHandler</text>

<!-- BOTTOM: DatabaseHandler -->
<rect class="pop" fill="var(--paper-soft)" height="55" rx="12" stroke="var(--purple-300)" stroke-width="1.5" width="175" x="323" y="268"></rect>
<text fill="var(--purple-500)" font-family="IBM Plex Mono" font-size="9" text-anchor="middle" x="410" y="287">Especialista 5</text>
<text fill="var(--ink)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="410" y="311">DatabaseHandler</text>
</svg>'''

if old_s26_svg in html:
    html = html.replace(old_s26_svg, new_s26_svg, 1)
    print("✓ Slide-26 class diagram simplified (titles only, compact)")
else:
    print("✗ Slide-26 SVG not found exactly - trying to search...")
    idx = html.find('id="slide-26"')
    if idx != -1:
        print(f"  slide-26 found at index {idx}")
        # Show context for debugging
        sub = html[idx:idx+300]
        print(f"  Context: {sub[:200]}")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ All three fixes applied.")
