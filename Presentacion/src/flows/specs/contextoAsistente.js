export const contextoAsistenteSpec = {
  id: 'ctx-asistente',
  viewBox: { w: 1000, h: 500 },
  interval: 2500,

  zones: [
    { id: 'z-ext', label: 'Entorno Físico', x: 2, y: 5, w: 22, h: 80, class: 'tone-slate' },
    { id: 'z-sys', label: 'El Sistema', x: 28, y: 5, w: 44, h: 80, class: 'tone-blue' },
    { id: 'z-api', label: 'Proveedores Cloud', x: 76, y: 5, w: 22, h: 80, class: 'tone-orange' }
  ],

  nodes: [
    { id: 'n-est', label: 'Estudiante', icon: 'User', x: 13, y: 45, w: 18, h: 22 },
    
    { id: 'n-asis', label: 'Asistente Virtual\n(Núcleo Central)', icon: 'Bot', x: 50, y: 45, w: 30, h: 26 },
    { id: 'n-sga', label: 'SGA\n(Pasivo)', icon: 'Database', x: 50, y: 85, w: 30, h: 18, class: 'is-dim' },
    
    { id: 'n-groq', label: 'Groq API\n(STT Whisper)', icon: 'Activity', x: 87, y: 30, w: 18, h: 18 },
    { id: 'n-tts', label: 'ElevenLabs\n(TTS)', icon: 'Volume2', x: 87, y: 65, w: 18, h: 18 }
  ],

  edges: [
    { id: 'e1', from: 'n-est', to: 'n-asis', label: 'Voz / Video' },
    { id: 'e2', from: 'n-asis', to: 'n-groq', label: 'Audio In' },
    { id: 'e3', from: 'n-groq', to: 'n-asis', label: 'Texto', isReturn: true },
    { id: 'e4', from: 'n-asis', to: 'n-tts', label: 'Texto Generado' },
    { id: 'e5', from: 'n-tts', to: 'n-asis', label: 'Audio Segmentado', isReturn: true },
    { id: 'e6', from: 'n-asis', to: 'n-est', label: 'Audio / Avatar 3D', isReturn: true },
    { id: 'e7', from: 'n-asis', to: 'n-sga', label: 'Desconectado', class: 'is-blocked' }
  ],

  particles: [
    { edgeId: 'e1', count: 3, color: 'var(--uti-cyan)' },
    { edgeId: 'e2', count: 2, color: 'var(--uti-orange)' },
    { edgeId: 'e3', count: 1, color: 'var(--text-main)' },
    { edgeId: 'e4', count: 1, color: 'var(--text-main)' },
    { edgeId: 'e5', count: 3, color: 'var(--uti-orange)' },
    { edgeId: 'e6', count: 3, color: 'var(--uti-purple)' }
  ],

  steps: [
    {
      id: 'ctx-0',
      label: 'Entrada Estudiante',
      highlightNodes: ['n-est', 'n-asis'],
      highlightEdges: ['e1'],
      activeParticles: ['e1'],
      detail: {
        title: 'Captura Sensorial',
        bullets: ['El estudiante envía audio (pregunta) y video (presencia) al Asistente.']
      }
    },
    {
      id: 'ctx-1',
      label: 'Delegación STT',
      highlightNodes: ['n-asis', 'n-groq'],
      highlightEdges: ['e2', 'e3'],
      activeParticles: ['e2', 'e3'],
      detail: {
        title: 'Transcripción (Whisper)',
        bullets: ['El Asistente envía el audio a Groq (STT).', 'Recibe el texto transcrito a alta velocidad.']
      }
    },
    {
      id: 'ctx-2',
      label: 'Procesamiento Interno',
      highlightNodes: ['n-asis'],
      highlightEdges: [],
      activeParticles: [],
      detail: {
        title: 'Caja Negra del Sistema',
        bullets: ['El Asistente procesa internamente la consulta usando su RAG local y LLM.']
      }
    },
    {
      id: 'ctx-3',
      label: 'Delegación TTS',
      highlightNodes: ['n-asis', 'n-tts'],
      highlightEdges: ['e4', 'e5'],
      activeParticles: ['e4', 'e5'],
      detail: {
        title: 'Síntesis de Voz',
        bullets: ['El Asistente envía el texto generado a ElevenLabs.', 'Recibe audio segmentado y fonemas.']
      }
    },
    {
      id: 'ctx-4',
      label: 'Salida Multimodal',
      highlightNodes: ['n-asis', 'n-est'],
      highlightEdges: ['e6'],
      activeParticles: ['e6'],
      detail: {
        title: 'Respuesta al Estudiante',
        bullets: ['El Asistente reproduce el audio y muestra la animación 3D al Estudiante simultáneamente.']
      }
    }
  ]
};
