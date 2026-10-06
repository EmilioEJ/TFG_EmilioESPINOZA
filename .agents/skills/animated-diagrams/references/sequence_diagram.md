# Manual Técnico de Diagramas de Secuencia Temporal (`SequenceDiagram`)

El componente [SequenceDiagram.jsx](file:///home/em1lio/TESIS/SISTEMA_TESIS/presentacion/src/flows/SequenceDiagram.jsx) implementa diagramas de secuencia UML animados y acumulativos para protocolos de red, intercambios criptográficos y transacciones distribuidas (ej. Diapositiva 13: *Autenticación y Autorización MQTT*).

A diferencia de los diagramas de grafo donde las cajas están dispersas en un plano 2D, aquí **el eje vertical representa el avance irreversible del tiempo**.

---

## 📐 1. Estructura de la Especificación (`spec`)

Un diagrama de secuencia se define como:

```javascript
export const miSecuenciaSpec = {
  id: 'auth_seq',       // Prefijo único para marcadores SVG de flechas
  interval: 2600,       // Tiempo de permanencia por etapa durante autoplay (ms)

  actors: [ ... ],      // Líneas de vida verticales (participantes)
  messages: [ ... ],    // Lista ordenada cronológicamente de mensajes e interacciones
  steps: [ ... ]        // Agrupación narrativa por etapas
};
```

---

## 👥 2. Actores y Líneas de Vida (`actors`)

Los actores se distribuyen de forma automática y equitativa a lo largo del ancho del lienzo:

```javascript
actors: [
  { id: 'D', label: 'Dispositivo', sub: 'ESP32 / Gateway', icon: 'Cpu' },
  { id: 'M', label: 'Mosquitto', sub: 'plugin go-auth', icon: 'Radio' },
  { id: 'B', label: 'Backend FastAPI', sub: 'auth y ACL', icon: 'Server' },
  { id: 'W', label: 'MQTT Worker', sub: 'iiot_mqtt_worker', icon: 'RefreshCw' },
  { id: 'DB', label: 'TimescaleDB', sub: 'PostgreSQL 15', icon: 'Database' }
]
```

### Cálculo de Carriles (`Lanes`)
* Ancho lógico total: `VB_W = 1000`.
* Ancho de carril por actor: `lane = VB_W / actors.length`.
* Posición horizontal del actor `i`: `x = (i + 0.5) * lane`.
* Cada actor genera una línea de vida vertical punteada (`flow-lifeline`) desde `y = 106` hasta el pie del diagrama.

> [!TIP]
> **Estrategia para minimizar cruces de líneas de vida**:
> Ordena los elementos en el array `actors` en función del flujo de llamadas más frecuente. Si el flujo típico es `Dispositivo → Broker → Backend → Base de Datos`, ese debe ser su orden físico de izquierda a derecha. Si un actor del centro interactúa con los dos extremos, ponlo en medio.

---

## 💬 3. Tipos de Mensajes (`messages`)

Cada mensaje ocupa una fila horizontal fija (`ROW_H = 46px`). El alto total del SVG se ajusta dinámicamente según el número de mensajes:
`vbH = HEADER_H (118) + messages.length * 46 + PAD_BOTTOM (26)`.

Existen 4 tipos (`kind`) soportados:

### A. Llamada Directa (`kind: 'call'`)
Flecha sólida direccional entre dos actores.
```javascript
{
  id: 'm1',
  kind: 'call',
  from: 'D',
  to: 'M',
  label: 'CONNECT',
  sub: 'username y password del dispositivo' // Subtítulo opcional debajo de la línea
}
```
* Etiqueta principal centrada en `y - 9px`.
* Subtítulo secundario centrado en `y + 15px`.
* Punta de flecha orientada hacia el destino (`dir = to > from ? 1 : -1`).

### B. Retorno / Respuesta (`kind: 'return'`)
Línea discontinua con respuesta síncrona o acuse de recibo.
```javascript
{
  id: 'm3',
  kind: 'return',
  from: 'B',
  to: 'M',
  label: '200 OK — credenciales válidas'
}
```
* En CSS aplica `stroke-dasharray: 7 5` (`.flow-msg.is-return`).

### C. Auto-llamada / Procesamiento Local (`kind: 'self'`)
Bucle lateral de ejecución interna en el mismo actor.
```javascript
{
  id: 'm12',
  kind: 'self',
  from: 'W',
  label: 'Evalúa alert_rules → Telegram'
}
```
* Dibuja un corchete SVG rectangular a la derecha de la línea de vida:
  `M x y-11 L x+w y-11 L x+w y+8 L x+4 y+8`.
* El texto se renderiza alineado a la izquierda (`style={{ textAnchor: 'start' }}`) con desplazamiento para evitar montarse sobre la flecha.

### D. Nota Flotante (`kind: 'note'`)
Tarjeta explicativa horizontal que abarca uno o varios actores contiguos.
```javascript
{
  id: 'n1',
  kind: 'note',
  over: ['M', 'B'], // Array de IDs de actores cubiertos
  label: 'go-auth delega la validación al backend'
}
```
* Dibuja una pastilla con fondo opaco y bordes redondeados (`rx="8"`), ideal para destacar mecanismos asíncronos o plugins delegados.

---

## ⏳ 4. Lógica de Revelado Acumulativo (`steps`)

En un protocolo temporal no tiene sentido "apagar" mensajes del pasado: si el dispositivo ya envió `CONNECT`, ese mensaje ocurrió y debe seguir visible en el historial del diagrama.

Por ello, `SequenceDiagram` implementa **revelado acumulativo**:

```javascript
/* Conjunto acumulativo de mensajes ocurridos hasta la etapa actual */
const revealed = new Set();
for (let i = 0; i <= step; i++) {
  steps[i].messages.forEach((id) => revealed.add(id));
}
```

### Tres estados de visibilidad de un mensaje
1. **Futuro** (`!revealed.has(m.id)`):
   Clase `.is-hidden`, `opacity: 0`. No distrae la atención de la audiencia.
2. **Histórico** (`revealed.has(m.id) && !activeMessages.has(m.id)`):
   Líneas y textos en gris neutro (`#94A3B8`). Queda como contexto del recorrido previo.
3. **Activo** (`activeMessages.has(m.id)`):
   Clase `.is-on`. Trazo reforzado a 3px y color corporativo naranja (`var(--uti-orange)`).

### Enfoque de Actores (`actors` en el step)
Si una etapa define `actors: ['M', 'B']`, los demás participantes no involucrados reciben la clase `.is-dim` (opacidad al 35%), guiando la vista del tribunal hacia la interacción relevante.

---

## 📋 5. Lista de Chequeo para Diagramas de Secuencia

1. ¿Los actores están ordenados para que la mayoría de mensajes vayan entre vecinos contiguos?
2. ¿Los mensajes de respuesta tienen `kind: 'return'` para verse punteados?
3. ¿Las llamadas internas usan `kind: 'self'` y su etiqueta es corta y legible?
4. ¿Las notas flotantes (`kind: 'note'`) definen actores válidos en `over`?
5. ¿Cada mensaje pertenece exactamente a un paso en el array `steps` para garantizar su revelado progresivo?
