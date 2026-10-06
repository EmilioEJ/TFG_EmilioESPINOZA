import re

def fix_all():
    path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # =====================================================
    # 1. FIX PAGE NUMBERS: The second ::after overrides the first one.
    #    Remove the first counter/::after block (lines ~394-410) since lines 470-493 handle it.
    # =====================================================
    html = html.replace(
        """/* Slide Enumeration */
body { counter-reset: slideCounter; }
.slide { counter-increment: slideCounter; }
.slide::after {
  content: counter(slideCounter);
  position: absolute;
  top: 40px;
  right: 50px;
  font-size: 20px;
  font-weight: 700;
  color: var(--ink-faint);
  font-family: var(--font-mono);
  opacity: 0.6;
}
.slide.cover::after {
  display: none;
}""",
        "/* Slide Enumeration - moved to SLIDE NUMBER RECTANGLES section */"
    )

    # =====================================================
    # 2. FIX: Remove the global .diag:hover scale that was interfering
    #    and replace with per-box hover effects
    # =====================================================
    html = html.replace(
        """.diag:hover {
  transform: scale(1.02);
  box-shadow: 0 20px 40px rgba(0,0,0,0.08);
}""",
        """/* Individual box hover effects instead of whole diagram */
.zone-box:hover, .rf-box:hover {
  filter: drop-shadow(0 0 12px rgba(98,36,184,0.4)) !important;
  stroke: var(--orange-500) !important;
  cursor: pointer;
}
.zone-box { transition: filter 0.3s ease, stroke 0.3s ease; }
.rf-box { transition: filter 0.3s ease, stroke 0.3s ease; }
.step-chip:hover {
  opacity: 1 !important;
  border-left-color: var(--orange-500) !important;
  background: var(--orange-100) !important;
  transform: scale(1.05);
  cursor: pointer;
}"""
    )

    # Also remove the BATCH 4 transform that scales ALL svg inside .diag
    html = html.replace(
        """    /* BATCH 4 CSS */
    .diag svg, .diag img {
        transform: scale(1.15);
        transform-origin: center center;
        transition: transform 0.3s ease;
    }
    /* Let's prevent massive overflow */
    .diag {
        padding: 20px;
    }""",
        """    /* BATCH 4 CSS - cleaned up */
    .diag {
        padding: 10px;
    }"""
    )

    # =====================================================
    # 3. FIX SLIDE 21 (Avatar States): The viewBox is too big (460x460)
    #    causing circles to overflow. Let me use a bigger viewBox and
    #    center everything properly. The circles have r=56-58 which is huge.
    # =====================================================
    old_slide21 = re.search(r'(<section class="slide"[^>]*id="slide-21"[^>]*>)(.*?)(</section>)', html, re.DOTALL)
    if old_slide21:
        new_slide21 = """
  <div class="slide-inner" style="display:flex; flex-direction:column; align-items:center;">
    <h2 class="headline" style="text-align:center;">El ciclo de vida del avatar</h2>
    <p class="subhead" style="text-align:center; margin-bottom:10px;">Pasa el cursor sobre cada estado para ver su explicación.</p>
    <div class="avatar-states-container" style="position:relative; width:100%; max-width:600px; margin:0 auto;">
      <div class="diag" id="diagStates" data-anim="avatarstates">
        <svg viewBox="-20 -20 520 520" width="100%" style="overflow:visible; max-height:55vh;">
          <defs><marker id="arrSt2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--ink-faint)"/></marker></defs>
          <path class="draw" d="M175 70 A 140 140 0 0 1 350 155" stroke="var(--line-strong)" stroke-width="2" fill="none" marker-end="url(#arrSt2)"/>
          <text x="290" y="72" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">presencia detectada</text>
          <path class="draw" d="M375 205 A 140 140 0 0 1 325 365" stroke="var(--line-strong)" stroke-width="2" fill="none" marker-end="url(#arrSt2)"/>
          <text x="365" y="290" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">silencio detectado</text>
          <path class="draw" d="M260 400 A 140 140 0 0 1 110 340" stroke="var(--line-strong)" stroke-width="2" fill="none" marker-end="url(#arrSt2)"/>
          <text x="155" y="400" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">TTFB completado</text>
          <path class="draw" d="M85 290 A 140 140 0 0 1 95 130" stroke="var(--orange-400)" stroke-width="2" fill="none" marker-end="url(#arrSt2)" stroke-dasharray="5 4"/>
          <text x="15" y="220" font-family="IBM Plex Mono" font-size="10" fill="var(--orange-600)">fin de audio</text>
          <path class="draw" d="M140 100 A 140 140 0 0 0 95 290" stroke="var(--ink-faint)" stroke-width="1.5" fill="none" marker-end="url(#arrSt2)" stroke-dasharray="2 4" opacity=".6"/>
          <text x="48" y="195" font-family="IBM Plex Mono" font-size="9" fill="var(--ink-faint)">timeout</text>
          <g class="state-node pop" id="stDormido2" data-state="0" data-tooltip="IDLE: El avatar realiza animaciones sutiles (respirar, parpadear) mientras espera detectar un rostro." transform="translate(130,60)" style="cursor:pointer;">
            <circle r="46" fill="#fff" stroke="var(--line-strong)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="14" fill="var(--ink)">Dormido</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">idle</text>
          </g>
          <g class="state-node pop" id="stEscuchando2" data-state="1" data-tooltip="LISTENING: Se activa el micrófono. El avatar asiente y mantiene contacto visual simulado." transform="translate(380,180)" style="cursor:pointer;">
            <circle r="48" fill="#fff" stroke="var(--purple-300)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="14" fill="var(--ink)">Escuchando</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">listening</text>
          </g>
          <g class="state-node pop" id="stPensando2" data-state="2" data-tooltip="THINKING: Mientras el RAG y LLM procesan, el avatar mira hacia arriba/lados, indicando procesamiento." transform="translate(300,390)" style="cursor:pointer;">
            <circle r="48" fill="#fff" stroke="var(--purple-300)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="14" fill="var(--ink)">Pensando</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">processing</text>
          </g>
          <g class="state-node pop" id="stHablando2" data-state="3" data-tooltip="TALKING: Reproduce el audio sintetizado sincronizando los visemas (movimiento labial) con el texto." transform="translate(80,340)" style="cursor:pointer;">
            <circle r="48" fill="#fff" stroke="var(--orange-300)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="14" fill="var(--ink)">Hablando</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">speaking</text>
          </g>
        </svg>
      </div>
      <div id="stateTooltip" style="position:absolute; bottom:-80px; left:50%; transform:translateX(-50%); background:var(--purple-50); border:2px solid var(--purple-200); border-radius:12px; padding:16px 24px; font-size:18px; color:var(--ink); text-align:center; width:90%; opacity:0; transition:opacity 0.3s ease; pointer-events:none;">
        Pasa el cursor sobre un estado...
      </div>
    </div>
  </div>
"""
        html = html[:old_slide21.start(2)] + new_slide21 + html[old_slide21.end(2):]

    # =====================================================
    # 4. RESTORE SEQUENCE DIAGRAM from original file
    # =====================================================
    old_slide27 = re.search(r'(<section class="slide"[^>]*id="slide-27"[^>]*>)(.*?)(</section>)', html, re.DOTALL)
    if old_slide27:
        new_slide27 = """
  <div class="slide-inner" style="max-width:1300px;">
    <h2 class="headline" style="max-width:50ch">Diagrama de secuencia: La orquestación en tiempo real</h2>
    <div class="diag" id="diagSequence" data-anim="sequence" style="margin-top:16px;">
      <svg viewBox="0 0 1180 520" width="100%" height="400" style="overflow:visible;">
        <defs>
        <marker id="arrSeqP" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--purple-500)"/></marker>
        <marker id="arrSeqO" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--orange-500)"/></marker>
        </defs>
        <rect x="2" y="8" width="116" height="34" rx="8" fill="var(--paper-soft)" stroke="var(--line-strong)" class="pop"/>
        <text x="60" y="30" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="12" fill="var(--ink)">Estudiante</text>
        <line class="draw" x1="60" y1="42" x2="60" y2="516" stroke="var(--line)" stroke-width="1.5"/>
        <rect x="167" y="8" width="116" height="34" rx="8" fill="var(--paper-soft)" stroke="var(--line-strong)" class="pop"/>
        <text x="225" y="30" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="12" fill="var(--ink)">Frontend</text>
        <line class="draw" x1="225" y1="42" x2="225" y2="516" stroke="var(--line)" stroke-width="1.5"/>
        <rect x="362" y="8" width="116" height="34" rx="8" fill="var(--paper-soft)" stroke="var(--line-strong)" class="pop"/>
        <text x="420" y="30" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="12" fill="var(--ink)">Backend</text>
        <line class="draw" x1="420" y1="42" x2="420" y2="516" stroke="var(--line)" stroke-width="1.5"/>
        <rect x="557" y="8" width="116" height="34" rx="8" fill="var(--paper-soft)" stroke="var(--line-strong)" class="pop"/>
        <text x="615" y="30" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="12" fill="var(--ink)">Groq (STT)</text>
        <line class="draw" x1="615" y1="42" x2="615" y2="516" stroke="var(--line)" stroke-width="1.5"/>
        <rect x="727" y="8" width="116" height="34" rx="8" fill="var(--paper-soft)" stroke="var(--line-strong)" class="pop"/>
        <text x="785" y="30" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="12" fill="var(--ink)">ChromaDB</text>
        <line class="draw" x1="785" y1="42" x2="785" y2="516" stroke="var(--line)" stroke-width="1.5"/>
        <rect x="887" y="8" width="116" height="34" rx="8" fill="var(--paper-soft)" stroke="var(--line-strong)" class="pop"/>
        <text x="945" y="30" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="12" fill="var(--ink)">LLM</text>
        <line class="draw" x1="945" y1="42" x2="945" y2="516" stroke="var(--line)" stroke-width="1.5"/>
        <rect x="1052" y="8" width="116" height="34" rx="8" fill="var(--paper-soft)" stroke="var(--line-strong)" class="pop"/>
        <text x="1110" y="30" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="12" fill="var(--ink)">ElevenLabs</text>
        <line class="draw" x1="1110" y1="42" x2="1110" y2="516" stroke="var(--line)" stroke-width="1.5"/>
        <g class="seq-msg" id="msg1"><path d="M 60 70 H 225" stroke="var(--purple-400)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqP)"/><text x="142.5" y="64" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">1. Se acerca a la cámara</text></g>
        <g class="seq-msg" id="msg2"><path d="M 225 100 H 420" stroke="var(--purple-400)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqP)"/><text x="322.5" y="94" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">2. Frame por WebSockets</text></g>
        <g class="seq-msg" id="msg3"><path d="M 420 130 H 225" stroke="var(--orange-500)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqO)"/><text x="322.5" y="124" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">3. PRESENCIA_DETECTADA</text></g>
        <g class="seq-msg" id="msg4"><path d="M 225 165 C 295 159, 295 181, 225 181" stroke="var(--purple-400)" stroke-width="2" fill="none" marker-end="url(#arrSeqP)"/><text x="303" y="159" text-anchor="start" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">4. Activa micrófono</text></g>
        <g class="seq-msg" id="msg5"><path d="M 225 198 H 420" stroke="var(--purple-400)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqP)"/><text x="322.5" y="192" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">5. Envía blob de audio</text></g>
        <g class="seq-msg" id="msg6"><path d="M 420 228 H 615" stroke="var(--purple-400)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqP)"/><text x="517.5" y="222" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">6. Audio para STT</text></g>
        <g class="seq-msg" id="msg7"><path d="M 615 258 H 420" stroke="var(--orange-500)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqO)"/><text x="517.5" y="252" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">7. Retorna texto (query)</text></g>
        <g class="seq-msg" id="msg8"><path d="M 420 288 H 785" stroke="var(--purple-400)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqP)"/><text x="602.5" y="282" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">8. Busca contexto semántico</text></g>
        <g class="seq-msg" id="msg9"><path d="M 785 318 H 420" stroke="var(--orange-500)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqO)"/><text x="602.5" y="312" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">9. Retorna chunks (hit rate)</text></g>
        <g class="seq-msg" id="msg10"><path d="M 420 348 H 945" stroke="var(--purple-400)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqP)"/><text x="682.5" y="342" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">10. Prompt + contexto + query</text></g>
        <g class="seq-msg" id="msg11"><path d="M 945 378 H 420" stroke="var(--orange-500)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqO)"/><text x="682.5" y="372" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">11. Genera respuesta textual</text></g>
        <g class="seq-msg" id="msg12"><path d="M 420 408 H 1110" stroke="var(--purple-400)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqP)"/><text x="765.0" y="402" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">12. Texto para TTS</text></g>
        <g class="seq-msg" id="msg13"><path d="M 1110 438 H 420" stroke="var(--orange-500)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqO)"/><text x="765.0" y="432" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">13. Retorna chunk de audio</text></g>
        <g class="seq-msg" id="msg14"><path d="M 420 468 H 225" stroke="var(--orange-500)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqO)"/><text x="322.5" y="462" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">14. Audio en Base64</text></g>
        <g class="seq-msg" id="msg15"><path d="M 225 498 H 60" stroke="var(--orange-500)" stroke-width="2.2" fill="none" marker-end="url(#arrSeqO)"/><text x="142.5" y="492" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="var(--ink-soft)">15. Reproduce + lip-sync</text></g>
      </svg>
      <div class="stepper" id="stepperSeq" style="margin-top:0; display:grid; grid-template-columns:repeat(5,1fr); gap:6px;">
        <div class="step-chip small" data-target="msg1"><span class="step-chip-n">1</span>Se acerca a la cámara</div>
        <div class="step-chip small" data-target="msg2"><span class="step-chip-n">2</span>Frame por WebSockets</div>
        <div class="step-chip small" data-target="msg3"><span class="step-chip-n">3</span>PRESENCIA_DETECTADA</div>
        <div class="step-chip small" data-target="msg4"><span class="step-chip-n">4</span>Activa micrófono</div>
        <div class="step-chip small" data-target="msg5"><span class="step-chip-n">5</span>Envía blob de audio</div>
        <div class="step-chip small" data-target="msg6"><span class="step-chip-n">6</span>Audio para STT</div>
        <div class="step-chip small" data-target="msg7"><span class="step-chip-n">7</span>Retorna texto (query)</div>
        <div class="step-chip small" data-target="msg8"><span class="step-chip-n">8</span>Busca contexto semántico</div>
        <div class="step-chip small" data-target="msg9"><span class="step-chip-n">9</span>Retorna chunks (hit rate)</div>
        <div class="step-chip small" data-target="msg10"><span class="step-chip-n">10</span>Prompt + contexto + query</div>
        <div class="step-chip small" data-target="msg11"><span class="step-chip-n">11</span>Genera respuesta textual</div>
        <div class="step-chip small" data-target="msg12"><span class="step-chip-n">12</span>Texto para TTS</div>
        <div class="step-chip small" data-target="msg13"><span class="step-chip-n">13</span>Retorna chunk de audio</div>
        <div class="step-chip small" data-target="msg14"><span class="step-chip-n">14</span>Audio en Base64</div>
        <div class="step-chip small" data-target="msg15"><span class="step-chip-n">15</span>Reproduce + lip-sync</div>
      </div>
    </div>
  </div>
"""
        html = html[:old_slide27.start(2)] + new_slide27 + html[old_slide27.end(2):]

    # =====================================================
    # 5. FIX SLIDE 18 (Vision Artificial) - Make both cards hover-reveal, compact layout
    # =====================================================
    old_slide22 = re.search(r'(<section class="slide"[^>]*id="slide-22"[^>]*>)(.*?)(</section>)', html, re.DOTALL)
    if old_slide22:
        new_slide22 = """
  <div class="slide-inner">
    <h2 class="headline" style="max-width:50ch">Visión artificial: Detección rápida y optimizada</h2>
    <p class="subhead" style="margin-bottom: 30px;">Pasa el cursor sobre cada tarjeta para ver los detalles.</p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
      <div class="interactive-card hover-reveal" style="padding: 30px;">
        <div style="display:flex; align-items:center; gap:20px;">
          <div class="icon-box">⚠️</div>
          <h3 style="color: var(--purple-900); font-size: 22px;">Idea inicial descartada</h3>
        </div>
        <p style="font-size: 18px;">La idea inicial —redes profundas de reconocimiento facial— consumía CPU/GPU en exceso y no era viable para un kiosco universitario.</p>
      </div>
      <div class="interactive-card hover-reveal" style="padding: 30px;">
        <div style="display:flex; align-items:center; gap:20px;">
          <div class="icon-box" style="background:var(--purple-100); color:var(--purple-600);">✅</div>
          <h3 style="color: var(--purple-900); font-size: 22px;">Solución: Bounding Box ligero</h3>
        </div>
        <p style="font-size: 18px;">El sistema detecta el área del rostro en píxeles con TensorFlow.js y MediaPipe. Si supera un umbral de proximidad, asume intención de interactuar y "despierta" al avatar — eficiencia computacional extrema.</p>
      </div>
    </div>
  </div>
"""
        html = html[:old_slide22.start(2)] + new_slide22 + html[old_slide22.end(2):]

    # =====================================================
    # 6. SLIDE 9 (Justificación) - Make it more creative
    # =====================================================
    old_slide_just = re.search(r'(<section class="slide"[^>]*id="slide-10"[^>]*>)(.*?)(</section>)', html, re.DOTALL)
    if old_slide_just:
        new_slide_just = """
  <div class="slide-inner">
    <h2 class="headline" style="max-width:50ch;">¿Por qué vale la pena este desarrollo?</h2>
    <p class="subhead" style="margin-bottom:30px;">Tres razones que conectan lo técnico con lo institucional. Pasa el cursor para profundizar.</p>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:24px;">
      <div class="interactive-card hover-reveal" style="padding:30px; border-left:5px solid var(--purple-600);">
        <div style="font-size:60px; text-align:center; margin-bottom:15px;">🚀</div>
        <h3 style="color:var(--purple-900); font-size:22px; text-align:center;">Innovación educativa</h3>
        <p style="font-size:18px; text-align:center;">Posiciona a la carrera a la vanguardia tecnológica, usando IA generativa de forma ética y aplicada.</p>
      </div>
      <div class="interactive-card hover-reveal" style="padding:30px; border-left:5px solid var(--orange-500);">
        <div style="font-size:60px; text-align:center; margin-bottom:15px;">⚡</div>
        <h3 style="color:var(--purple-900); font-size:22px; text-align:center;">Eficiencia operativa</h3>
        <p style="font-size:18px; text-align:center;">Libera horas de trabajo administrativo en las secretarías, automatizando consultas repetitivas.</p>
      </div>
      <div class="interactive-card hover-reveal" style="padding:30px; border-left:5px solid var(--purple-400);">
        <div style="font-size:60px; text-align:center; margin-bottom:15px;">🌐</div>
        <h3 style="color:var(--purple-900); font-size:22px; text-align:center;">Accesibilidad</h3>
        <p style="font-size:18px; text-align:center;">Transforma documentos densos de 50 páginas en respuestas conversacionales, inmediatas y en español natural.</p>
      </div>
    </div>
  </div>
"""
        html = html[:old_slide_just.start(2)] + new_slide_just + html[old_slide_just.end(2):]

    # =====================================================
    # 7. Add step-chip hover interactivity via JS
    # =====================================================
    js_chip_hover = """
  // Step-chip hover: highlight target elements on mouseover
  document.querySelectorAll('.step-chip').forEach(function(chip){
    chip.addEventListener('mouseenter', function(){
      var targets = (this.getAttribute('data-target')||'').split(/\\s+/).filter(Boolean);
      targets.forEach(function(tid){
        var el = document.getElementById(tid);
        if(el){ el.classList.add('tgt-active'); }
      });
      this.classList.add('is-active');
    });
    chip.addEventListener('mouseleave', function(){
      var targets = (this.getAttribute('data-target')||'').split(/\\s+/).filter(Boolean);
      targets.forEach(function(tid){
        var el = document.getElementById(tid);
        if(el){ el.classList.remove('tgt-active'); }
      });
      this.classList.remove('is-active');
    });
  });
"""
    # Check if we already added it
    if 'Step-chip hover' not in html:
        html = html.replace('runDiagrams(slides[0]);', 'runDiagrams(slides[0]);\n' + js_chip_hover)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("All fixes applied successfully.")

if __name__ == '__main__':
    fix_all()
