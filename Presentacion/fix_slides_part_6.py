import re

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix titles
html = html.replace(
    'El aporte del proyecto: Aria: un asistente especializado, no generalista.',
    'El aporte del proyecto: Aria, un asistente especializado y no generalista.'
)
html = html.replace(
    'Resultados · Latencia operativa: Respuesta fluida: solo 1.25 segundos de espera (latencia).',
    'Resultados · Latencia operativa: Respuesta fluida de solo 1.25 segundos.'
)
html = html.replace(
    'Diagrama de contexto · Nivel 0: El sistema como caja negra.',
    'Diagrama de contexto Nivel 0: El sistema como caja negra.'
)
html = html.replace(
    'Requerimientos del sistema: Lo que el sistema hace — y cómo debe hacerlo.',
    'Requerimientos del sistema: Lo que hace y cómo debe hacerlo.'
)

# Fix Slide 07 (slide-11 ID)
old_fin = '<div class="icon-box">💰</div>\n          <h3 style="color: var(--purple-900); font-size: 22px;">Dimensión Financiera</h3>'
new_fin = '<div class="icon-box">🏛️</div>\n          <h3 style="color: var(--purple-900); font-size: 22px;">Información Institucional</h3>'
if old_fin in html:
    html = html.replace(old_fin, new_fin)
    
old_fin_txt = '<p style="font-size: 18px;">Valores de aranceles ($700 presencial Quito), fechas de pagos diferidos (mayo, junio, julio) y canales oficiales de recaudación bancaria.</p>'
new_fin_txt = '<p style="font-size: 18px;">Ubicación de campus, títulos y especializaciones ofrecidas, e información relevante sobre los niveles y exámenes de suficiencia de inglés.</p>'
if old_fin_txt in html:
    html = html.replace(old_fin_txt, new_fin_txt)

# Fix Slide 13 (Requerimientos)
html = html.replace('<b style="color:var(--ink); font-family:var(--font-mono); font-size:12px;">RF-01</b> — ', '• ')
html = html.replace('<b style="color:var(--ink); font-family:var(--font-mono); font-size:12px;">RF-02</b> — ', '• ')
html = html.replace('<b style="color:var(--ink); font-family:var(--font-mono); font-size:12px;">RF-03</b> — ', '• ')
html = html.replace('<b style="color:var(--black); font-family:var(--font-mono); font-size:12px;">RNF-01</b> — ', '• ')
html = html.replace('<b style="color:var(--black); font-family:var(--font-mono); font-size:12px;">RNF-02</b> — ', '• ')
html = html.replace('<b style="color:var(--black); font-family:var(--font-mono); font-size:12px;">RNF-03</b> — ', '• ')

# Fix Conclusions
old_conclusions = """<h2 class="headline" style="max-width:40ch">Conclusiones: Tres hallazgos que sostienen el proyecto.</h2>
<ul class="point-list" style="margin-top:30px; max-width:940px;">
<li><span class="point-mark">01</span><div class="point-body"><b>RAG es viable y escalable</b><p>La integración de LLMs con técnicas RAG demostró ser una solución técnica altamente viable para descentralizar la burocracia académica.</p></div></li>
<li><span class="point-mark">02</span><div class="point-body"><b>Sin interrupciones</b><p>WebSockets y el procesamiento asíncrono en FastAPI garantizaron un flujo de interacción continuo, vital para interfaces basadas en voz.</p></div></li>
<li><span class="point-mark">03</span><div class="point-body"><b>Privacidad sin sacrificar recursos</b><p>Sustituir biometría compleja por bounding boxes cumplió el RNF-01 (Privacidad por Diseño) y ahorró recursos del servidor.</p></div></li>
</ul>"""

new_conclusions = """<h2 class="headline" style="max-width:none">Conclusiones: Resultados de los objetivos planteados.</h2>
<ul class="point-list" style="margin-top:20px; max-width:1100px; display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
<li><span class="point-mark">01</span><div class="point-body"><b>Base de conocimiento sólida</b><p>El análisis de procesos permitió determinar los requerimientos y establecer exitosamente la base de conocimiento con reglamentos y mallas.</p></div></li>
<li><span class="point-mark">02</span><div class="point-body"><b>Arquitectura integrada</b><p>El diseño modular logró una integración fluida de RAG, voz y avatar 3D en tiempo real usando WebSockets.</p></div></li>
<li><span class="point-mark">03</span><div class="point-body"><b>Prototipo funcional eficiente</b><p>Se implementó un sistema plenamente operativo que combina modelos de lenguaje locales (LLMs) con visión artificial ligera.</p></div></li>
<li><span class="point-mark">04</span><div class="point-body"><b>Alta usabilidad comprobada</b><p>Las pruebas demostraron una latencia ultrabaja y un alto nivel de satisfacción (SUS), validando la eficacia del sistema con estudiantes.</p></div></li>
</ul>"""

if old_conclusions in html:
    html = html.replace(old_conclusions, new_conclusions)
else:
    print("Could not find old conclusions exact match.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixes applied successfully!")
