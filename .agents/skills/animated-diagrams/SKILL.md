---
name: animated-diagrams
description: >-
  Construcción, ajuste y mantenimiento de diagramas animados interactivos en la presentación de sustentación de tesis:
  Asistente Virtual 3D con Visión Artificial y RAG.
  Use this skill whenever creating, modifying, fixing, or explaining animated diagrams in `Presentacion/src/flows`,
  including C4 architecture container diagrams, sequence diagrams, particle data flows, geometry routing, collision avoidance,
  or step-by-step narrative flows in React + SVG. TRIGGERS: diagramas animados, diagrama c4, diagrama de secuencia,
  FlowGraph, SequenceDiagram, flows, avatar 3d, chromadb, rag, arquitectura ai, asistente virtual, visión artificial.
---

# Diagramas Animados e Interactivos de Presentación (Asistente 3D AI)

Esta skill estandariza el diseño, la geometría y la especificación de los diagramas animados paso a paso en la presentación de tesis del **Asistente Virtual 3D** (`Presentacion/src/flows`).

El proyecto cuenta con un motor propio en **React + SVG + HTML** dividido en dos familias:
1. **Diagramas de Grafo / Contenedores C4 (`FlowGraph`)**: Para la arquitectura general (Frontend Unity/Web, Backend FastAPI, Base Vectorial ChromaDB, Inteligencia Groq LLM) y tuberías de datos.
2. **Diagramas de Secuencia Temporal (`SequenceDiagram`)**: Para flujos específicos como Ingesta de Documentos RAG, Detección de Visión Artificial, o transcripción STT/TTS.

Ambos sistemas comparten el mismo ciclo de vida (`useFlowPlayer`), navegación por pasos (`FlowStepper`), panel explicativo con métricas (`FlowDetail`) y catálogo desacoplado de iconos (`icons.js`).

---

## 🧭 ¿Cuándo usar cada motor?

| Necesidad | Motor | Archivo Componente | Spec Recomendada |
|---|---|---|---|
| Arquitectura de contenedores C4, microservicios AI, base de datos vectorial (ChromaDB), modelos LLM y Frontend Avatar 3D | **`FlowGraph`** | `FlowGraph.jsx` | `arquitecturaAsistente.js` |
| Flujos de Ingesta RAG, procesamiento de audio TTS/STT, y secuencias de Detección de Visión Artificial | **`SequenceDiagram`** | `SequenceDiagram.jsx` | `secuenciaRag.js` |

---

## ⚡ Reglas de Oro Geométricas y de Diseño

### 1. Sistema de Coordenadas en C4 / FlowGraph
* **Nodos = Coordenadas de Centroide (% del lienzo)**:
  `node.x` y `node.y` representan el **centro** de la caja. El CSS aplica `transform: translate(-50%, -50%)`. `node.w` y `node.h` son el ancho y alto en porcentaje.
* **Zonas = Esquina Superior Izquierda (% del lienzo)**:
  `zone.x` y `zone.y` son la esquina superior izquierda del `<rect>` SVG.
* **Margen Superior de Zona (Título)**:
  El título de una zona se dibuja en `(x + 14, y + 22)` dentro del marco. **Nunca coloques un nodo en `y < 14%` dentro de su zona**, o tapará el título.
* **Regla del 10% de Aire entre Cajas**:
  Si una arista con etiqueta (`label`) pasa entre dos nodos, debe haber al menos un **10% de separación vertical u horizontal**. Con separaciones del 5-7%, la etiqueta del chip ahoga la flecha o tapa las puntas.
* **Corredores de Ruteo (`via`)**:
  No cruces líneas diagonalmente sobre zonas o títulos ajenos. Usa puntos intermedios `via: [{ x, y }]` para hacer viajar la flecha por pasillos entre zonas (ej. 3-5% de ancho libre) o por bordes libres.

### 2. Reglas Temporales en Diagramas de Secuencia
* **Revelado Acumulativo**:
  En `SequenceDiagram`, los mensajes de pasos anteriores permanecen visibles pero atenuados; los del paso activo brillan en cyan (`var(--uti-cyan)`). Los pasos futuros se ocultan con `opacity: 0`.
* **Orden de Actores para Cero Cruces**:
  Ordena los actores en el array `actors` en función de la secuencia natural de llamadas para evitar que las líneas de mensaje crucen líneas de vida intermedias.

### 3. Flujo y Narrativa de Sustentación
* **Autoplay no invasivo**: Cada slide inicia en el paso 0 y reproduce automáticamente con `spec.interval` (2400-2800 ms).
* **Controles de Teclado**:
  - `↑` / `↓`: Retroceder / Avanzar paso a paso manualmente (cancela el autoplay).
  - `R`: Reiniciar la animación desde el inicio.

---

## 🛠️ Procedimiento Paso a Paso para Crear un Diagrama

### Paso 1: Crear la Spec
Crea un nuevo archivo en `Presentacion/src/flows/specs/<nombre>.js`.

### Paso 2: Verificar Iconos
Si tu diagrama necesita nuevos iconos (ej. `Brain`, `Database`, `User`, `Camera`):
1. Revisa `icons.js` en tu proyecto `Presentacion/src/flows/icons.js`.
2. Si el icono de Lucide no está registrado, impórtalo y agrégalo a `FLOW_ICONS`.

### Paso 3: Definir las Etapas Narrativas (`steps`)
Cada etapa debe aportar valor a la exposición oral:
- `id`: Slug único.
- `label`: Título corto para el botón del stepper.
- `detail`:
  - `title`: Frase conceptual clara.
  - `bullets`: 2 a 4 viñetas de sustento técnico con terminología precisa.
  - `code`: (Opcional) Ej. fragmento JSON de embedding o prompt.

### Paso 4: Integrar en la Diapositiva correspondiente (`App.jsx`)
Importa el componente y la spec para renderizarlo.
