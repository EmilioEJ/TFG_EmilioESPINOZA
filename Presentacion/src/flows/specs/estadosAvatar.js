export const estadosAvatarSpec = {
  id: 'estados-avatar',
  viewBox: { w: 1000, h: 500 },
  interval: 2500,

  zones: [
    { id: 'z-avatar', label: 'Máquina de Estados: Avatar 3D', x: 10, y: 5, w: 80, h: 90 }
  ],

  nodes: [
    { id: 'n-sleep', label: '1. Dormido\n(Idle)', icon: 'WifiOff', x: 30, y: 50, w: 18, h: 22 },
    { id: 'n-listen', label: '2. Escuchando\n(Listening)', icon: 'Camera', x: 50, y: 20, w: 18, h: 22 },
    { id: 'n-think', label: '3. Pensando\n(Processing)', icon: 'RefreshCw', x: 70, y: 50, w: 18, h: 22 },
    { id: 'n-speak', label: '4. Hablando\n(Speaking)', icon: 'Volume2', x: 50, y: 80, w: 18, h: 22 }
  ],

  edges: [
    { id: 'e1', from: 'n-sleep', to: 'n-listen', label: 'Bounding box > threshold' },
    { id: 'e2', from: 'n-listen', to: 'n-think', label: 'Silencio detectado' },
    { id: 'e3', from: 'n-think', to: 'n-speak', label: 'Recibe audio (TTFB)' },
    { id: 'e4', from: 'n-speak', to: 'n-sleep', label: 'Fin audio + Inactividad' },
    { id: 'e5', from: 'n-speak', to: 'n-listen', label: 'Fin audio + Presencia' },
    { id: 'e6', from: 'n-listen', to: 'n-sleep', label: 'Timeout sin voz' }
  ],

  particles: [
    { edgeId: 'e1', count: 2, color: 'var(--uti-cyan)' },
    { edgeId: 'e2', count: 2, color: 'var(--uti-purple)' },
    { edgeId: 'e3', count: 2, color: 'var(--uti-orange)' },
    { edgeId: 'e4', count: 2, color: 'var(--text-dim)' },
    { edgeId: 'e5', count: 2, color: 'var(--uti-cyan)' },
    { edgeId: 'e6', count: 2, color: 'var(--text-dim)' }
  ],

  steps: [
    {
      id: 'st-0',
      label: 'Dormido',
      highlightNodes: ['n-sleep'],
      highlightEdges: [],
      activeParticles: [],
      detail: {
        title: 'Estado Inicial (Idle)',
        bullets: ['Condición: No hay nadie en la cámara.', 'Animación: Ojos cerrados, respiración lenta.']
      }
    },
    {
      id: 'st-1',
      label: 'Despierto',
      highlightNodes: ['n-sleep', 'n-listen'],
      highlightEdges: ['e1'],
      activeParticles: ['e1'],
      detail: {
        title: 'Estado: Escuchando',
        bullets: ['Transición: Bounding box supera el umbral (Presencia detectada).', 'Animación: Ojos abiertos, contacto visual.']
      }
    },
    {
      id: 'st-2',
      label: 'Pensando',
      highlightNodes: ['n-listen', 'n-think'],
      highlightEdges: ['e2'],
      activeParticles: ['e2'],
      detail: {
        title: 'Estado: Procesamiento',
        bullets: ['Transición: Usuario termina de hablar (silencio detectado).', 'Animación: Mirando arriba/lado, postura reflexiva.']
      }
    },
    {
      id: 'st-3',
      label: 'Hablando',
      highlightNodes: ['n-think', 'n-speak'],
      highlightEdges: ['e3'],
      activeParticles: ['e3'],
      detail: {
        title: 'Estado: Respuesta',
        bullets: ['Transición: Recibe audio del servidor (TTFB completado).', 'Animación: Lip-sync activo, gestos de manos.']
      }
    },
    {
      id: 'st-4',
      label: 'Ciclo / Retorno',
      highlightNodes: ['n-speak', 'n-listen', 'n-sleep'],
      highlightEdges: ['e4', 'e5'],
      activeParticles: ['e4', 'e5'],
      detail: {
        title: 'Transición de Salida',
        bullets: ['Fin del audio -> Vuelve a "Despierto" o "Dormido" si hay inactividad (timeout).']
      }
    }
  ]
};
