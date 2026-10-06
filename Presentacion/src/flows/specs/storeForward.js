/* Store-and-Forward ante un corte de WAN de 12 h.
   Combina el flujograma decisional del agente (Figura 4, fig_flujo_edge_agent.mmd) con el
   mapeo temporal de la resincronización (Figura 7, fig_ejemplo_2.mmd). Las cifras de resultado
   salen de TESIS/Capítulos/03_Implementación.tex: corte de 12 h de reloj real, 43.015
   lecturas equivalentes a 86.030 puntos de dato, 0 % de pérdida y 0 % de duplicados.

   El agente representado es edge_agent/agents/agent_plc_modbus.py: es el que combina Modbus TCP
   con sincronización REST pura, que es lo que dibuja este diagrama. (maad_plc_dual.py lee Modbus
   ASCII por serie y publica en modo dual MQTT+REST; no es este flujo.)

   Los detalles operativos —nombre del caché, tamaño de lote, purga— están tomados del código,
   no de la memoria. Donde ambos difieren se citan los dos con su procedencia. */

export const storeForwardSpec = {
  id: 'sf',
  /* 1000×600 = la proporción del hueco de la diapositiva: el diagrama lo llena entero. */
  viewBox: { w: 1000, h: 600 },
  interval: 2800,

  zones: [
    { id: 'planta', label: 'Planta industrial', x: 1, y: 10, w: 42, h: 80, tone: 'green' },
    { id: 'wan', label: 'Enlace WAN', x: 45, y: 10, w: 13, h: 80, tone: 'amber' },
    { id: 'cloud', label: 'Nube — VPS', x: 60, y: 10, w: 39, h: 80, tone: 'purple' }
  ],

  nodes: [
    /* Ninguna caja arranca antes del 23 % de alto: por encima queda la banda donde se pintan
       los títulos de zona y donde tienen que caber los rótulos de las flechas horizontales,
       que en este diagrama son largos ("Lote firmado", "200 OK { inserted: N }"). */
    { id: 'SENSOR', x: 9.5, y: 36, w: 17, h: 16, icon: 'Gauge', title: 'Sensor / PLC', tech: 'Modbus TCP · HR 0–4' },
    { id: 'AGENT', x: 34, y: 36, w: 16, h: 18, icon: 'HardDrive', title: 'Edge Agent', tech: 'Raspberry Pi 3', detail: 'agent_plc_modbus.py' },
    { id: 'SQLITE', x: 34, y: 74, w: 16, h: 16, icon: 'Database', title: 'SQLite WAL', tech: 'plc_cache.db', detail: 'Máx. 50.000 filas · FIFO' },
    { id: 'WAN', x: 51.5, y: 36, w: 9, h: 13, icon: 'Wifi', title: 'WAN', tech: 'HTTPS' },
    { id: 'API', x: 79, y: 33, w: 28, h: 17, icon: 'Server', title: 'Backend FastAPI', tech: 'POST /api/v1/edge/sync', detail: 'Verifica device_token + HMAC' },
    { id: 'DB', x: 79, y: 73, w: 28, h: 17, icon: 'Database', title: 'TimescaleDB', tech: 'ON CONFLICT DO NOTHING', detail: 'PK (ts, device_identifier, variable)' }
  ],

  edges: [
    { id: 'sensor-agent', from: 'SENSOR', to: 'AGENT', label: 'cada 5 s' },
    { id: 'agent-sqlite', from: 'AGENT', to: 'SQLITE', label: 'INSERT en cache', via: [{ x: 30.5, y: 56 }] },
    { id: 'sqlite-agent', from: 'SQLITE', to: 'AGENT', label: 'SELECT pendientes', labelAt: 0.5, via: [{ x: 38, y: 56 }] },
    { id: 'agent-wan', from: 'AGENT', to: 'WAN', label: 'HTTPS' },
    { id: 'wan-api', from: 'WAN', to: 'API', label: 'Lote firmado' },
    { id: 'api-db', from: 'API', to: 'DB', label: 'INSERT idempotente' },
    /* El acuse vuelve por la banda alta, por encima de las cajas pero DENTRO de los recuadros.
       Antes pasaba por y=4, fuera de toda zona: se leía como una curva suelta que entraba y
       salía del diagrama sin que se supiera de dónde venía. */
    { id: 'api-ack', from: 'API', to: 'AGENT', label: '200 OK { inserted: N }', labelAt: 0.5, via: [{ x: 79, y: 19 }, { x: 34, y: 19 }] }
  ],

  steps: [
    {
      id: 'normal',
      label: 'Operación normal',
      nodes: ['SENSOR', 'AGENT', 'WAN', 'API', 'DB'],
      edges: ['sensor-agent', 'agent-wan', 'wan-api', 'api-db'],
      detail: {
        title: 'Con enlace activo, el dato va directo a la nube',
        bullets: [
          'El agente sondea el PLC cada 5 segundos y obtiene 5 variables por muestreo: temperatura, humedad, presión, vibración y voltaje.',
          'Cada variable se persiste como una fila propia, porque la clave primaria es (ts, device_identifier, variable).',
          'Latencia extremo a extremo estimada por suma de tramos: ≈ 330,8 ms.'
        ]
      }
    },
    {
      id: 'corte',
      label: 'Corte de WAN (12 h)',
      nodes: ['SENSOR', 'AGENT', 'SQLITE'],
      edges: ['sensor-agent', 'agent-sqlite', 'agent-wan'],
      nodeStates: { WAN: 'down', API: 'off', DB: 'off' },
      edgeStates: { 'agent-wan': 'blocked' },
      detail: {
        title: 'El enlace cae y el borde sigue midiendo',
        metric: { value: 43015, from: 0, label: 'lecturas retenidas en SQLite (86.030 puntos de dato)', tone: 'orange' },
        bullets: [
          'El ensayo decisivo no fue una simulación: doce horas de reloj real con el destino inalcanzable.',
          'Muestreando dos variables por segundo, el agente acumuló 43.015 lecturas — 86.030 puntos de dato.',
          'Se encolan en cache bajo transacción atómica, con PRAGMA journal_mode = WAL: un apagón no corrompe la base.',
          'Al llegar a 50.000 filas, purga por antigüedad hasta el 85 % de capacidad.'
        ],
        note: 'Una arquitectura cloud-céntrica pura lo habría perdido todo.'
      }
    },
    {
      id: 'reconexion',
      label: 'Reconexión detectada',
      nodes: ['AGENT', 'SQLITE', 'WAN'],
      edges: ['sqlite-agent'],
      detail: {
        title: 'El agente drena su caché local',
        bullets: [
          'Lee los registros pendientes y los agrupa en lotes de 20 muestreos (el ensayo de la memoria usó 100; el límite duro del endpoint son 500).',
          'Firma cada lote con HMAC-SHA256 sobre el cuerpo serializado, usando el secreto precompartido.',
          'Ante error de red reintenta con backoff exponencial, duplicando la espera hasta un techo de 30 s.'
        ],
        code: "hmac.new(secret, body, hashlib.sha256).hexdigest()"
      }
    },
    {
      id: 'envio',
      label: 'Envío firmado',
      nodes: ['AGENT', 'WAN', 'API'],
      edges: ['agent-wan', 'wan-api'],
      detail: {
        title: 'El backend verifica antes de aceptar nada',
        bullets: [
          'Identifica al dispositivo por su device_token en la cabecera Authorization: Bearer.',
          'Recupera el hmac_secret (cifrado en reposo con Fernet) y recalcula la firma sobre el cuerpo recibido.',
          'La firma es obligatoria: si falta o no coincide, responde 403 Forbidden.'
        ],
        code: 'X-HMAC-Signature: 9f2c…  ·  Authorization: Bearer …'
      }
    },
    {
      id: 'idempotencia',
      label: 'Idempotencia en dos niveles',
      nodes: ['API', 'DB'],
      edges: ['api-db'],
      detail: {
        title: 'Reenviar un lote nunca duplica ni redispara alertas',
        bullets: [
          'Nivel API: pg_advisory_xact_lock sobre el batch_id cortocircuita peticiones duplicadas.',
          'Nivel base de datos: la clave primaria compuesta y ON CONFLICT DO NOTHING descartan la inserción repetida.',
          'El batch_id es determinista, derivado del contenido del lote: no depende de expiración temporal.'
        ],
        code: 'INSERT … ON CONFLICT DO NOTHING'
      }
    },
    {
      id: 'confirmacion',
      label: 'Confirmación y purga',
      nodes: ['API', 'AGENT', 'SQLITE'],
      edges: ['api-ack', 'agent-sqlite'],
      detail: {
        title: 'Solo tras el 200 OK el borde suelta el dato',
        metric: { value: 0, from: 43015, label: 'lecturas pendientes en el búfer', tone: 'green' },
        bullets: [
          'El agente solo borra de cache las filas del lote que el backend ha confirmado; si la respuesta no llega, se reintentan.',
          'Al restablecerse el enlace se sincronizaron los 86.030 puntos: 0 % de pérdida y 0 % de duplicados.',
          'Con un PLC físico sobre Modbus RS-485 el resultado se repitió: 41.580 de 41.580 lecturas.'
        ]
      }
    }
  ]
};

export default storeForwardSpec;
