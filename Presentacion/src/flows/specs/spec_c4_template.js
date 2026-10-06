/**
 * Plantilla base para Diagramas de Contenedores C4 y Grafos de Flujo (FlowGraph).
 *
 * Instrucciones:
 * 1. Ajusta los IDs de zonas y nodos según tu subsistema.
 * 2. Mantén viewBox en { w: 1000, h: 600 } para encajar en el layout 16:9 de la presentación.
 * 3. En los nodos, (x, y) son los CENTROS de cada caja (% del viewBox).
 * 4. En las zonas, (x, y) son la ESQUINA SUPERIOR IZQUIERDA.
 * 5. Deja al menos un 10% de separación libre entre cajas adyacentes para las etiquetas.
 */

export const miArquitecturaSpec = {
  id: 'ejemplo_c4',
  viewBox: { w: 1000, h: 600 },
  interval: 2600, // milisegundos por etapa en autoplay

  // Zonas de fondo (redes, perímetros o capas de seguridad)
  zones: [
    { id: 'borde', label: 'Capa Edge / Borde', x: 2, y: 10, w: 28, h: 80, tone: 'blue' },
    { id: 'vps', label: 'Servidor VPS / Docker', x: 33, y: 10, w: 38, h: 80, tone: 'slate' },
    { id: 'salida', label: 'Monitoreo y Clientes', x: 74, y: 10, w: 24, h: 80, tone: 'green' }
  ],

  // Cajas de servicios, contenedores o hardware
  nodes: [
    {
      id: 'SENSOR',
      x: 15,
      y: 32,
      w: 18,
      h: 18,
      icon: 'Cpu',
      title: 'Dispositivo IoT',
      tech: 'ESP32 · FreeRTOS',
      detail: 'MQTTS :8883'
    },
    {
      id: 'GATEWAY',
      x: 15,
      y: 68,
      w: 18,
      h: 18,
      icon: 'HardDrive',
      title: 'Edge Gateway',
      tech: 'Raspberry Pi',
      detail: 'Store & Forward'
    },
    {
      id: 'BROKER',
      x: 52,
      y: 32,
      w: 20,
      h: 18,
      icon: 'Radio',
      title: 'Eclipse Mosquitto',
      tech: 'MQTT Broker :1883',
      detail: 'Plugin go-auth'
    },
    {
      id: 'BACKEND',
      x: 52,
      y: 68,
      w: 20,
      h: 18,
      icon: 'Server',
      title: 'API FastAPI',
      tech: 'Python 3.11 · :8000',
      detail: 'REST + WebSockets'
    },
    {
      id: 'DASHBOARD',
      x: 86,
      y: 50,
      w: 18,
      h: 22,
      icon: 'LayoutDashboard',
      title: 'SPA React 18',
      tech: 'Vite · Chart.js',
      detail: 'Actualización en vivo'
    }
  ],

  // Aristas y protocolos
  edges: [
    { id: 'sensor-broker', from: 'SENSOR', to: 'BROKER', label: 'MQTTS :8883' },
    { id: 'gateway-backend', from: 'GATEWAY', to: 'BACKEND', label: 'HTTPS :443' },
    { id: 'broker-backend', from: 'BROKER', to: 'BACKEND', label: 'auth/ACL' },
    { id: 'backend-dash', from: 'BACKEND', to: 'DASHBOARD', label: 'WSS :8000' }
  ],

  // Secuencia de etapas narrativas para la exposición oral
  steps: [
    {
      id: 'ingesta',
      label: 'Ingesta directa',
      nodes: ['SENSOR', 'BROKER'],
      edges: ['sensor-broker'],
      detail: {
        title: 'Publicación de telemetría de campo',
        bullets: [
          'El microcontrolador muestrea variables y publica cada 5 segundos mediante MQTTS con TLS 1.3.',
          'El broker canaliza el flujo cifrado hacia el puerto 8883 terminado por el proxy inverso.',
          'Si la red WAN está activa, no existe latencia apreciable de retención.'
        ],
        code: 'v1/devices/{id}/telemetry'
      }
    },
    {
      id: 'seguridad',
      label: 'Validación y ACL',
      nodes: ['BROKER', 'BACKEND'],
      edges: ['broker-backend'],
      detail: {
        title: 'Autenticación delegada en el backend',
        bullets: [
          'Mosquitto no almacena contraseñas; delega cada conexión HTTP al endpoint /api/v1/mqtt/auth.',
          'Se comprueban credenciales individuales por dispositivo (device_token).',
          'La consulta ACL restringe estrictamente la publicación a su propio tópico.'
        ],
        code: 'POST /api/v1/mqtt/auth'
      }
    },
    {
      id: 'despacho',
      label: 'Entrega al usuario',
      nodes: ['BACKEND', 'DASHBOARD'],
      edges: ['backend-dash'],
      detail: {
        title: 'Transmisión reactiva sin sobrecarga',
        metric: { value: 15, suffix: ' ms', label: 'latencia mediana hacia el navegador', tone: 'green' },
        bullets: [
          'El WebSocketManager despacha la lectura en vivo hacia el cliente React conectado.',
          'No se realiza sondeo continuo (polling), reduciendo el consumo de CPU y ancho de banda.',
          'La interfaz visualiza los gráficos reactivos de inmediato.'
        ],
        code: 'WSS /api/v1/ws/devices/{id}/telemetry'
      }
    }
  ]
};

export default miArquitecturaSpec;
