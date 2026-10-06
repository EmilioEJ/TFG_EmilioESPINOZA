/* Diagrama de Contenedores C4 (Figura 2 de la tesis).
   Nodos y aristas transcritos de TESIS/Capítulos/fig/fig_diagrama_contenedores.mmd; las
   etiquetas de protocolo y endpoint provienen de TESIS/Contexto/docs/09_Arquitectura.md.
   Única simplificación: las dos aristas React→FastAPI del .mmd (REST y WebSocket) se
   dibujan como una sola, porque comparten origen y destino. */

export const arquitecturaSpec = {
  id: 'arq',
  viewBox: { w: 1000, h: 600 },
  interval: 2600,

  zones: [
    { id: 'industrial', label: 'Industrial', x: 1, y: 10, w: 14, h: 78, tone: 'green' },
    { id: 'edge', label: 'Edge (borde)', x: 18.5, y: 10, w: 13, h: 78, tone: 'blue' },
    { id: 'docker', label: 'Docker Compose — VPS', x: 36.5, y: 2, w: 48.5, h: 95, tone: 'slate' },
    { id: 'backend', label: 'Backend FastAPI :8000', x: 55.5, y: 15, w: 17.5, h: 58, tone: 'red' },
    { id: 'external', label: 'Externos', x: 87, y: 10, w: 12, h: 78, tone: 'amber' }
  ],

  nodes: [
    { id: 'PLC', x: 8, y: 32, w: 12, h: 22, icon: 'Factory', title: 'PLC / Sensor industrial', tech: 'Modbus TCP esclavo', detail: 'Holding Registers 0–4' },
    { id: 'ARDUINO', x: 8, y: 68, w: 11, h: 20, icon: 'CircuitBoard', title: 'Arduino Nano + DHT11', tech: 'Serial JSON' },
    { id: 'ESP', x: 25, y: 32, w: 12, h: 22, icon: 'Cpu', title: 'ESP32 + sensores', tech: 'MQTT Publisher', detail: 'Portal WiFiManager' },
    { id: 'EDGE_AGENT', x: 25, y: 68, w: 12, h: 24, icon: 'HardDrive', title: 'Edge Agent Python', tech: 'Store-and-Forward', detail: 'SQLite WAL' },
    /* La columna central se reparte el alto en cuatro filas con ~10 % de aire entre caja y
       caja. Ese hueco no es estético: es el sitio donde tiene que caber el rótulo de la
       flecha que las une. Con la separación anterior (7 %) la flecha medía 21 unidades y
       cualquier rótulo la tapaba entera. Traefik arranca en y=15 para no pisar el título de
       la zona Docker, que se pinta dentro del recuadro y llega hasta y≈7. */
    { id: 'TRAEFIK', x: 45, y: 15, w: 16, h: 12, icon: 'Lock', title: 'Traefik v3', tech: 'TLS · :443 y :8883', detail: 'Única entrada pública' },
    { id: 'MQTT', x: 45, y: 39, w: 14, h: 16, icon: 'Radio', title: 'Eclipse Mosquitto', tech: ':1883 / :9001 WS', detail: 'Plugin go-auth' },
    { id: 'WORKER', x: 45, y: 65, w: 14, h: 16, icon: 'RefreshCw', title: 'MQTT Worker', tech: 'paho-mqtt', detail: 'Contenedor propio' },
    { id: 'DB', x: 52, y: 90, w: 22, h: 13, icon: 'Database', title: 'TimescaleDB', tech: 'PostgreSQL 15 · :5432', detail: 'Trigger NOTIFY' },
    { id: 'API', x: 64.25, y: 27, w: 15, h: 14, icon: 'Server', title: 'REST API / WebSocket', tech: '/api/v1/*' },
    { id: 'ALERT', x: 64.25, y: 45, w: 14, h: 14, icon: 'Bell', title: 'Alert Engine', tech: 'Notificador Telegram' },
    { id: 'WS_MGR', x: 64.25, y: 64, w: 14, h: 14, icon: 'Activity', title: 'WebSocket Manager', tech: 'LISTEN / NOTIFY' },
    { id: 'FRONT', x: 81, y: 45, w: 8, h: 15, icon: 'LayoutDashboard', title: 'SPA React 18', tech: 'Nginx :80' },
    { id: 'TG', x: 93, y: 25, w: 10, h: 16, icon: 'Bot', title: 'Telegram Bot API' }
  ],

  edges: [
    { id: 'plc-agent', from: 'PLC', to: 'EDGE_AGENT', label: 'Modbus TCP :502', via: [{ x: 16.75, y: 48 }] },
    { id: 'ard-agent', from: 'ARDUINO', to: 'EDGE_AGENT', label: 'Serial' },
    { id: 'esp-traefik', from: 'ESP', to: 'TRAEFIK', label: 'MQTTS :8883', labelAt: 0.6 },
    { id: 'traefik-mqtt', from: 'TRAEFIK', to: 'MQTT', label: ':1883' },
    /* El tramo vertical corre por el pasillo entre la zona Edge y la de Docker. Ese pasillo
       medía 2,5 % del lienzo: la flecha salía pegada a los dos bordes discontinuos y su
       rótulo los cruzaba. Estrechando la zona Edge queda en 5 %, con aire a ambos lados. */
    { id: 'agent-traefik', from: 'EDGE_AGENT', to: 'TRAEFIK', label: 'HTTPS :443', labelAt: 0.5, via: [{ x: 34, y: 68 }, { x: 34, y: 15 }] },
    /* Baja por el corredor que queda entre la columna central (acaba en x=52) y la zona del
       backend (empieza en 55,5), y entra a la API por su costado izquierdo. Bajando por dentro
       de la zona, como hacía antes, la flecha atravesaba el rótulo "BACKEND FASTAPI :8000",
       que se pinta a lo ancho de todo su borde superior. */
    { id: 'traefik-api', from: 'TRAEFIK', to: 'API', label: 'POST /edge/sync', labelAt: 0.6, via: [{ x: 53.9, y: 15 }, { x: 53.9, y: 27 }] },
    { id: 'mqtt-api', from: 'MQTT', to: 'API', label: 'auth + ACL', labelAt: 0.5 },
    { id: 'mqtt-worker', from: 'MQTT', to: 'WORKER', label: 'v1/devices/+/telemetry' },
    { id: 'worker-db', from: 'WORKER', to: 'DB', label: 'INSERT readings' },
    { id: 'worker-alert', from: 'WORKER', to: 'ALERT', label: 'Evalúa' },
    /* Sube por el corredor izquierdo (entre la columna central, que acaba en x=52, y la zona
       del backend, que empieza en 55,5) y entra a la API por ese mismo lado. Subiendo por el
       corredor derecho cortaba en dos la diagonal de ws-front, y los rótulos SQL y WSS
       quedaban amontonados sobre el mismo trazo sin saber cuál era de cuál. */
    { id: 'db-api', from: 'DB', to: 'API', label: 'SQL', labelAt: 0.55, via: [{ x: 53.9, y: 78 }, { x: 53.9, y: 30 }] },
    /* Anclado cerca del WebSocket Manager: en el punto medio caia sobre la vertical de
       db-api, que arranca de la misma caja, y no se sabia de cual de las dos era. */
    { id: 'db-ws', from: 'DB', to: 'WS_MGR', label: 'NOTIFY new_reading', labelAt: 0.72 },
    { id: 'ws-front', from: 'WS_MGR', to: 'FRONT', label: 'WSS', labelAt: 0.5 },
    { id: 'alert-tg', from: 'ALERT', to: 'TG', label: 'sendMessage', labelAt: 0.55 },
    /* Sube por el eje del dashboard y entra a la API por arriba, no por el corredor de
       db-api: así las dos verticales quedan a 6 % una de otra y no se confunden. */
    { id: 'front-api', from: 'FRONT', to: 'API', label: 'REST + WSS', labelAt: 0.5, via: [{ x: 81, y: 21 }] }
  ],

  steps: [
    {
      id: 'adquisicion',
      label: 'Adquisición en planta',
      nodes: ['PLC', 'ARDUINO', 'EDGE_AGENT'],
      edges: ['plc-agent', 'ard-agent'],
      detail: {
        title: 'La señal física entra al sistema',
        bullets: [
          'agent_plc_modbus.py actúa de maestro Modbus TCP y lee los registros 0–4 del PLC: temperatura, humedad, presión, vibración y voltaje.',
          'Para el Arduino Nano hay un agente distinto, agent_serial.py, que consume tramas JSON línea a línea por el puerto serie USB.',
          'Sea cual sea el agente, la Raspberry Pi estampa la marca de tiempo ISO 8601 UTC en el momento del muestreo.'
        ],
        code: 'read_holding_registers(address=0, count=5, slave=1)'
      }
    },
    {
      id: 'transporte',
      label: 'Publicación MQTT y autenticación',
      nodes: ['ESP', 'TRAEFIK', 'MQTT', 'API'],
      edges: ['esp-traefik', 'traefik-mqtt', 'mqtt-api'],
      detail: {
        title: 'El ESP32 publica y el broker delega la autenticación',
        bullets: [
          'Nada del VPS se expone directamente: todos los puertos están atados a localhost y Traefik es la única puerta desde internet.',
          'El ESP32 conecta por MQTTS al 8883, donde Traefik termina el TLS y reenvía al 1883 del broker dentro de la red Docker.',
          'Publica en su tópico exclusivo v1/devices/{device_identifier}/telemetry con QoS 0.',
          'No hay contraseñas estáticas: mosquitto-go-auth consulta al backend, con username = device_identifier y password = device_token.'
        ],
        code: 'POST /api/v1/mqtt/auth  ·  POST /api/v1/mqtt/acl'
      }
    },
    {
      id: 'sync',
      label: 'Sincronización diferida',
      nodes: ['EDGE_AGENT', 'TRAEFIK', 'API'],
      edges: ['agent-traefik', 'traefik-api'],
      detail: {
        title: 'La vía resiliente: lotes firmados por HTTPS',
        bullets: [
          'Cuando el enlace WAN cae, el agente retiene la telemetría en SQLite WAL y la reenvía al reconectar.',
          'Cada lote viaja firmado con HMAC-SHA256 en la cabecera X-HMAC-Signature.',
          'El dispositivo se identifica con su device_token en Authorization: Bearer, no con un JWT de usuario.',
          'Traefik publica también el 443 del dashboard, que Nginx sirve junto al proxy hacia la API.'
        ],
        code: 'POST /api/v1/edge/sync'
      }
    },
    {
      id: 'ingesta',
      label: 'Procesamiento e ingesta',
      nodes: ['MQTT', 'WORKER', 'DB'],
      edges: ['mqtt-worker', 'worker-db'],
      detail: {
        title: 'Un contenedor dedicado consume y persiste',
        bullets: [
          'iiot_mqtt_worker se suscribe con QoS 1 al comodín v1/devices/+/telemetry.',
          'Auto-registra en device_variables cualquier variable nueva que detecte, sin tocar el firmware.',
          'Inserta en la hypertable readings, particionada automáticamente por ts.'
        ],
        code: 'PK (ts, device_identifier, variable)'
      }
    },
    {
      id: 'tiempo-real',
      label: 'Tiempo real al dashboard',
      nodes: ['DB', 'WS_MGR', 'FRONT', 'API'],
      edges: ['db-ws', 'ws-front', 'front-api', 'db-api'],
      detail: {
        title: 'La base de datos avisa; nadie hace polling',
        bullets: [
          'Un trigger PL/pgSQL emite pg_notify y el WebSocketManager, que mantiene un LISTEN abierto, lo recibe.',
          'Medido de extremo a extremo (publicación MQTT → pantalla): mediana de 15 ms y p95 de 34 ms sobre 90 muestras, frente al umbral de 10 s del RNF-01.5.',
          'Rangos mayores a 60 min no usan WebSocket: el frontend consulta el endpoint de agregados.'
        ],
        code: "LISTEN new_reading → broadcast_local()"
      }
    },
    {
      id: 'alertas',
      label: 'Motor de alertas',
      nodes: ['WORKER', 'ALERT', 'TG'],
      edges: ['worker-alert', 'alert-tg'],
      detail: {
        title: 'Notificación descentralizada por Telegram',
        bullets: [
          'El worker delega la evaluación de reglas a un pool de hilos para no bloquear la ingesta.',
          'Cada usuario registra su propio telegram_bot_token y chat_id: las alertas no pasan por un bot central.',
          'El cooldown (15 min por defecto) evita la fatiga de alertas.'
        ]
      }
    }
  ]
};

export default arquitecturaSpec;
