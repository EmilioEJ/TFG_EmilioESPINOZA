/* Reactividad en tiempo real y alertas descentralizadas (Figura 5 de la tesis).
   Transcrito de TESIS/Capítulos/fig/fig_secuencia_alertas_telegram.mmd; la rama alt del
   diagrama de secuencia se representa aquí como bifurcación del motor de alertas.

   Verificado contra el código: el canal es 'new_reading' (ws_manager.py:65), el trigger es
   trg_notify_reading_insert AFTER INSERT FOR EACH ROW (init_db.py:205) y el umbral de agregación
   es range > 60 min (ModularDashboard.tsx:116). El motor de alertas NO escribe en audit_logs
   —'alert.triggered' no existe en el backend—, por eso ese nodo no aparece aquí. */

export const tiempoRealSpec = {
  id: 'rt',
  /* 1000×600 = la misma proporción que el hueco disponible en la diapositiva, así que el
     diagrama lo llena en vez de dejar una franja muerta abajo. */
  viewBox: { w: 1000, h: 600 },
  interval: 2600,

  zones: [
    /* Cada zona reserva una banda superior libre: su título se pinta DENTRO del recuadro, y
       si un nodo empieza a esa altura lo tapa. Por eso ninguna caja arranca antes del 14 %
       de su zona. */
    { id: 'ingesta', label: 'Ingesta', x: 1, y: 10, w: 41, h: 38, tone: 'blue' },
    { id: 'realtime', label: 'Camino en tiempo real — sin polling', x: 66, y: 5, w: 33, h: 32, tone: 'purple' },
    { id: 'alerting', label: 'Camino de alertas', x: 36, y: 54, w: 63, h: 34, tone: 'amber' }
  ],

  nodes: [
    /* La fila de ingesta se separa hasta dejar ~6 % de hueco entre caja y caja: es donde
       tienen que caber "MQTT / REST" e "INSERT readings", que antes acababan encima de las
       propias cajas por falta de sitio. La base de datos, además, se apartó del bloque de
       tiempo real: pegada a él la flecha del NOTIFY medía 11 unidades y no se veía. */
    { id: 'DEVICE', x: 9, y: 30, w: 15, h: 13, icon: 'Cpu', title: 'Dispositivo / Gateway', tech: 'MQTT · /edge/sync' },
    { id: 'API', x: 32, y: 30, w: 15, h: 13, icon: 'Server', title: 'Backend / MQTT Worker', tech: 'INSERT INTO readings' },
    { id: 'DB', x: 53, y: 30, w: 15, h: 15, icon: 'Database', title: 'PostgreSQL / TimescaleDB', tech: 'Trigger AFTER INSERT', detail: "pg_notify('new_reading')" },
    { id: 'WS', x: 75, y: 22, w: 14, h: 13, icon: 'Activity', title: 'WebSocket Manager', tech: 'LISTEN new_reading' },
    { id: 'REACT', x: 92, y: 22, w: 13, h: 15, icon: 'LayoutDashboard', title: 'Dashboard React', tech: '15 ms de mediana' },
    { id: 'ALERT', x: 46, y: 72, w: 16, h: 15, icon: 'Bell', title: 'Alert Engine', tech: 'umbral + cooldown' },
    { id: 'TG', x: 72, y: 66, w: 14, h: 13, icon: 'Bot', title: 'Telegram Bot API', tech: 'sendMessage' },
    { id: 'OPER', x: 92, y: 66, w: 12, h: 13, icon: 'Smartphone', title: 'Operador', tech: 'Push en el móvil' }
  ],

  edges: [
    { id: 'dev-api', from: 'DEVICE', to: 'API', label: 'MQTT / REST' },
    { id: 'api-db', from: 'API', to: 'DB', label: 'INSERT readings' },
    { id: 'db-ws', from: 'DB', to: 'WS', label: 'NOTIFY' },
    { id: 'ws-react', from: 'WS', to: 'REACT', label: 'WSS' },
    /* Baja primero y entra al camino de alertas por su costado izquierdo. En diagonal directa
       cruzaba el rótulo "CAMINO DE ALERTAS", que se pinta en la banda superior de esa zona. */
    { id: 'api-alert', from: 'API', to: 'ALERT', label: 'Evalúa reglas', via: [{ x: 32, y: 68 }] },
    { id: 'alert-db', from: 'ALERT', to: 'DB', label: 'SELECT alert_rules', labelAt: 0.55, via: [{ x: 64, y: 62 }] },
    { id: 'alert-tg', from: 'ALERT', to: 'TG', label: 'sendMessage' },
    { id: 'tg-oper', from: 'TG', to: 'OPER', label: 'Push' }
  ],

  steps: [
    {
      id: 'ingesta',
      label: 'Ingesta de la lectura',
      nodes: ['DEVICE', 'API', 'DB'],
      edges: ['dev-api', 'api-db'],
      detail: {
        title: 'Una lectura entra por cualquiera de las dos vías',
        bullets: [
          'Da igual si llegó por MQTT en tiempo real o en un lote diferido de /edge/sync: el destino es la misma hypertable.',
          'La fila queda escrita en readings con su company_id, que es lo que garantiza el aislamiento entre inquilinos.'
        ],
        code: 'INSERT INTO readings (ts, device_identifier, variable, value)'
      }
    },
    {
      id: 'notify',
      label: 'Trigger y NOTIFY',
      nodes: ['DB', 'WS'],
      edges: ['db-ws'],
      detail: {
        title: 'La propia base de datos avisa a quien escucha',
        bullets: [
          'El trigger PL/pgSQL trg_notify_reading_insert ejecuta pg_notify tras cada fila insertada (AFTER INSERT FOR EACH ROW).',
          'El WebSocketManager mantiene un LISTEN permanente sobre el canal new_reading, con reconexión automática.',
          'Esto sustituye a un broker externo: no hay Redis ni RabbitMQ que desplegar, monitorizar ni pagar.'
        ],
        code: "pg_notify('new_reading', payload_json)"
      }
    },
    {
      id: 'stream',
      label: 'Stream al dashboard',
      nodes: ['WS', 'REACT'],
      edges: ['ws-react'],
      detail: {
        title: 'Del NOTIFY a la gráfica, sin preguntar',
        metric: { value: 15, label: 'ms de latencia mediana de la publicación a la pantalla (p95 34 ms)', suffix: ' ms', tone: 'green', animate: false },
        bullets: [
          'Cada cliente suscrito tiene su propia asyncio.Queue de 100 huecos; el dashboard conserva una ventana de 300 puntos en vivo.',
          'El canal se autentica con el JWT: el frontend lo envía en el subprotocolo Sec-WebSocket-Protocol, y el backend acepta también query param.',
          'Solo los rangos de 60 minutos o menos usan datos crudos; por encima, el frontend pide agregados con time_bucket.'
        ],
        code: 'WSS /api/v1/ws/devices/{device_identifier}/telemetry'
      }
    },
    {
      id: 'reglas',
      label: 'Motor de alertas',
      nodes: ['API', 'ALERT', 'DB'],
      edges: ['api-alert', 'alert-db'],
      detail: {
        title: 'En paralelo, se evalúan las reglas del dispositivo',
        bullets: [
          'Consulta las alert_rules activas del dispositivo: condición (>, <, >=, <=, ==), umbral y cooldown_minutes.',
          'El envío no bloquea la ingesta: el worker MQTT lo delega a un pool de 3 hilos y el camino /edge/sync lo hace de forma asíncrona con aiohttp.'
        ],
        code: 'SELECT alert_rules WHERE device_identifier = … AND is_active = TRUE'
      }
    },
    {
      id: 'notificacion',
      label: 'Notificación al operador',
      nodes: ['ALERT', 'TG', 'OPER'],
      edges: ['alert-tg', 'tg-oper'],
      detail: {
        title: 'Aviso directo al operador responsable',
        bullets: [
          'Cada usuario registra su propio bot: el token y el chat_id son suyos, no de un bot central de la plataforma.',
          'Si un usuario no ha configurado bot o chat_id, se le omite sin interrumpir el resto de notificaciones.'
        ],
        note: 'Si el cooldown sigue activo o no se supera el umbral, la notificación se suprime — es lo que evita la fatiga de alertas.'
      }
    }
  ]
};

export default tiempoRealSpec;
