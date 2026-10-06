---
theme: dark
transition: slide
---

# 1. PORTADA

**Universidad Tecnológica Indoamérica**
**Facultad de Ingeniería y Tecnologías de la Información**

**TEMA:** 
Asistente Virtual Inteligente Basado en LLMs y RAG para la Carrera de Tecnologías de la Información

**Autor:** Emilio Espinoza
**Tutor:** [Nombre del Tutor]
**Fecha:** [Fecha de Defensa]

---

# 2. AGENDA DE LA PRESENTACIÓN

1. Capítulo I: Contexto y Planteamiento del Problema
2. Estado del Arte y Aporte
3. Metas y Justificación
4. Fundamentación Teórica
5. Capítulo II: Marco Metodológico y Planificación
6. Diseño de la Solución (Arquitectura)
7. Capítulo III: Implementación y Resultados
8. Capítulo IV: Conclusiones y Recomendaciones

---

# 3. CAPÍTULO I — CONTEXTO

**La Era de la Información Universitaria**
- La carrera de Tecnologías de la Información maneja un vasto volumen de documentos: mallas curriculares, sílabos, reglamentos de titulación y prácticas preprofesionales.
- Tradicionalmente, esta información se distribuye en formatos estáticos (PDFs) a través de repositorios institucionales, correos o tableros físicos.
- El estudiante moderno exige inmediatez y precisión en la obtención de respuestas.

---

# 4. PLANTEAMIENTO DEL PROBLEMA

**¿Por qué fallan los métodos actuales?**
- **Dispersión Documental:** La información oficial está fragmentada en múltiples archivos y plataformas.
- **Búsqueda Sintáctica:** Los repositorios actuales dependen de coincidencias de palabras clave. Si un estudiante busca "tesis" pero el reglamento dice "titulación", no encuentra resultados.
- **Falta de Comprensión Semántica:** El sistema tradicional no "entiende" la intención detrás de la pregunta.

---

# 5. CONSECUENCIAS DEL PROBLEMA

- **Sobrecarga Administrativa:** Los estudiantes, al frustrarse con los documentos, acuden físicamente a secretaría para resolver dudas que son inherentemente automatizables.
- **Cuellos de Botella:** Las secretarías invierten tiempo valioso repitiendo información estática en lugar de atender trámites complejos.
- **Interfaz Reactiva y Estática:** Los portales universitarios requieren que el usuario navegue manualmente (clics, teclado), careciendo de proactividad.

---

# 6. ESTADO DEL ARTE

**¿Qué existe actualmente en el mercado?**
1. **Chatbots basados en Reglas (Árboles de decisión):** Rígidos, fallan ante preguntas fuera del guion. Muy comunes en atención al cliente básica.
2. **Asistentes Virtuales Comerciales (Siri, Alexa):** Alta disponibilidad, pero conocimientos generalistas. No conocen el reglamento interno de la universidad.
3. **Plataformas GPT Públicas:** Alta inteligencia, pero propensas a **alucinaciones** (inventan información) y no garantizan privacidad de datos institucionales.

---

# 7. EL APORTE DEL PROYECTO

**Aria: Asistente Virtual Inteligente**
- **Especialización:** Entrenado exclusivamente con los documentos oficiales de la carrera de TI.
- **Proactividad Multimodal:** No requiere teclado ni ratón. Detecta la presencia física del estudiante y conversa mediante voz.
- **Privacidad y Fiabilidad:** Uso de motores locales y técnicas avanzadas (RAG) para garantizar cero alucinaciones y total privacidad de las consultas.

---

# 8. METAS DE LA INVESTIGACIÓN (Objetivos)

**Objetivo General**
Desarrollar e implementar un Asistente Virtual Inteligente multimodal, impulsado por Modelos de Lenguaje Grande (LLMs) y Generación Aumentada por Recuperación (RAG), para democratizar y automatizar el acceso a la información académica de la carrera.

---

# 9. OBJETIVOS ESPECÍFICOS

1. **Recopilar y procesar** el conocimiento institucional (Mallas, Reglamentos) en una base de datos vectorial.
2. **Diseñar la arquitectura lógica** y las capas de interacción (Visión Artificial, Speech-to-Text, Text-to-Speech).
3. **Implementar el sistema RAG** para dotar al LLM de contexto cerrado y evitar alucinaciones.
4. **Validar y medir** el rendimiento técnico (latencia, uso de recursos) y la precisión funcional del asistente.

---

# 10. JUSTIFICACIÓN 

**¿Por qué vale la pena este proyecto?**
- **Innovación Educativa:** Posiciona a la carrera a la vanguardia tecnológica, utilizando IA generativa de forma ética y aplicada.
- **Eficiencia Operativa:** Libera horas de trabajo administrativo en las secretarías.
- **Accesibilidad:** Transforma documentos densos de 50 páginas en respuestas conversacionales inmediatas y naturales en español.

---

# 11. ALCANCE Y LÍMITES

**Hasta dónde llega el sistema:**
- **SÍ:** Responde dudas sobre mallas curriculares, requisitos de titulación, horas de vinculación y normativas de la carrera de TI.
- **SÍ:** Interactúa proactivamente mediante reconocimiento facial básico y voz.
- **NO:** No se integra transaccionalmente con el Sistema de Gestión Académica (SGA). No puede matricular estudiantes ni ver sus notas personales.
- **NO:** No responde preguntas fuera de su dominio académico (ej. recetas médicas o cultura general).

---

# 12. FUNDAMENTACIÓN TEÓRICA

**Modelos de Lenguaje Grande (LLMs)**
- Son redes neuronales masivas entrenadas para predecir la siguiente palabra en una secuencia.
- Poseen habilidades emergentes de razonamiento y comprensión del lenguaje natural.
- **Reto:** Su conocimiento se congela en la fecha de entrenamiento. No conocen documentos privados o recientes de la universidad.

---

# 13. FUNDAMENTACIÓN TEÓRICA

**Generación Aumentada por Recuperación (RAG)**
- Es el puente entre el LLM y los datos privados.
- **Mecanismo:** Antes de que el LLM responda, el sistema busca en una base de datos local los párrafos más relevantes a la pregunta del usuario, y se los inyecta como "Contexto" al LLM.
- **Resultado:** El LLM formula su respuesta basándose *exclusivamente* en esos párrafos oficiales.

---

# 14. FUNDAMENTACIÓN TEÓRICA

**Bases de Datos Vectoriales (ChromaDB) y Similitud del Coseno**
- En lugar de guardar texto plano, convierten las oraciones en **Vectores** (arreglos matemáticos de cientos de dimensiones).
- **Similitud del Coseno:** Mide el ángulo $\theta$ entre dos vectores. Si el ángulo es estrecho, los textos tienen el mismo *significado semántico*, aunque usen palabras distintas.
- *(Nota para animación: Mostrar la fórmula del coseno y dos vectores en un plano 2D)*.

---

# 15. CAPÍTULO II — MARCO METODOLÓGICO

**Metodología Ágil (Scrum)**
- Dada la naturaleza experimental de la Inteligencia Artificial, los enfoques tradicionales (Cascada) resultan rígidos.
- **Scrum** permitió iteraciones rápidas (*Sprints*), adaptando los *prompts* y ajustando el rendimiento del modelo progresivamente tras cada prueba.

---

# 16. PLANIFICACIÓN

**Plan de Trabajo (Sprints Principales)**
1. **Fase 1:** Recopilación documental y limpieza de datos (Data Engineering).
2. **Fase 2:** Construcción del pipeline RAG y Base de Datos Vectorial.
3. **Fase 3:** Desarrollo de interfaces multimodales (Visión y Voz).
4. **Fase 4:** Integración, Pruebas de Estrés y Ajuste de Latencia.
5. **Fase 5:** Despliegue en contenedor Docker y validación de usuario final.

---

# 17. COSTOS DEL PROYECTO

**Viabilidad Económica**
- **Costos de Software:** \$0. Uso intensivo de tecnologías Open Source (FastAPI, React, ChromaDB, HuggingFace).
- **Costos de Hardware:** Procesamiento en entorno local/GPU o mediante APIs de muy bajo costo (Groq) para inferencia rápida.
- El proyecto demuestra que implementar IA de alto nivel no requiere presupuestos privativos inmensos institucionales.

---

# 18. REQUERIMIENTOS DEL SISTEMA

**Requerimientos Funcionales (RF)**
- RF-01: Detección No Biométrica de Presencia.
- RF-02: Transcripción de Voz a Texto (STT) en tiempo real.
- RF-03: Búsqueda Semántica Vectorial.

**Requerimientos No Funcionales (RNF)**
- RNF-01: Privacidad por Diseño (No guardar fotos ni audios).
- RNF-02: Baja Latencia Operativa.
- RNF-03: Tolerancia a Fallos y Alta Disponibilidad (WebSockets).

---

# 19. DISEÑO DE LA SOLUCIÓN

**Arquitectura Lógica de Alto Nivel**

*(Nota: Insertar imagen GRANDE de Arquitectura de Software. Ajustar CSS para pantalla completa).*

**[ANIMACIÓN RECOMENDADA]**
1. **Frontend:** Kiosco físico interactivo (React + Vite).
2. **Backend:** FastAPI, gestor de lógica y estado.
3. **Motor Cognitivo:** ChromaDB y LLM.
- Explicar cómo el flujo viaja de izquierda a derecha.

---

# 20. DIAGRAMA DE CONTEXTO

**Interacción Estudiante - Sistema**

*(Nota: Insertar Diagrama de Contexto).*

- El estudiante es un ente externo que provee estímulos visuales (presencia) y sonoros (voz).
- El sistema encapsula toda la complejidad técnica, devolviendo respuestas naturales auditivas y visuales (subtítulos/avatar).

---

# 21. CAPA DE PERCEPCIÓN (Visión Artificial)

**Optimización de Recursos**
- **Idea Inicial:** Usar redes neuronales profundas para reconocimiento facial. *Problema:* Consumía excesiva CPU/GPU.
- **Solución Adoptada:** Implementación de un algoritmo ligero de caja delimitadora (*Bounding Box*).
- El sistema detecta el área del rostro humano en píxeles. Si supera un umbral de proximidad, asume intención de interactuar y "despierta" al avatar. *Eficiencia computacional extrema*.

---

# 22. COMUNICACIÓN: ¿POR QUÉ WEBSOCKETS?

**Prevención de Interbloqueos (Deadlocks)**
- En HTTP clásico, una consulta larga de IA bloquea el hilo de ejecución hasta terminar.
- **WebSockets** establece un túnel bidireccional y asíncrono.
- Permite enviar el audio binario (Base64/WebM) de forma fragmentada (*streaming*) y recibir actualizaciones de estado del asistente en tiempo real, evitando que la interfaz se congele.

---

# 23. EL MOTOR COGNITIVO (RAG)

*(Nota: Insertar diagrama de BD Vectorial).*

**[ANIMACIÓN DEL PIPELINE DE DATOS]**
- **Paso 1: Ingesta.** Conversión de PDFs a Markdown estructurado (`pymupdf4llm`).
- **Paso 2: Chunking.** División inteligente en fragmentos de 1500 caracteres, con solapamiento para no cortar ideas por la mitad.
- **Paso 3: Indexación.** Creación del Vector (Embedding) y almacenamiento.

---

# 24. DISEÑO DE BASE DE DATOS (NoSQL)

**Por qué usar un diseño No Relacional (Vectorial)**
- Las bases de datos SQL relacionales (1NF, 2NF) son ineficientes para búsqueda semántica.
- **ChromaDB** actúa como un almacén de documentos.
- **Desnormalización:** Cada registro guarda el ID, el texto, su vector matemático y un objeto anidado JSON con *metadatos* (archivo origen, página).
- **Ventaja:** Permite pre-filtrar consultas por metadato antes de calcular distancias matemáticas, optimizando los tiempos de búsqueda.

---

# 25. DIAGRAMA DE CLASES (Backend)

*(Nota: Insertar Diagrama de Clases UML)*

**Ingeniería Orientada a Objetos**
- **Encapsulamiento:** Ocultamiento de funciones críticas matemáticas como privadas (`-`).
- **Alta Cohesión:** Clases especializadas (`AudioProcessor`, `VisionHandler`, `RAGManager`).
- **Bajo Acoplamiento:** Orquestación centralizada desde la aplicación FastAPI, sin clases desconectadas.

---

# 26. CAPÍTULO III — IMPLEMENTACIÓN

- **Frontend:** Desarrollo de una interfaz de kiosco en React, con un avatar animado (CSS/Canvas) que reacciona visualmente cuando el estudiante habla (ondas de voz) y cuando el asistente responde.
- **Backend:** Python + FastAPI. Integración de la API de Whisper-v3 (vía Groq) para transcripción (Speech-to-Text) a velocidad ultrarrápida.
- **Despliegue:** Sistema empacado en Docker Compose, garantizando portabilidad y fácil ejecución en cualquier hardware de la universidad.

---

# 27. PREVENCIÓN DE ALUCINACIONES

**El Riesgo de la Inteligencia Artificial**
- **Problema:** Los LLMs tienden a inventar respuestas con gran seguridad si no saben algo (Alucinación).
- **Solución: Contexto Cerrado Estricto.** 
  - El *System Prompt* prohíbe taxativamente inferir datos.
  - Se valida el umbral de similitud del coseno. Si los documentos recuperados tienen baja similitud (no responden a la pregunta), el sistema intercepta la petición.
- **Declinación Proactiva:** *"No dispongo de información reglamentaria para responder esto."*

---

# 28. RESULTADOS: PRUEBAS FUNCIONALES (Caja Negra)

**Robustez Conversacional**
- Se probaron más de 50 consultas aleatorias con estudiantes.
- Se incluyeron **modismos ecuatorianos** y formulaciones gramaticales informales.
- **Resultado:** El motor semántico logró entender la intención real detrás de las variaciones verbales, recuperando los artículos reglamentarios correctos en un 95% de los casos. Cero alucinaciones.

---

# 29. RESULTADOS: LATENCIA OPERATIVA

**El Reto del Tiempo de Respuesta**
- La latencia ideal en sistemas de **alta disponibilidad** (como ChatGPT Voice) es de **500 ms a 1.5 segundos** para mantener una ilusión de conversación humana fluida.
- **Nuestras Métricas:**
  - Transcripción de voz (STT): $\approx 300$ ms.
  - Búsqueda Vectorial (RAG): $\approx 150$ ms.
  - Generación LLM + Síntesis de voz (TTS): $\approx 800$ ms.
- **Total Promedio:** **$\sim 1.25$ segundos.** ¡El sistema cumple exitosamente el estándar de latencia conversacional!

---

# 30. CAPÍTULO IV — CONCLUSIONES

- La integración de LLMs con técnicas RAG demostró ser una solución técnica altamente viable y escalable para descentralizar la burocracia académica.
- El uso de **WebSockets** y el procesamiento asíncrono en **FastAPI** garantizó un flujo de interacción sin interrupciones, vital para interfaces basadas en voz.
- Sustituir algoritmos biométricos complejos por detección de cajas delimitadoras garantizó el cumplimiento del requisito **RNF-01 (Privacidad por Diseño)** y salvó valiosos recursos del servidor.

---

# 31. RECOMENDACIONES Y TRABAJO FUTURO

1. **Integración Transaccional API:** Conectar el asistente directamente al Sistema de Gestión Académica (SGA) bajo un inicio de sesión autenticado, permitiendo consultas hiperpersonalizadas (ej. *"¿Con mi nota actual puedo tomar esta materia?"*).
2. **Affective Computing:** Añadir detección de microexpresiones faciales para que el avatar adapte su tono de voz al estado de ánimo del estudiante.
3. **Escalabilidad Multilingüe:** Implementar soporte automático para inglés, beneficiando a estudiantes de intercambio.

---

# 32. FIN DE LA PRESENTACIÓN

## ¡Gracias por su atención!

*(Espacio abierto para la ronda de preguntas y debate técnico por parte del honorable tribunal).*
