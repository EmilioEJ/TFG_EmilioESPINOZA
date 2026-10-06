import re

def fix_all_3():
    path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # =====================================================
    # 1. PAGE NUMBERS (Slide Enumeration)
    # =====================================================
    if 'body { counter-reset: slideCounter; }' not in html:
        # Let's just insert it at the very top of the CSS
        css_start = html.find('<style>')
        if css_start != -1:
            css_inject = """
/* SLIDE NUMBERS RESTORED */
body { counter-reset: slideCounter; }
.slide { counter-increment: slideCounter; }
.slide::after {
  content: "Diapositiva " counter(slideCounter);
  position: absolute;
  top: 30px;
  right: 40px;
  background: var(--purple-900);
  color: white;
  padding: 8px 24px;
  font-size: 16px;
  font-weight: 600;
  border-bottom: 6px solid var(--orange-500);
  border-radius: 8px;
  font-family: var(--font-body);
  opacity: 1 !important;
  z-index: 1000;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
.slide.cover::after {
  display: none !important;
}
"""
            html = html[:css_start+7] + css_inject + html[css_start+7:]

    # Remove the old broken slide numbering block that might be further down
    broken_block = """.slide {
  counter-increment: slideCounter;
}
.slide::after {
  content: "Diapositiva " counter(slideCounter);
  position: absolute;
  top: 40px;
  right: 0;
  background: var(--purple-900);
  color: white;
  padding: 10px 30px;
  font-size: 18px;
  font-weight: 600;
  border-bottom: 8px solid var(--orange-500);
  font-family: var(--font-body);
  opacity: 1 !important;
  z-index: 100;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}"""
    html = html.replace(broken_block, "")

    # =====================================================
    # 2. GLOBAL HOVER EFFECTS ON DIAGRAM ELEMENTS
    # =====================================================
    if '/* INTERACTIVE SVG ELEMENTS */' not in html:
        css_start = html.find('<style>')
        svg_hover_css = """
/* INTERACTIVE SVG ELEMENTS */
.diag rect, .diag circle, .diag ellipse, .diag path.draw, .diag text {
  transition: all 0.3s ease;
}
.diag rect:hover, .diag circle:hover, .diag ellipse:hover {
  filter: drop-shadow(0 10px 15px rgba(228, 88, 31, 0.4));
  transform: translateY(-3px);
  cursor: pointer;
  stroke: var(--orange-500) !important;
  stroke-width: 3px !important;
}
.diag text:hover {
  fill: var(--orange-600) !important;
  cursor: pointer;
  transform: scale(1.05);
}
.step-chip {
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}
"""
        html = html[:css_start+7] + svg_hover_css + html[css_start+7:]

    # =====================================================
    # 3. SLIDE 9 (RAG Diagram - slide-13)
    # Make it more beautiful and creative
    # =====================================================
    old_slide13 = re.search(r'(<section class="slide"[^>]*id="slide-13"[^>]*>)(.*?)(</section>)', html, re.DOTALL)
    if old_slide13:
        new_slide13 = """
  <div class="slide-inner">
    <h2 class="headline" style="max-width: 50ch;">Fundamentos Teóricos: RAG, el puente entre el LLM y los datos.</h2>
    <p class="subhead" style="margin-bottom: 30px;">Pasa el cursor por cada bloque para ver cómo se transforma la información en conocimiento.</p>
    
    <div style="display:flex; justify-content:space-between; align-items:center; gap:20px; margin-top:20px;">
      
      <!-- Paso 1 -->
      <div class="interactive-card hover-reveal" style="flex:1; padding:25px; text-align:center; border:2px solid var(--purple-200); background:white;">
        <div class="icon-box" style="margin:0 auto 15px;">🗣️</div>
        <h3 style="color:var(--purple-900); font-size:20px;">1. Pregunta</h3>
        <p style="font-size:16px;">El estudiante realiza una consulta natural y ambigua. Ej: "¿Cómo me titulo?"</p>
      </div>

      <div style="font-size:30px; color:var(--orange-500); font-weight:bold;">→</div>
      
      <!-- Paso 2 -->
      <div class="interactive-card hover-reveal" style="flex:1; padding:25px; text-align:center; border:2px solid var(--purple-300); background:var(--purple-50);">
        <div class="icon-box" style="margin:0 auto 15px; background:var(--purple-200); color:var(--purple-800);">🔍</div>
        <h3 style="color:var(--purple-900); font-size:20px;">2. Búsqueda</h3>
        <p style="font-size:16px;">ChromaDB localiza los párrafos del reglamento que son matemáticamente similares a la pregunta.</p>
      </div>

      <div style="font-size:30px; color:var(--orange-500); font-weight:bold;">→</div>

      <!-- Paso 3 -->
      <div class="interactive-card hover-reveal" style="flex:1; padding:25px; text-align:center; border:2px solid var(--orange-300); background:var(--orange-50);">
        <div class="icon-box" style="margin:0 auto 15px; background:var(--orange-200); color:var(--orange-800);">🧠</div>
        <h3 style="color:var(--orange-900); font-size:20px;">3. Inyección</h3>
        <p style="font-size:16px;">El LLM recibe la pregunta + los párrafos exactos recuperados, creando un "contexto cerrado".</p>
      </div>
      
      <div style="font-size:30px; color:var(--purple-500); font-weight:bold;">→</div>

      <!-- Paso 4 -->
      <div class="interactive-card hover-reveal" style="flex:1; padding:25px; text-align:center; border:2px solid var(--purple-600); background:var(--purple-950);">
        <div class="icon-box" style="margin:0 auto 15px; background:var(--purple-700); color:white;">🎯</div>
        <h3 style="color:white; font-size:20px;">4. Respuesta</h3>
        <p style="font-size:16px; color:var(--purple-100);">El modelo redacta una respuesta fiel y empática, sin inventar absolutamente nada.</p>
      </div>
      
    </div>
  </div>
"""
        html = html[:old_slide13.start(2)] + new_slide13 + html[old_slide13.end(2):]

    # =====================================================
    # 4. SLIDE 14 (Arquitectura - slide-19)
    # ENLARGE DIAGRAM AND POP-UP ANIMATIONS FOR STEPPER
    # =====================================================
    if '<section class="slide" data-ch="5" id="slide-19">' in html:
        # Instead of replacing the whole slide, let's inject CSS to make the diagram bigger and the stepper look like popups
        popup_css = """
/* POP-UP STEPPER FOR ARCHITECTURE */
#slide-19 .diag svg {
  transform: scale(1.3) !important;
  transform-origin: center top !important;
  margin-top: 20px;
  margin-bottom: 60px;
}
#stepperArch {
  position: absolute;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  width: 90%;
  display: flex !important;
  justify-content: center;
  gap: 15px;
}
#stepperArch .step-chip {
  background: white !important;
  border: 2px solid var(--purple-200) !important;
  border-radius: 12px !important;
  padding: 15px 20px !important;
  box-shadow: 0 10px 25px rgba(0,0,0,0.15) !important;
  font-size: 16px !important;
  transform: translateY(20px);
  opacity: 0.7;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
}
#stepperArch .step-chip.is-active, #stepperArch .step-chip:hover {
  transform: translateY(-10px) scale(1.1) !important;
  opacity: 1 !important;
  border-color: var(--orange-500) !important;
  background: var(--purple-50) !important;
  z-index: 100;
}
"""
        css_start = html.find('<style>')
        html = html[:css_start+7] + popup_css + html[css_start+7:]

    # =====================================================
    # 5. SLIDE 18 (Visión artificial - slide-22)
    # Re-integrate the 3rd card and make them consistent
    # =====================================================
    old_slide22 = re.search(r'(<section class="slide"[^>]*id="slide-22"[^>]*>)(.*?)(</section>)', html, re.DOTALL)
    if old_slide22:
        new_slide22 = """
  <div class="slide-inner">
    <h2 class="headline" style="max-width:50ch">Visión artificial: Detección rápida y optimizada</h2>
    <p class="subhead" style="margin-bottom: 30px;">Pasa el cursor sobre cada tarjeta para ver los detalles de la implementación.</p>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px;">
      
      <div class="interactive-card hover-reveal" style="padding: 30px; border-top: 5px solid var(--purple-300);">
        <div style="display:flex; flex-direction:column; align-items:center; gap:15px; text-align:center;">
          <div class="icon-box" style="width:80px; height:80px; font-size:40px;">⚠️</div>
          <h3 style="color: var(--purple-900); font-size: 22px;">Idea inicial descartada</h3>
        </div>
        <p style="font-size: 18px; text-align:center;">El uso de redes profundas de reconocimiento facial consumía demasiada CPU/GPU y no era viable para hardware limitado de un kiosco.</p>
      </div>

      <div class="interactive-card hover-reveal" style="padding: 30px; border-top: 5px solid var(--orange-500); background:var(--orange-50);">
        <div style="display:flex; flex-direction:column; align-items:center; gap:15px; text-align:center;">
          <div class="icon-box" style="background:var(--orange-200); color:var(--orange-700); width:80px; height:80px; font-size:40px;">✅</div>
          <h3 style="color: var(--orange-900); font-size: 22px;">Solución adoptada</h3>
        </div>
        <p style="font-size: 18px; text-align:center;">Se optó por un <b>Bounding Box ligero</b> que sólo detecta la presencia del rostro en píxeles. Si el usuario se acerca, asume intención de hablar.</p>
      </div>

      <div class="interactive-card hover-reveal" style="padding: 30px; border-top: 5px solid var(--purple-600); background:var(--purple-50);">
        <div style="display:flex; flex-direction:column; align-items:center; gap:15px; text-align:center;">
          <div class="icon-box" style="background:var(--purple-200); color:var(--purple-800); width:80px; height:80px; font-size:40px;">👁️</div>
          <h3 style="color: var(--purple-900); font-size: 22px;">¿Cómo funciona?</h3>
        </div>
        <p style="font-size: 18px; text-align:center;">Utiliza <b>TensorFlow.js</b> y <b>MediaPipe</b>. Al detectar un rostro, activa el micrófono; si el rostro sale del cuadro, pausa la escucha para ahorrar recursos.</p>
      </div>

    </div>
  </div>
"""
        html = html[:old_slide22.start(2)] + new_slide22 + html[old_slide22.end(2):]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("All additional fixes applied successfully.")

if __name__ == '__main__':
    fix_all_3()
