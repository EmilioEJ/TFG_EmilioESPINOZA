# Manual Técnico de Grafos C4 y Flujos de Arquitectura (`FlowGraph`)

El componente [FlowGraph.jsx](file:///home/em1lio/TESIS/SISTEMA_TESIS/presentacion/src/flows/FlowGraph.jsx) renderiza diagramas de arquitectura en capas (estilo Contenedores C4 de Simon Brown), redes industriales y pipelines de datos con animación de partículas en tiempo real.

---

## 📐 1. Estructura de la Especificación (`spec`)

Un diagrama de grafo se define como un objeto JavaScript puro con la siguiente anatomía:

```javascript
export const miArquitecturaSpec = {
  id: 'mi_arq',                    // Prefijo único para IDs SVG (evita colisión de marcadores)
  viewBox: { w: 1000, h: 600 },    // Dimensiones lógicas (1000x600 mantiene proporción 1.66 / 1.79)
  interval: 2600,                  // Tiempo de permanencia por etapa en ms durante autoplay
  particleDur: '1.5s',             // (Opcional) Duración del ciclo de viaje de partículas (def: 1.5s)

  zones: [ ... ],                  // Agrupaciones de fondo (redes, zonas de seguridad, capas)
  nodes: [ ... ],                  // Cajas de servicios, hardware, bases de datos o contenedores
  edges: [ ... ],                  // Flechas direccionales con protocolo y ruteo
  steps: [ ... ]                   // Secuencia narrativa paso a paso
};
```

---

## 🎨 2. Zonas de Fondo (`zones`)

Las zonas agrupan visualmente los componentes según su ubicación física, de red o de seguridad.

```javascript
zones: [
  {
    id: 'industrial',
    label: 'Planta Industrial',
    x: 1,      // % horizontal (esquina superior izquierda)
    y: 10,     // % vertical (esquina superior izquierda)
    w: 22,     // % ancho
    h: 80,     // % alto
    tone: 'green' // Paleta de color
  }
]
```

### Tonos disponibles (`tone`)
Cada tono define variables CSS `--zone-fill` y `--zone-stroke`:
* `green`: Entorno físico de planta / sensores (verde industrial `#16A34A` / `#F0FDF4`).
* `blue`: Capa Edge / Puertas de enlace (azul tecnológico `#2563EB` / `#EFF6FF`).
* `slate`: Contenedores Docker / Servidor VPS neutro (gris `#94A3B8` / `#F8FAFC`).
* `red`: Backend / API / Zona crítica (rojo `#EF4444` / `#FEF2F2`).
* `amber`: Servicios externos / Redes WAN / Broker (ámbar `#D97706` / `#FFFBEB`).
* `purple`: Módulos de analítica / Tiempo real / Alertas (morado `#7E22CE` / `#FAF5FF`).

> [!WARNING]
> **Espacio reservado para el título de la zona**:
> El título se dibuja automáticamente en SVG en `(x + 14, y + 22)` con texto de 13 px en mayúsculas. Ningún nodo debe colocarse a menos de un 14% de la parte superior de la zona para evitar que la caja tape las letras.

---

## 📦 3. Nodos de Arquitectura (`nodes`)

Los nodos son elementos HTML posicionados en capa superior sobre el SVG para garantizar tipografía nítida y auto-ajuste de texto.

```javascript
nodes: [
  {
    id: 'PLC',
    x: 12,                  // % Centroide horizontal (cx)
    y: 35,                  // % Centroide vertical (cy)
    w: 15,                  // % Ancho de la caja
    h: 18,                  // % Alto de la caja
    icon: 'Factory',        // Clave del icono en icons.js
    title: 'PLC Siemens S7',// Título principal
    tech: 'Modbus TCP :502',// Subtítulo técnico monoespaciado
    detail: 'Holding Regs'  // (Opcional) Detalle adicional
  }
]
```

### Reglas críticas de nodos
1. **Coordenadas al Centro**: `x` e `y` son el **centro geométrico** de la caja (porque la clase `.flow-node` tiene `transform: translate(-50%, -50%)`).
2. **Dimensiones mínimas legibles**: Ancho recomendado entre 11% y 18%; alto entre 12% y 22%. Si el texto técnico es largo, es preferible aumentar el ancho `w` a reducir el texto.

---

## 🔗 4. Aristas, Ruteo y Geometría (`edges`)

Las aristas se calculan en [geometry.js](file:///home/em1lio/TESIS/SISTEMA_TESIS/presentacion/src/flows/geometry.js):

```javascript
edges: [
  {
    id: 'plc-agent',
    from: 'PLC',
    to: 'EDGE_AGENT',
    label: 'Modbus TCP',     // Texto sobre el chip de la flecha
    labelAt: 0.5,            // Fracción del recorrido (0.0 = inicio, 1.0 = fin, def: 0.5)
    via: [                   // Puntos de quiebre (en % del viewBox)
      { x: 22, y: 35 },
      { x: 22, y: 65 }
    ]
  }
]
```

### Cómo funciona el cálculo geométrico
1. **Ray-Casting perimetral (`anchor`)**:
   La función calcula la intersección exacta entre el vector `centro_origen → primer_objetivo` y el contorno rectangular del nodo, añadiendo un `gap: 7px`. La flecha sale y entra rozando el borde de la caja, sin penetrar en el contenido.
2. **Curvas suavizadas cuadráticas (`roundedPath`)**:
   Los puntos intermedios (`via`) no forman esquinas en ángulo recto agresivo; se redondean con un radio cuadrático de `16px`.
3. **Colocación automática de etiquetas sin colisiones (`layoutLabels`)**:
   En cada etapa, el motor prueba múltiples candidatos (`t` a lo largo de la curva y desplazamientos perpendiculares `nivel`).
   - Penaliza colisiones contra cajas de nodos (`coste += overlap * 60`).
   - Penaliza colisiones contra títulos de zonas (`coste += overlap * 30`).
   - Penaliza colisiones contra líneas de otras aristas (`coste += 700`).
   - Penaliza tapar la punta o el inicio de la flecha (`coste += 900`).
   - Si la etiqueta debe apartarse a más de 16 px del ancla para evitar chocar, dibuja automáticamente una línea guía o **tirante** (`flow-edge-leader`).

---

## 🌊 5. Partículas de Datos en Movimiento

Cuando una arista está activa en el paso actual (`activeEdges.has(e.id)`), `FlowGraph` inyecta automáticamente el componente `EdgeParticles`:

```jsx
const PARTICLE_OFFSETS = ['0s', '0.75s'];

const EdgeParticles = ({ pathId, dur }) =>
  PARTICLE_OFFSETS.map((begin) => (
    <circle key={begin} className="flow-particle" r="6">
      <animateMotion dur={dur} begin={begin} repeatCount="indefinite" calcMode="linear">
        <mpath href={`#${pathId}`} xlinkHref={`#${pathId}`} />
      </animateMotion>
    </circle>
  ));
```

* **Doble desfase (`0s` y `0.75s`)**: Evita el efecto de "una sola bolita perdida" y genera la ilusión visual de un caudal o flujo continuo de paquetes.
* **Corte por accesibilidad**: Si el sistema operativo tiene activado `prefers-reduced-motion: reduce`, las partículas se desactivan automáticamente.

---

## 🚨 6. Estados de Falla y Simulación de Caídas

Para ilustrar resiliencia, pérdida de enlace o servidores caídos (como en el ensayo de 12 horas de Store-and-Forward):

```javascript
steps: [
  {
    id: 'corte',
    label: 'Corte de WAN (12 h)',
    nodes: ['SENSOR', 'AGENT', 'SQLITE'],
    edges: ['sensor-agent', 'agent-sqlite', 'agent-wan'],
    // Estados visuales de nodos:
    nodeStates: {
      WAN: 'down',   // Borde rojo punteado, icono rojo de alarma
      API: 'off',    // Atenuado al 15% de opacidad
      DB: 'off'
    },
    // Estados visuales de aristas:
    edgeStates: {
      'agent-wan': 'blocked' // Interrumpe la línea y dibuja un disco rojo con una 'X'
    },
    detail: { ... }
  }
]
```

* **Aspa de corte (`is-blocked`)**: Se dibuja exactamente en el punto medio geométrico del trazo (`midX`, `midY`). No se generan partículas sobre enlaces cortados.

---

## 📋 7. Lista de Chequeo para Grafos C4 Impecables

1. ¿Las cajas adyacentes tienen al menos **10% de separación** si una flecha etiquetada pasa entre ellas?
2. ¿Los nodos superiores están por debajo de `y = 15%` de su zona para no pisar el rótulo de la zona?
3. ¿Las aristas largas usan `via` para viajar por pasillos en lugar de cortar cajas diagonalmente?
4. ¿Los nombres de iconos en `spec.nodes` están presentes en `icons.js`?
5. ¿Cada paso (`step`) tiene un `detail` con viñetas técnicas útiles para sustentar oralmente?
