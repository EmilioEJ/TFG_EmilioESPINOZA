export const arquitecturaAsistenteSpec = {
  id: 'arq-asistente',
  viewBox: { w: 1200, h: 700 },
  interval: 2200,

  zones: [
    { id: 'z-cli', label: '1. Cliente (Frontend - Kiosco)', x: 2, y: 5, w: 25, h: 90, class: 'tone-slate' },
    { id: 'z-net', label: '2. Capa de Comunicación', x: 28, y: 5, w: 16, h: 90, class: 'tone-blue' },
    { id: 'z-bck', label: '3. Servidor Backend (FastAPI)', x: 45, y: 5, w: 25, h: 90, class: 'tone-purple' },
    { id: 'z-cog', label: '4. Capa Cognitiva (IA)', x: 72, y: 5, w: 26, h: 90, class: 'tone-orange' }
  ],

  nodes: [
    // Cliente
    { id: 'n-ui', label: 'Avatar 3D\n(Ready Player Me)', icon: 'User', x: 14, y: 25, w: 20, h: 18 },
    { id: 'n-cam', label: 'Webcam\n(Visión)', icon: 'Camera', x: 14, y: 55, w: 18, h: 14 },
    { id: 'n-mic', label: 'Micrófono\n(Captura)', icon: 'Mic', x: 14, y: 75, w: 18, h: 14 },

    // Red
    { id: 'n-ws', label: 'WebSocket\n(Bidireccional)', icon: 'ArrowLeftRight', x: 36, y: 50, w: 14, h: 20 },

    // Backend
    { id: 'n-vis', label: 'Módulo Visión\n(Presencia)', icon: 'Eye', x: 57, y: 30, w: 20, h: 18 },
    { id: 'n-rag', label: 'Gestor RAG\n(Orquestador)', icon: 'BrainCircuit', x: 57, y: 65, w: 20, h: 18 },

    // Capa Cognitiva
    { id: 'n-stt', label: 'Motor STT\n(Whisper v3)', icon: 'Activity', x: 85, y: 20, w: 20, h: 14 },
    { id: 'n-db', label: 'ChromaDB\n(Base Vectorial)', icon: 'Database', x: 85, y: 45, w: 20, h: 14 },
    { id: 'n-llm', label: 'Motor LLM\n(Llama 3)', icon: 'Brain', x: 85, y: 65, w: 20, h: 14 },
    { id: 'n-tts', label: 'Motor TTS\n(ElevenLabs)', icon: 'Volume2', x: 85, y: 85, w: 20, h: 14 }
  ],

  edges: [
    { id: 'e1', from: 'n-cam', to: 'n-vis', label: '1. Detecta rostro' },
    { id: 'e2', from: 'n-mic', to: 'n-ws', label: '2. Audio al Server' },
    { id: 'e3', from: 'n-ws', to: 'n-rag', label: 'Audio In' },
    
    { id: 'e4', from: 'n-rag', to: 'n-stt', label: '3. Audio a STT' },
    { id: 'e5', from: 'n-stt', to: 'n-rag', label: 'Retorna Texto', isReturn: true },
    
    { id: 'e6', from: 'n-rag', to: 'n-db', label: '4. Consulta Vectorial' },
    { id: 'e7', from: 'n-db', to: 'n-rag', label: '5. Retorna Fragmentos', isReturn: true },
    
    { id: 'e8', from: 'n-rag', to: 'n-llm', label: '6. Texto + Contexto' },
    { id: 'e9', from: 'n-llm', to: 'n-rag', label: '7. Genera Respuesta', isReturn: true },
    
    { id: 'e10', from: 'n-rag', to: 'n-tts', label: '8. Envia Texto a TTS' },
    { id: 'e11', from: 'n-tts', to: 'n-rag', label: '9. Flujo Audio+Visemas', isReturn: true },
    
    { id: 'e12', from: 'n-rag', to: 'n-ws', label: 'Audio Out' },
    { id: 'e13', from: 'n-ws', to: 'n-ui', label: '10. Reproduce y Anima' }
  ],

  particles: [
    { edgeId: 'e1', count: 1, color: 'var(--uti-cyan)' },
    { edgeId: 'e2', count: 2, color: 'var(--uti-orange)' },
    { edgeId: 'e3', count: 2, color: 'var(--uti-orange)' },
    { edgeId: 'e4', count: 1, color: 'var(--uti-purple)' },
    { edgeId: 'e5', count: 1, color: 'var(--text-main)' },
    { edgeId: 'e6', count: 1, color: 'var(--uti-cyan)' },
    { edgeId: 'e7', count: 2, color: 'var(--uti-green)' },
    { edgeId: 'e8', count: 2, color: 'var(--uti-purple)' },
    { edgeId: 'e9', count: 1, color: 'var(--text-main)' },
    { edgeId: 'e10', count: 1, color: 'var(--text-main)' },
    { edgeId: 'e11', count: 3, color: 'var(--uti-orange)' },
    { edgeId: 'e12', count: 3, color: 'var(--uti-orange)' },
    { edgeId: 'e13', count: 3, color: 'var(--uti-orange)' }
  ],

  steps: [
    {
      id: 'step-det',
      label: 'Detección',
      highlightNodes: ['n-cam', 'n-vis', 'n-mic'],
      highlightEdges: ['e1'],
      activeParticles: ['e1'],
      detail: { title: 'Paso 1: Detección', bullets: ['Usuario se acerca (Webcam detecta rostro).', 'Se activa el micrófono para captura.'] }
    },
    {
      id: 'step-in',
      label: 'Ingreso',
      highlightNodes: ['n-mic', 'n-ws', 'n-rag'],
      highlightEdges: ['e2', 'e3'],
      activeParticles: ['e2', 'e3'],
      detail: { title: 'Paso 2: WebSockets', bullets: ['Usuario habla.', 'Audio se envía por WebSocket al Backend.'] }
    },
    {
      id: 'step-stt',
      label: 'Transcripción',
      highlightNodes: ['n-rag', 'n-stt'],
      highlightEdges: ['e4', 'e5'],
      activeParticles: ['e4', 'e5'],
      detail: { title: 'Paso 3: STT', bullets: ['Backend envía audio a Whisper v3.', 'Retorna Texto de la pregunta.'] }
    },
    {
      id: 'step-rag',
      label: 'RAG',
      highlightNodes: ['n-rag', 'n-db'],
      highlightEdges: ['e6', 'e7'],
      activeParticles: ['e6', 'e7'],
      detail: { title: 'Pasos 4-5: Consulta ChromaDB', bullets: ['Backend envía Texto al Gestor RAG.', 'ChromaDB retorna fragmentos relevantes de PDF.'] }
    },
    {
      id: 'step-llm',
      label: 'Inferencia',
      highlightNodes: ['n-rag', 'n-llm'],
      highlightEdges: ['e8', 'e9'],
      activeParticles: ['e8', 'e9'],
      detail: { title: 'Pasos 6-7: Llama 3', bullets: ['Backend envía Texto + Fragmentos PDF al LLM.', 'LLM genera respuesta estructurada.'] }
    },
    {
      id: 'step-tts',
      label: 'Síntesis',
      highlightNodes: ['n-rag', 'n-tts'],
      highlightEdges: ['e10', 'e11'],
      activeParticles: ['e10', 'e11'],
      detail: { title: 'Pasos 8-9: ElevenLabs', bullets: ['Backend envía respuesta a TTS.', 'TTS devuelve flujo de audio + fonemas.'] }
    },
    {
      id: 'step-out',
      label: 'Renderizado',
      highlightNodes: ['n-rag', 'n-ws', 'n-ui'],
      highlightEdges: ['e12', 'e13'],
      activeParticles: ['e12', 'e13'],
      detail: { title: 'Paso 10: Salida Multimodal', bullets: ['Cliente reproduce audio.', 'Anima la boca del Avatar 3D simultáneamente.'] }
    }
  ]
};
