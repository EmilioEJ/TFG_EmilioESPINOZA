/**
 * Plantilla base para Diagramas de Secuencia Temporal (SequenceDiagram).
 *
 * Instrucciones:
 * 1. Ordena los `actors` de izquierda a derecha según el flujo natural de mensajes.
 * 2. Utiliza `kind: 'call'` para peticiones directas y `kind: 'return'` para respuestas.
 * 3. Utiliza `kind: 'self'` para lógica interna en un componente.
 * 4. Utiliza `kind: 'note'` con `over: ['ACTOR_A', 'ACTOR_B']` para destacar conceptos clave.
 * 5. Cada mensaje debe asignarse al menos a un step para asegurar su revelado progresivo.
 */

export const miSecuenciaSpec = {
  id: 'ejemplo_seq',
  interval: 2600, // milisegundos por etapa en autoplay

  // Actores y líneas de vida (distribuidos automáticamente en el eje horizontal)
  actors: [
    { id: 'CLI', label: 'Cliente / Sensor', sub: 'ESP32 / Postman', icon: 'Cpu' },
    { id: 'GW', label: 'Proxy / Gateway', sub: 'Traefik v3', icon: 'Lock' },
    { id: 'API', label: 'Servicio API', sub: 'FastAPI :8000', icon: 'Server' },
    { id: 'DB', label: 'Base de Datos', sub: 'TimescaleDB', icon: 'Database' }
  ],

  // Mensajes ordenados cronológicamente de arriba hacia abajo
  messages: [
    { id: 'm1', kind: 'call', from: 'CLI', to: 'GW', label: 'POST /api/v1/telemetry', sub: 'Bearer token + JSON' },
    { id: 'm2', kind: 'call', from: 'GW', to: 'API', label: 'Proxy reverse', sub: 'TLS terminado' },
    { id: 'n1', kind: 'note', over: ['API'], label: 'Verificación de token y schema Pydantic' },
    { id: 'm3', kind: 'call', from: 'API', to: 'DB', label: 'INSERT INTO readings' },
    { id: 'm4', kind: 'return', from: 'DB', to: 'API', label: '201 Created — id: 48912' },
    { id: 'm5', kind: 'self', from: 'API', label: 'pg_notify("new_reading")' },
    { id: 'm6', kind: 'return', from: 'API', to: 'GW', label: '200 OK' },
    { id: 'm7', kind: 'return', from: 'GW', to: 'CLI', label: '200 OK { success: true }' }
  ],

  // Etapas acumulativas para la defensa oral
  steps: [
    {
      id: 'peticion',
      label: '1. Envío inicial',
      messages: ['m1', 'm2'],
      actors: ['CLI', 'GW', 'API'],
      detail: {
        title: 'Llegada de la trama de datos',
        bullets: [
          'El cliente remoto envía la carga útil firmada a través del puerto seguro HTTPS 443.',
          'Traefik verifica los certificados TLS y reenvía internamente la petición a la red privada de FastAPI.'
        ],
        code: 'POST /api/v1/telemetry'
      }
    },
    {
      id: 'procesamiento',
      label: '2. Ingesta y persistencia',
      messages: ['n1', 'm3', 'm4'],
      actors: ['API', 'DB'],
      detail: {
        title: 'Validación en memoria y escritura transaccional',
        bullets: [
          'La API comprueba la integridad del token Bearer del dispositivo antes de tocar la base de datos.',
          'Se inserta la lectura en la hypertable particionada por tiempo de TimescaleDB.'
        ],
        code: 'INSERT INTO readings (ts, device_identifier, value)'
      }
    },
    {
      id: 'reactividad',
      label: '3. Notificación y respuesta',
      messages: ['m5', 'm6', 'm7'],
      actors: ['API', 'GW', 'CLI'],
      detail: {
        title: 'Disparo asíncrono y confirmación',
        bullets: [
          'Un trigger interno notifica a los hilos de WebSocket para actualización reactiva sin polling.',
          'El cliente recibe inmediatamente el código de éxito HTTP 200 con confirmación de almacenamiento.'
        ],
        code: 'pg_notify("new_reading", payload)'
      }
    }
  ]
};

export default miSecuenciaSpec;
