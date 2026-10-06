/* Conexión, autenticación y autorización en el broker MQTT (Figura 6 de la tesis).
   Transcrito de TESIS/Capítulos/fig/fig_secuencia_autenticacion.mmd.

   Corrección respecto al .mmd original: quien consume el mensaje MQTT, consulta el dispositivo,
   inserta la lectura y dispara las alertas NO es el backend REST, sino el contenedor
   iiot_mqtt_worker (docker-compose.yml:80, backend/start.sh:8-11). Por eso aquí son dos actores
   distintos: el backend solo atiende las llamadas de auth/ACL que le delega go-auth.

   Orden de los actores elegido para minimizar cruces: solo m8 (Mosquitto → Worker) cruza una
   línea de vida. */

export const authMqttSpec = {
  id: 'auth',
  interval: 2600,

  actors: [
    { id: 'D', label: 'Dispositivo', sub: 'ESP32 / Gateway', icon: 'Cpu' },
    { id: 'M', label: 'Mosquitto', sub: 'plugin go-auth', icon: 'Radio' },
    { id: 'B', label: 'Backend FastAPI', sub: 'auth y ACL', icon: 'Server' },
    { id: 'W', label: 'MQTT Worker', sub: 'iiot_mqtt_worker', icon: 'RefreshCw' },
    { id: 'DB', label: 'TimescaleDB', sub: 'PostgreSQL 15', icon: 'Database' }
  ],

  messages: [
    { id: 'm1', kind: 'call', from: 'D', to: 'M', label: 'CONNECT', sub: 'username y password del dispositivo' },
    { id: 'n1', kind: 'note', over: ['M', 'B'], label: 'go-auth delega la validación al backend' },
    { id: 'm2', kind: 'call', from: 'M', to: 'B', label: 'POST /api/v1/mqtt/auth' },
    { id: 'm3', kind: 'return', from: 'B', to: 'M', label: '200 OK — credenciales válidas' },
    { id: 'm4', kind: 'call', from: 'M', to: 'B', label: 'POST /api/v1/mqtt/acl' },
    { id: 'm5', kind: 'return', from: 'B', to: 'M', label: '200 OK — tópico permitido' },
    { id: 'm6', kind: 'return', from: 'M', to: 'D', label: 'CONNACK (rc = 0)' },
    { id: 'm7', kind: 'call', from: 'D', to: 'M', label: 'PUBLISH telemetry', sub: 'v1/devices/{did}/telemetry · QoS 0' },
    { id: 'n2', kind: 'note', over: ['M', 'W'], label: 'El worker está suscrito con QoS 1 a v1/devices/+/telemetry' },
    { id: 'm8', kind: 'call', from: 'M', to: 'W', label: 'Mensaje MQTT' },
    { id: 'm9', kind: 'call', from: 'W', to: 'DB', label: 'SELECT devices … is_active = TRUE' },
    { id: 'm10', kind: 'return', from: 'DB', to: 'W', label: 'dispositivo encontrado' },
    { id: 'm11', kind: 'call', from: 'W', to: 'DB', label: 'INSERT INTO readings' },
    { id: 'm12', kind: 'self', from: 'W', label: 'Evalúa alert_rules → Telegram' }
  ],

  steps: [
    {
      id: 'connect',
      label: 'Conexión',
      messages: ['m1'],
      actors: ['D', 'M'],
      detail: {
        title: 'El dispositivo se presenta con credenciales propias',
        bullets: [
          'username = device_identifier (formato DEV-XXXXXXXX) y password = device_token, de 48 bytes URL-safe.',
          'Cada dispositivo tiene las suyas: no hay una contraseña compartida en el broker.',
          'El token no se vuelve a exponer después de crear el dispositivo.'
        ]
      }
    },
    {
      id: 'auth',
      label: 'Autenticación',
      messages: ['n1', 'm2', 'm3'],
      actors: ['M', 'B'],
      detail: {
        title: 'Mosquitto no guarda usuarios: pregunta',
        bullets: [
          'El plugin mosquitto-go-auth delega cada conexión al backend, que valida contra la base de datos.',
          'Dar de baja un dispositivo en la aplicación lo desconecta sin editar ficheros ni reiniciar el broker.',
          'La caché de credenciales del broker (TTL 300 s) evita consultar la base en cada reconexión; a cambio, una baja tarda hasta 5 minutos en propagarse.'
        ],
        code: 'POST /api/v1/mqtt/auth'
      }
    },
    {
      id: 'acl',
      label: 'Autorización ACL',
      messages: ['m4', 'm5', 'm6'],
      actors: ['D', 'M', 'B'],
      detail: {
        title: 'Autenticarse no basta: hay que poder publicar ahí',
        bullets: [
          'La segunda llamada comprueba que ese dispositivo tenga permiso sobre ese tópico concreto.',
          'Un dispositivo no puede publicar ni leer el tópico de otro, ni siquiera dentro de la misma empresa.',
          'El broker decide por el código HTTP: 200 concede, 403 deniega. Solo con ambas respuestas afirmativas devuelve CONNACK rc=0.'
        ],
        code: 'POST /api/v1/mqtt/acl'
      }
    },
    {
      id: 'publish',
      label: 'Publicación',
      messages: ['m7', 'n2', 'm8'],
      actors: ['D', 'M', 'W'],
      detail: {
        title: 'La telemetría entra por el tópico del dispositivo',
        bullets: [
          'Publica con QoS 0 cada 5 segundos; el worker, un contenedor aparte del backend REST, consume del comodín con QoS 1.',
          'El ESP32 no lleva reloj: envía su uptime en ts y el backend le asigna la marca UTC al recibirlo.',
          'En redes públicas la conexión va sobre TLS, validando contra la CA raíz ISRG Root X1.'
        ],
        code: 'v1/devices/{device_identifier}/telemetry'
      }
    },
    {
      id: 'persist',
      label: 'Persistencia y alertas',
      messages: ['m9', 'm10', 'm11', 'm12'],
      actors: ['W', 'DB'],
      detail: {
        title: 'Última comprobación antes de escribir',
        bullets: [
          'El worker verifica que el dispositivo siga activo (is_active); si no, descarta el mensaje.',
          'Las variables no vistas antes se auto-registran en device_variables, sin recompilar el firmware.',
          'Tras insertar, se evalúan las reglas de alerta y el envío a Telegram se delega a un pool de hilos para no frenar la ingesta.'
        ]
      }
    }
  ]
};

export default authMqttSpec;
