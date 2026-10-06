export const slidesData = [
  {
    "title": "PORTADA",
    "content": "**Universidad Tecnológica Indoamérica**\n**Facultad de Ingeniería y Tecnologías de la Información**\n\n**TEMA:** \nAsistente Virtual Inteligente Basado en LLMs y RAG para la Carrera de Tecnologías de la Información\n\n**Autor:** Emilio Espinoza\n**Tutor:** Ing. Christian Eduardo Iza Llumiguisín\n**Fecha:** 2026"
  },
  {
    "title": "AGENDA DE LA PRESENTACIÓN",
    "content": "1. Capítulo I: Contexto y Planteamiento del Problema\n2. Estado del Arte y Aporte\n3. Metas y Justificación\n4. Fundamentación Teórica\n5. Capítulo II: Marco Metodológico y Planificación\n6. Diseño de la Solución (Arquitectura)\n7. Capítulo III: Implementación y Resultados\n8. Capítulo IV: Conclusiones y Recomendaciones"
  },
  {
    "title": "CAPÍTULO I — CONTEXTO",
    "content": "**La Era de la Información Universitaria**\n- La carrera de Tecnologías de la Información maneja un vasto corpus documental: mallas curriculares, sílabos, reglamentos de titulación y prácticas preprofesionales.\n- Tradicionalmente, esta información se distribuye en formatos estáticos (PDFs) a través de repositorios institucionales, correos o tableros físicos.\n- El estudiante moderno exige inmediatez y precisión en la obtención de respuestas."
  },
  {
    "title": "PLANTEAMIENTO DEL PROBLEMA",
    "content": "**¿Por qué fallan los métodos actuales?**\n- **Dispersión Documental:** La información oficial está fragmentada en múltiples archivos y plataformas.\n- **Búsqueda Sintáctica:** Los repositorios actuales dependen de coincidencias de palabras clave. Si un estudiante busca \"tesis\" pero el reglamento dice \"titulación\", no encuentra resultados.\n- **Falta de Comprensión Semántica:** El sistema tradicional no \"entiende\" la intención detrás de la pregunta."
  },
  {
    "title": "CONSECUENCIAS DEL PROBLEMA",
    "content": "- **Sobrecarga Administrativa:** Los estudiantes, al frustrarse con los documentos, acuden físicamente a secretaría para resolver dudas que son inherentemente automatizables.\n- **Cuellos de Botella:** Las secretarías invierten tiempo valioso repitiendo información estática en lugar de atender trámites complejos.\n- **Interfaz Reactiva y Estática:** Los portales universitarios requieren que el usuario navegue manualmente (clics, teclado), careciendo de proactividad."
  },
  {
    "title": "ESTADO DEL ARTE",
    "content": "**¿Qué existe actualmente en el mercado?**\n1. **Chatbots basados en Reglas (Árboles de decisión):** Rígidos, fallan ante preguntas fuera del guion. Muy comunes en atención al cliente básica.\n2. **Asistentes Virtuales Comerciales (Siri, Alexa):** Alta disponibilidad, pero conocimientos generalistas. No conocen el reglamento interno de la universidad.\n3. **Plataformas GPT Públicas:** Alta inteligencia, pero propensas a **alucinaciones** (inventan información) y no garantizan privacidad de datos institucionales."
  },
  {
    "title": "EL APORTE DEL PROYECTO",
    "content": "**Aria: Asistente Virtual Inteligente**\n- **Especialización:** Entrenado exclusivamente con el corpus documental oficial de la carrera de TI.\n- **Proactividad Multimodal:** No requiere teclado ni ratón. Detecta la presencia física del estudiante y conversa mediante voz.\n- **Privacidad y Fiabilidad:** Uso de motores locales y técnicas avanzadas (RAG) para garantizar cero alucinaciones y total privacidad de las consultas."
  },
  {
    "title": "METAS DE LA INVESTIGACIÓN (Objetivos)",
    "content": "**Objetivo General**\nDesarrollar e implementar un Asistente Virtual Inteligente multimodal, impulsado por Modelos de Lenguaje Grande (LLMs) y Generación Aumentada por Recuperación (RAG), para democratizar y automatizar el acceso a la información académica de la carrera."
  },
  {
    "title": "OBJETIVOS ESPECÍFICOS",
    "content": "1. **Recopilar y procesar** el conocimiento institucional (Mallas, Reglamentos) en una base de datos vectorial.\n2. **Diseñar la arquitectura lógica** y las capas de interacción (Visión Artificial, Speech-to-Text, Text-to-Speech).\n3. **Implementar el sistema RAG** para dotar al LLM de contexto cerrado y evitar alucinaciones.\n4. **Validar y medir** el rendimiento técnico (latencia, uso de recursos) y la precisión funcional del asistente."
  },
  {
    "title": "JUSTIFICACIÓN",
    "content": "**¿Por qué vale la pena este proyecto?**\n- **Innovación Educativa:** Posiciona a la carrera a la vanguardia tecnológica, utilizando IA generativa de forma ética y aplicada.\n- **Eficiencia Operativa:** Libera horas de trabajo administrativo en las secretarías.\n- **Accesibilidad:** Transforma documentos densos de 50 páginas en respuestas conversacionales inmediatas y naturales en español."
  },
  {
    "title": "ALCANCE Y LÍMITES",
    "content": "**Hasta dónde llega el sistema:**\n- **SÍ:** Responde dudas sobre mallas curriculares, requisitos de titulación, horas de vinculación y normativas de la carrera de TI.\n- **SÍ:** Interactúa proactivamente mediante reconocimiento facial básico y voz.\n- **NO:** No se integra transaccionalmente con el Sistema de Gestión Académica (SGA). No puede matricular estudiantes ni ver sus notas personales.\n- **NO:** No responde preguntas fuera de su dominio académico (ej. recetas médicas o cultura general)."
  },
  {
    "title": "FUNDAMENTACIÓN TEÓRICA",
    "content": "**Modelos de Lenguaje Grande (LLMs)**\n- Son redes neuronales masivas entrenadas para predecir la siguiente palabra en una secuencia.\n- Poseen habilidades emergentes de razonamiento y comprensión del lenguaje natural.\n- **Reto:** Su conocimiento se congela en la fecha de entrenamiento. No conocen documentos privados o recientes de la universidad."
  },
  {
    "title": "FUNDAMENTACIÓN TEÓRICA",
    "content": "**Generación Aumentada por Recuperación (RAG)**\n- Es el puente entre el LLM y los datos privados.\n- **Mecanismo:** Antes de que el LLM responda, el sistema busca en una base de datos local los párrafos más relevantes a la pregunta del usuario, y se los inyecta como \"Contexto\" al LLM.\n- **Resultado:** El LLM formula su respuesta basándose *exclusivamente* en esos párrafos oficiales."
  },
  {
    "title": "FUNDAMENTACIÓN TEÓRICA",
    "content": "**Bases de Datos Vectoriales (ChromaDB) y Similitud del Coseno**\n- En lugar de guardar texto plano, convierten las oraciones en **Vectores** (arreglos matemáticos de cientos de dimensiones).\n- **Similitud del Coseno:** Mide el ángulo $\\theta$ entre dos vectores. Si el ángulo es estrecho, los textos tienen el mismo *significado semántico*, aunque usen palabras distintas.\n- *(Nota para animación: Mostrar la fórmula del coseno y dos vectores en un plano 2D)*."
  },
  {
    "title": "CAPÍTULO II — MARCO METODOLÓGICO",
    "content": "**Metodología Ágil (Scrum)**\n- Dada la naturaleza experimental de la Inteligencia Artificial, los enfoques tradicionales (Cascada) resultan rígidos.\n- **Scrum** permitió iteraciones rápidas (*Sprints*), adaptando los *prompts* y ajustando el rendimiento del modelo progresivamente tras cada prueba."
  },
  {
    "title": "PLANIFICACIÓN",
    "content": "**Plan de Trabajo (Sprints Principales)**\n1. **Fase 1:** Recopilación documental y limpieza de datos (Data Engineering).\n2. **Fase 2:** Construcción del pipeline RAG y Base de Datos Vectorial.\n3. **Fase 3:** Desarrollo de interfaces multimodales (Visión y Voz).\n4. **Fase 4:** Integración, Pruebas de Estrés y Ajuste de Latencia.\n5. **Fase 5:** Despliegue en contenedor Docker y validación de usuario final."
  },
  {
    "title": "COSTOS DEL PROYECTO",
    "content": "**Viabilidad Económica**\n- **Costos de Software:** \\$0. Uso intensivo de tecnologías Open Source (FastAPI, React, ChromaDB, HuggingFace).\n- **Costos de Hardware:** Procesamiento en entorno local/GPU o mediante APIs de muy bajo costo (Groq) para inferencia rápida.\n- El proyecto demuestra que implementar IA de alto nivel no requiere presupuestos privativos inmensos institucionales."
  },
  {
    "title": "REQUERIMIENTOS DEL SISTEMA",
    "content": "**Requerimientos Funcionales (RF)**\n- RF-01: Detección No Biométrica de Presencia.\n- RF-02: Transcripción de Voz a Texto (STT) en tiempo real.\n- RF-03: Búsqueda Semántica Vectorial.\n\n**Requerimientos No Funcionales (RNF)**\n- RNF-01: Privacidad por Diseño (No guardar fotos ni audios).\n- RNF-02: Baja Latencia Operativa.\n- RNF-03: Tolerancia a Fallos y Alta Disponibilidad (WebSockets)."
  },
  {
    "title": "DISEÑO DE LA SOLUCIÓN",
    "content": "**Arquitectura Lógica de Alto Nivel**\n\n*(Nota: Insertar imagen GRANDE de Arquitectura de Software. Ajustar CSS para pantalla completa).*\n\n**[ANIMACIÓN RECOMENDADA]**\n1. **Frontend:** Kiosco físico interactivo (React + Vite).\n2. **Backend:** FastAPI, gestor de lógica y estado.\n3. **Motor Cognitivo:** ChromaDB y LLM.\n- Explicar cómo el flujo viaja de izquierda a derecha."
  },
  {
    "title": "DIAGRAMA DE CONTEXTO",
    "content": "**Interacción Estudiante - Sistema**\n\n*(Nota: Insertar Diagrama de Contexto).*\n\n- El estudiante es un ente externo que provee estímulos visuales (presencia) y sonoros (voz).\n- El sistema encapsula toda la complejidad técnica, devolviendo respuestas naturales auditivas y visuales (subtítulos/avatar)."
  },
  {
    "title": "CAPA DE PERCEPCIÓN (Visión Artificial)",
    "content": "**Optimización de Recursos**\n- **Idea Inicial:** Usar redes neuronales profundas para reconocimiento facial. *Problema:* Consumía excesiva CPU/GPU.\n- **Solución Adoptada:** Implementación de un algoritmo ligero de caja delimitadora (*Bounding Box*).\n- El sistema detecta el área del rostro humano en píxeles. Si supera un umbral de proximidad, asume intención de interactuar y \"despierta\" al avatar. *Eficiencia computacional extrema*."
  },
  {
    "title": "COMUNICACIÓN: ¿POR QUÉ WEBSOCKETS?",
    "content": "**Prevención de Interbloqueos (Deadlocks)**\n- En HTTP clásico, una consulta larga de IA bloquea el hilo de ejecución hasta terminar.\n- **WebSockets** establece un túnel bidireccional y asíncrono.\n- Permite enviar el audio binario (Base64/WebM) de forma fragmentada (*streaming*) y recibir actualizaciones de estado del asistente en tiempo real, evitando que la interfaz se congele."
  },
  {
    "title": "EL MOTOR COGNITIVO (RAG)",
    "content": "*(Nota: Insertar diagrama de BD Vectorial).*\n\n**[ANIMACIÓN DEL PIPELINE DE DATOS]**\n- **Paso 1: Ingesta.** Conversión de PDFs a Markdown estructurado (`pymupdf4llm`).\n- **Paso 2: Chunking.** División inteligente en fragmentos de 1500 caracteres, con solapamiento para no cortar ideas por la mitad.\n- **Paso 3: Indexación.** Creación del Vector (Embedding) y almacenamiento."
  },
  {
    "title": "DISEÑO DE BASE DE DATOS (NoSQL)",
    "content": "**Por qué usar un diseño No Relacional (Vectorial)**\n- Las bases de datos SQL relacionales (1NF, 2NF) son ineficientes para búsqueda semántica.\n- **ChromaDB** actúa como un almacén de documentos.\n- **Desnormalización:** Cada registro guarda el ID, el texto, su vector matemático y un objeto anidado JSON con *metadatos* (archivo origen, página).\n- **Ventaja:** Permite pre-filtrar consultas por metadato antes de calcular distancias matemáticas, optimizando los tiempos de búsqueda."
  },
  {
    "title": "DIAGRAMA DE CLASES (Backend)",
    "content": "*(Nota: Insertar Diagrama de Clases UML)*\n\n**Ingeniería Orientada a Objetos**\n- **Encapsulamiento:** Ocultamiento de funciones críticas matemáticas como privadas (`-`).\n- **Alta Cohesión:** Clases especializadas (`AudioProcessor`, `VisionHandler`, `RAGManager`).\n- **Bajo Acoplamiento:** Orquestación centralizada desde la aplicación FastAPI, sin clases desconectadas."
  },
  {
    "title": "CAPÍTULO III — IMPLEMENTACIÓN",
    "content": "- **Frontend:** Desarrollo de una interfaz de kiosco en React, con un avatar animado (CSS/Canvas) que reacciona visualmente cuando el estudiante habla (ondas de voz) y cuando el asistente responde.\n- **Backend:** Python + FastAPI. Integración de la API de Whisper-v3 (vía Groq) para transcripción (Speech-to-Text) a velocidad ultrarrápida.\n- **Despliegue:** Sistema empacado en Docker Compose, garantizando portabilidad y fácil ejecución en cualquier hardware de la universidad."
  },
  {
    "title": "PREVENCIÓN DE ALUCINACIONES",
    "content": "**El Riesgo de la Inteligencia Artificial**\n- **Problema:** Los LLMs tienden a inventar respuestas con gran seguridad si no saben algo (Alucinación).\n- **Solución: Contexto Cerrado Estricto.** \n  - El *System Prompt* prohíbe taxativamente inferir datos.\n  - Se valida el umbral de similitud del coseno. Si los documentos recuperados tienen baja similitud (no responden a la pregunta), el sistema intercepta la petición.\n- **Declinación Proactiva:** *\"No dispongo de información reglamentaria para responder esto.\"*"
  },
  {
    "title": "RESULTADOS: PRUEBAS FUNCIONALES (Caja Negra)",
    "content": "**Robustez Conversacional**\n- Se probaron más de 50 consultas aleatorias con estudiantes.\n- Se incluyeron **modismos ecuatorianos** y formulaciones gramaticales informales.\n- **Resultado:** El motor semántico logró entender la intención real detrás de las variaciones verbales, recuperando los artículos reglamentarios correctos en un 95% de los casos. Cero alucinaciones."
  },
  {
    "title": "RESULTADOS: LATENCIA OPERATIVA",
    "content": "**El Reto del Tiempo de Respuesta**\n- La latencia ideal en sistemas de **alta disponibilidad** (como ChatGPT Voice) es de **500 ms a 1.5 segundos** para mantener una ilusión de conversación humana fluida.\n- **Nuestras Métricas:**\n  - Transcripción de voz (STT): $\\approx 300$ ms.\n  - Búsqueda Vectorial (RAG): $\\approx 150$ ms.\n  - Generación LLM + Síntesis de voz (TTS): $\\approx 800$ ms.\n- **Total Promedio:** **$\\sim 1.25$ segundos.** ¡El sistema cumple exitosamente el estándar de latencia conversacional!"
  },
  {
    "title": "CAPÍTULO IV — CONCLUSIONES",
    "content": "- La integración de LLMs con técnicas RAG demostró ser una solución técnica altamente viable y escalable para descentralizar la burocracia académica.\n- El uso de **WebSockets** y el procesamiento asíncrono en **FastAPI** garantizó un flujo de interacción sin interrupciones, vital para interfaces basadas en voz.\n- Sustituir algoritmos biométricos complejos por detección de cajas delimitadoras garantizó el cumplimiento del requisito **RNF-01 (Privacidad por Diseño)** y salvó valiosos recursos del servidor."
  },
  {
    "title": "RECOMENDACIONES Y TRABAJO FUTURO",
    "content": "1. **Integración Transaccional API:** Conectar el asistente directamente al Sistema de Gestión Académica (SGA) bajo un inicio de sesión autenticado, permitiendo consultas hiperpersonalizadas (ej. *\"¿Con mi nota actual puedo tomar esta materia?\"*).\n2. **Affective Computing:** Añadir detección de microexpresiones faciales para que el avatar adapte su tono de voz al estado de ánimo del estudiante.\n3. **Escalabilidad Multilingüe:** Implementar soporte automático para inglés, beneficiando a estudiantes de intercambio."
  },
  {
    "title": "FIN DE LA PRESENTACIÓN",
    "content": "## ¡Gracias por su atención!\n\n*(Espacio abierto para la ronda de preguntas y debate técnico por parte del honorable tribunal).*"
  }
];
