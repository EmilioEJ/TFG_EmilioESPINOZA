import re

def fix_avatar():
    path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # The exact original SVG for the avatar states diagram, wrapped in the slide-inner div.
    # Added the data-tooltip attributes exactly as the user wants them.
    correct_slide21 = """
  <div class="slide-inner" style="display:flex; flex-direction:column; align-items:center;">
    <h2 class="headline" style="text-align:center;">El ciclo de vida del avatar y sus interacciones</h2>
    <p class="subhead" style="text-align:center; margin-bottom: 20px;">Pasa el cursor sobre cada estado para ver su explicación.</p>
    
    <div class="avatar-states-container" style="position:relative; width:100%; max-width:600px; margin:0 auto;">
      <div class="diag" id="diagStates" data-anim="avatarstates" style="margin-top:20px;">
        <svg viewBox="0 0 460 460" width="100%" height="420" style="overflow:visible;">
          <defs><marker id="arrSt" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--ink-faint)"/></marker></defs>

          <path class="draw" d="M160 90 A 150 150 0 0 1 370 160" stroke="var(--line-strong)" stroke-width="2" fill="none" marker-end="url(#arrSt)"/>
          <text x="300" y="80" font-family="IBM Plex Mono" font-size="9.5" fill="var(--ink-soft)">presencia detectada</text>

          <path class="draw" d="M390 210 A 150 150 0 0 1 340 380" stroke="var(--line-strong)" stroke-width="2" fill="none" marker-end="url(#arrSt)"/>
          <text x="358" y="300" font-family="IBM Plex Mono" font-size="9.5" fill="var(--ink-soft)">silencio detectado</text>

          <path class="draw" d="M270 410 A 150 150 0 0 1 110 350" stroke="var(--line-strong)" stroke-width="2" fill="none" marker-end="url(#arrSt)"/>
          <text x="150" y="410" font-family="IBM Plex Mono" font-size="9.5" fill="var(--ink-soft)">TTFB completado</text>

          <path class="draw" d="M95 300 A 150 150 0 0 1 100 140" stroke="var(--orange-400)" stroke-width="2" fill="none" marker-end="url(#arrSt)" stroke-dasharray="5 4"/>
          <text x="20" y="230" font-family="IBM Plex Mono" font-size="9.5" fill="var(--orange-600)">fin de audio</text>

          <path class="draw" d="M150 105 A 150 150 0 0 0 105 300" stroke="var(--ink-faint)" stroke-width="1.5" fill="none" marker-end="url(#arrSt)" stroke-dasharray="2 4" opacity=".6"/>
          <text x="55" y="200" font-family="IBM Plex Mono" font-size="8.5" fill="var(--ink-faint)">timeout</text>

          <g class="state-node pop" id="stDormido" data-state="0" transform="translate(130,60)" data-tooltip="IDLE: El avatar realiza animaciones sutiles (respirar, parpadear) mientras espera detectar un rostro.">
            <circle r="52" fill="#fff" stroke="var(--line-strong)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="13" fill="var(--ink)">Dormido</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="var(--ink-soft)">idle</text>
          </g>
          
          <g class="state-node pop" id="stEscuchando" data-state="1" transform="translate(400,190)" data-tooltip="LISTENING: Se activa el micrófono. El avatar asiente y mantiene contacto visual simulado.">
            <circle r="55" fill="#fff" stroke="var(--purple-300)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="13" fill="var(--ink)">Escuchando</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="var(--ink-soft)">listening</text>
          </g>
          
          <g class="state-node pop" id="stPensando" data-state="2" transform="translate(310,400)" data-tooltip="THINKING: Mientras el RAG y LLM procesan, el avatar mira hacia arriba/lados, indicando procesamiento.">
            <circle r="55" fill="#fff" stroke="var(--purple-300)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="13" fill="var(--ink)">Pensando</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="var(--ink-soft)">processing</text>
          </g>
          
          <g class="state-node pop" id="stHablando" data-state="3" transform="translate(80,360)" data-tooltip="TALKING: Reproduce el audio sintetizado sincronizando los visemas (movimiento labial) con el texto.">
            <circle r="55" fill="#fff" stroke="var(--orange-300)" stroke-width="2.5"/>
            <text y="-4" text-anchor="middle" font-family="IBM Plex Sans" font-weight="600" font-size="13" fill="var(--ink)">Hablando</text>
            <text y="14" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="var(--ink-soft)">speaking</text>
          </g>
        </svg>
      </div>

      <div id="stateTooltip" style="position:absolute; bottom:-40px; left:50%; transform:translateX(-50%); background:var(--purple-50); border:2px solid var(--purple-200); border-radius:12px; padding:20px 30px; font-size:18px; color:var(--ink); text-align:center; width:90%; opacity:0; transition:opacity 0.3s ease; pointer-events:none; z-index:1000; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        Pasa el cursor sobre un estado...
      </div>
    </div>
  </div>
"""

    # We need to replace the content of slide-21.
    old_slide21 = re.search(r'(<section class="slide"[^>]*id="slide-21"[^>]*>)(.*?)(</section>)', html, re.DOTALL)
    if old_slide21:
        html = html[:old_slide21.start(2)] + "\n" + correct_slide21 + "\n" + html[old_slide21.end(2):]

    # Furthermore, I should fix the generic CSS I added that might be breaking SVG layouts
    # in some browsers by removing `transform: translateY(-3px);` from SVG hover effects
    # as SVG transforms in CSS are tricky and might conflict with the `transform` attribute
    # on parent elements like <g>.
    bad_svg_hover = """
.diag rect:hover, .diag circle:hover, .diag ellipse:hover {
  filter: drop-shadow(0 10px 15px rgba(228, 88, 31, 0.4));
  transform: translateY(-3px);
  cursor: pointer;
  stroke: var(--orange-500) !important;
  stroke-width: 3px !important;
}"""
    good_svg_hover = """
.diag rect:hover, .diag circle:hover, .diag ellipse:hover {
  filter: drop-shadow(0 10px 15px rgba(228, 88, 31, 0.4));
  cursor: pointer;
  stroke: var(--orange-500) !important;
  stroke-width: 3px !important;
}
.state-node:hover {
  transform: scale(1.05);
}
"""
    html = html.replace(bad_svg_hover, good_svg_hover)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Fixed slide-21 avatar diagram and SVG hover CSS.")

if __name__ == '__main__':
    fix_avatar()
