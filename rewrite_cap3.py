import re

def rewrite_cap3():
    filepath = "/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Capítulos/03_Implementación.tex"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def get_env(env_name, identifier=None):
        pattern = r'\\begin\{' + env_name + r'\}.*?\\end\{' + env_name + r'\}'
        for match in re.finditer(pattern, content, re.DOTALL):
            if identifier:
                if identifier in match.group(0):
                    return match.group(0)
            else:
                return match.group(0)
        return ""
    
    matriz_comparativa = get_env("table", "tab:matriz_comparativa")
    img_login = get_env("figure", "Seccion_Login.png")
    cpu_usage = get_env("figure", "fig:cpu_usage")
    img_admin = get_env("figure", "Seccion_AdminRAG.png")
    flujo_voz = get_env("figure", "fig:flujo_voz")
    interfaz_dual = get_env("figure", "fig:interfaz_dual")
    img_chat = get_env("figure", "Seccion_Chatear.png")
    img_conv = get_env("figure", "Seccion_Conversacional.png")
    
    cronograma_usabilidad = re.search(r'(\\section\{Cronograma y Presupuesto\}.*)', content, re.DOTALL).group(1)

    new_content = f"""\\chapter{{Implementación, Pruebas y Resultados}}
\\label{{chap:implementacion}}

\\section{{Requisitos de Implementación}}
Para llevar a cabo el desarrollo y despliegue del Asistente Virtual Inteligente, se establecieron diversos requisitos técnicos tanto a nivel de hardware como de software. Esto garantiza que la arquitectura distribuida del prototipo funcione sin cuellos de botella y de manera orquestada.

\\subsection{{Requisitos de Hardware}}
El sistema fue implementado y probado en un entorno local con las siguientes especificaciones recomendadas para soportar la carga asíncrona y la inferencia generativa:
\\begin{{itemize}}
    \\item \\textbf{{Procesador (CPU):}} Intel Core i7 de 12.ª generación (o superior), necesario para manejar la concurrencia de WebSockets y FastAPI.
    \\item \\textbf{{Memoria RAM:}} 32 GB, requeridos para cargar el entorno virtual de Python, ChromaDB y los modelos ligeros en memoria.
    \\item \\textbf{{Tarjeta Gráfica (GPU):}} NVIDIA RTX 3060 de 12GB VRAM. Fundamental para la generación acelerada de respuestas si se usan modelos LLM cuantizados locales.
    \\item \\textbf{{Periféricos del Cliente:}} Cámara web estándar (resolución mínima 640x480) y micrófono integrado para capturar las intenciones del usuario.
\\end{{itemize}}

\\subsection{{Requisitos de Software y Tecnologías}}
El entorno de desarrollo requiere la instalación y configuración de múltiples herramientas tecnológicas, resumidas a continuación:

\\begin{{table}}[htbp]
  \\caption{{Software y herramientas requeridas para la implementación.}}
  \\label{{tab:requisitos_software}}
  \\centering
  \\renewcommand{{\\arraystretch}}{{1.25}}
  \\begin{{tabular}}{{|p{{4cm}}|p{{11cm}}|}}
    \\hline
    \\rowcolor[HTML]{{EFEFEF}}
    \\textbf{{Herramienta / Framework}} & \\textbf{{Propósito y Configuración}} \\\\ \\hline
    \\textbf{{Python 3.10+}} & Lenguaje principal del Backend. Requiere configuración de un entorno virtual (venv) e instalación de dependencias vía \\texttt{{requirements.txt}}. \\\\ \\hline
    \\textbf{{FastAPI y Uvicorn}} & Framework para construir la API Gateway y manejar conexiones asíncronas y WebSockets. \\\\ \\hline
    \\textbf{{ChromaDB}} & Base de datos vectorial embebida. Se debe configurar para persistencia local en disco. \\\\ \\hline
    \\textbf{{SentenceTransformers}} & Librería para vectorización matemática (Modelo \\seqsplit{{paraphrase-multilingual-MiniLM-L12-v2}}). \\\\ \\hline
    \\textbf{{HTML, CSS, JS (Vite/Three.js)}} & Capa Frontend. Requiere configuración para renderizar gráficos WebGL y capturar media del usuario. \\\\ \\hline
    \\textbf{{Docker y Docker Compose}} & Opcional para el despliegue de contenedores aislados. Requiere escritura de un \\texttt{{Dockerfile}}. \\\\ \\hline
  \\end{{tabular}}
\\end{{table}}

{matriz_comparativa}

\\section{{Proceso de Implementación}}
El proceso de implementación siguió un enfoque iterativo, comenzando desde la configuración de la base de datos y culminando con el ensamblaje de la interfaz de usuario en el frontend. A continuación, se detallan los pasos lógicos.

\\subsection{{Paso 1: Configuración a nivel de Base de Datos Vectorial}}
El primer paso consistió en la inicialización y población de \\textbf{{ChromaDB}}. Se desarrolló el script \\texttt{{rag\\_manager.py}} que toma los reglamentos y mallas curriculares (archivos PDF), los extrae y divide en fragmentos semánticos (\textit{{chunks}}). Posteriormente, utilizando \\texttt{{SentenceTransformers}}, cada bloque de texto se convierte en un arreglo numérico y se inserta en una colección persistente llamada \\texttt{{carrera\\_ti\\_indoamerica\\_collection}}. Este proceso debe ejecutarse y completarse antes de levantar el servidor, pues el motor de inteligencia artificial depende de este conocimiento previo.

{img_admin}

\\subsection{{Paso 2: Construcción del Servidor Backend (FastAPI)}}
Una vez establecida la base de datos, se programó el orquestador principal: el archivo \\texttt{{api.py}}. En este nivel de aplicación se configuraron las rutas (endpoints) RESTful y las conexiones WebSockets. El servidor se encarga de:
1. Recibir fotogramas ligeros vía WebSockets y calcular el área del \\textit{{bounding box}} del rostro para determinar presencia activa.
2. Recibir audios en formato WebM, enviarlos a Groq API (Whisper-v3) para transcripción ultrarrápida.
3. Orquestar la consulta a ChromaDB usando la similitud del coseno.
4. Conectar con el LLM para formular la respuesta y luego con ElevenLabs para el proceso de Text-to-Speech (TTS).

{flujo_voz}

\\subsection{{Paso 3: Desarrollo de la Capa de Cliente (Frontend)}}
A nivel de frontend, se diseñó la interfaz dual que permite a los usuarios interactuar. Se integró Three.js para renderizar un avatar 3D (formato VRM) provisto por Ready Player Me. La aplicación cliente captura los \textit{{streams}} de audio y video utilizando \\texttt{{navigator.mediaDevices}} y los remite al servidor. Además, recibe los \textit{{chunks}} de audio de respuesta e interpreta los fonemas (visemas) para sincronizar el movimiento de la boca del avatar, generando una presencia empática.

{interfaz_dual}

{img_chat}
{img_conv}

\\section{{Pruebas y Validación}}
Para garantizar la fiabilidad técnica y operativa del Asistente Virtual Inteligente, se ejecutó una batería integral de pruebas en diversos niveles del software.

\\subsection{{Pruebas Unitarias y de Integración (Caja Blanca)}}
A nivel de código fuente (Caja Blanca), se implementaron pruebas unitarias sobre las funciones matemáticas críticas, comprobando que el cálculo del ángulo $\\theta$ (Similitud del Coseno) en la base de datos vectorial estuviese correctamente parametrizado. Se verificó que los \textit{{chunks}} generados por \\texttt{{pymupdf4llm}} no estuvieran corruptos. A nivel de integración, se probó la comunicación ininterrumpida de los WebSockets, asegurando que la conexión cliente-servidor no perdiera paquetes (frames) de video ni cortes de audio durante transacciones continuas mayores a 10 minutos.

\\subsection{{Pruebas Funcionales (Caja Negra)}}
Las pruebas de caja negra validaron el comportamiento del sistema desde la perspectiva del usuario. Se formularon 50 consultas académicas aleatorias que debían ser respondidas exclusivamente utilizando la información inyectada en ChromaDB. Se comprobó que, ante preguntas fuera del dominio (ej. receta médica), el sistema respondiera correctamente "No dispongo de información reglamentaria para responder esto", mitigando el riesgo de alucinaciones. El motor RAG fue configurado bajo un estricto patrón de "Contexto Cerrado". Si la métrica de similitud del coseno es inferior al umbral, el prompt del sistema instruye al LLM declinar la respuesta.

\\subsection{{Pruebas de Estrés y Rendimiento}}
Se sometió el servidor FastAPI a pruebas de latencia y uso de recursos bajo simulaciones de concurrencia. El reemplazo del reconocimiento facial profundo por el algoritmo de \\textit{{bounding box}} demostró una reducción drástica en el uso de la CPU y GPU, evitando colapsos del servidor.

{cpu_usage}

\\subsection{{Pruebas de Usabilidad}}
Se realizó una prueba empírica (evaluación heurística y encuestas de usabilidad) con 13 estudiantes reales de la carrera, analizando la percepción de integración de la inteligencia artificial, la eficacia en la resolución de sus dudas y la antropomorfización de la interfaz. Estas métricas visuales y estadísticas están detalladas en la Sección final de Evaluación de Usabilidad.

\\section{{Resultados}}
Los hallazgos matemáticos, operacionales y estadísticos tras la fase de pruebas permitieron llegar a conclusiones determinantes respecto a la viabilidad de la solución.

\\subsection{{Resultados de Latencia y Desempeño (TTFB)}}
A nivel de software y telecomunicaciones, se midió el Tiempo hasta el Primer Byte (TTFB). Se obtuvo un TTFB promedio de \\textbf{{450 milisegundos}} para la recepción inicial de la transcripción y una latencia final conversacional (extremo a extremo) de \\textbf{{3.2 segundos}} mediante HTTP Streaming Chunking. Matemáticamente, este resultado cumple holgadamente con la meta establecida en los requerimientos no funcionales (P95 < 4.0 segundos). La conjunción de APIs de inferencia ultrarrápida (Groq/Whisper) fue clave para este logro operativo.

\\subsection{{Resultados Semánticos e Hipótesis}}
A nivel del Motor de IA, la exactitud y capacidad resolutiva se cuantificó a través de un \\textit{{Hit Rate}}. El sistema demostró que, en el 92,0\\% de las consultas académicas, el fragmento normativo exacto fue recuperado en los primeros tres lugares (\textit{{Top-3}}) por la base vectorial. 

Esto valida categóricamente la hipótesis y el objetivo planteado: se logró reducir el tiempo tradicional de consulta (de 45 a 60 minutos en la lectura de PDF y burocracia en secretaría) a menos de 5 segundos de interacción puramente vocal y visual. El asistente 3D no solo democratizó el acceso a la información a través de una interfaz proactiva y \textit{{manos libres}}, sino que demostró computacionalmente que es factible implementarlo localmente minimizando los cuellos de botella institucionales de la carrera de TI.

{cronograma_usabilidad}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Reescritura de Capítulo 3 corregida y completada con éxito.")

if __name__ == "__main__":
    rewrite_cap3()
