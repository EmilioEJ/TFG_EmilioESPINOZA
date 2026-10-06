export const clasesBackendSpec = {
  id: 'clases-backend',
  viewBox: { w: 1200, h: 800 },
  interval: 2200,

  zones: [
    { id: 'z-circ', label: 'Bucle Cerrado: Interconexión de Clases', x: 2, y: 5, w: 96, h: 90, class: 'tone-slate' }
  ],

  nodes: [
    // Izquierda (Interfaces)
    { id: 'n-ui', label: 'UserInterface', icon: 'LayoutDashboard', x: 20, y: 25, w: 18, h: 18 },
    { id: 'n-vis', label: 'VisionHandler', icon: 'Camera', x: 20, y: 75, w: 18, h: 18 },
    { id: 'n-ava', label: 'AvatarController', icon: 'User', x: 50, y: 15, w: 18, h: 18 },

    // Centro (Procesadores)
    { id: 'n-aud', label: 'AudioProcessor', icon: 'Volume2', x: 50, y: 45, w: 18, h: 18 },
    { id: 'n-inp', label: 'InputRouter', icon: 'ArrowLeftRight', x: 50, y: 75, w: 18, h: 18 },

    // Derecha (Cognitivo y BD)
    { id: 'n-llm', label: 'LLMController', icon: 'Brain', x: 80, y: 25, w: 18, h: 18 },
    { id: 'n-rag', label: 'RAGManager', icon: 'BrainCircuit', x: 80, y: 55, w: 18, h: 18 },
    { id: 'n-db', label: 'VectorDatabase', icon: 'Database', x: 80, y: 85, w: 18, h: 18 }
  ],

  edges: [
    { id: 'e1', from: 'n-vis', to: 'n-ui', label: '1. Detecta rostro' },
    { id: 'e2', from: 'n-ui', to: 'n-aud', label: '2. Saludo a TTS' },
    { id: 'e2b', from: 'n-ui', to: 'n-ava', label: '2b. Subtítulos' },
    
    { id: 'e3', from: 'n-vis', to: 'n-aud', label: '3. Activa Mic' },
    { id: 'e4', from: 'n-aud', to: 'n-inp', label: '4. STT Texto' },
    { id: 'e4b', from: 'n-ui', to: 'n-inp', label: '4b. Texto Teclado' },
    
    { id: 'e5', from: 'n-inp', to: 'n-llm', label: '5. Inyecta Query' },
    { id: 'e6', from: 'n-llm', to: 'n-rag', label: '6. Pide Contexto' },
    { id: 'e7', from: 'n-rag', to: 'n-db', label: '7. Busca Datos' },
    
    { id: 'e8', from: 'n-db', to: 'n-rag', label: '8. Retorna Markdown', isReturn: true },
    { id: 'e9', from: 'n-rag', to: 'n-llm', label: '9. Inyecta Contexto', isReturn: true },
    
    { id: 'e10', from: 'n-llm', to: 'n-aud', label: '10. Texto a TTS' },
    { id: 'e10b', from: 'n-llm', to: 'n-ui', label: '10b. Texto al Chat' },
    { id: 'e11', from: 'n-aud', to: 'n-ava', label: '11. Anima Lip-Sync' },
    
    { id: 'e12', from: 'n-ava', to: 'n-ui', label: '12. Termina y Libera' },
    { id: 'e13', from: 'n-ui', to: 'n-vis', label: '13. Espera en loop' }
  ],

  particles: [
    { edgeId: 'e1', count: 1, color: 'var(--uti-cyan)' },
    { edgeId: 'e2', count: 1, color: 'var(--uti-orange)' },
    { edgeId: 'e3', count: 1, color: 'var(--uti-cyan)' },
    { edgeId: 'e4', count: 1, color: 'var(--uti-purple)' },
    { edgeId: 'e5', count: 1, color: 'var(--uti-purple)' },
    { edgeId: 'e6', count: 1, color: 'var(--uti-orange)' },
    { edgeId: 'e7', count: 1, color: 'var(--uti-cyan)' },
    { edgeId: 'e8', count: 2, color: 'var(--uti-green)' },
    { edgeId: 'e9', count: 2, color: 'var(--uti-green)' },
    { edgeId: 'e10', count: 1, color: 'var(--uti-orange)' },
    { edgeId: 'e11', count: 1, color: 'var(--uti-cyan)' },
    { edgeId: 'e12', count: 1, color: 'var(--text-dim)' },
    { edgeId: 'e13', count: 1, color: 'var(--text-dim)' }
  ],

  steps: [
    {
      id: 'cls-0',
      label: '1. Inicio (Saludo)',
      highlightNodes: ['n-vis', 'n-ui', 'n-aud', 'n-ava'],
      highlightEdges: ['e1', 'e2', 'e2b'],
      activeParticles: ['e1', 'e2'],
      detail: {
        title: 'Primera Interacción',
        bullets: ['VisionHandler detecta rostro y avisa a UI.', 'UI dispara saludo hardcodeado (ej. "¡Hola! ¿En qué te ayudo?") hacia AudioProcessor.']
      }
    },
    {
      id: 'cls-1',
      label: '2. Captura Pregunta',
      highlightNodes: ['n-vis', 'n-aud', 'n-ui', 'n-inp'],
      highlightEdges: ['e3', 'e4', 'e4b'],
      activeParticles: ['e3', 'e4', 'e4b'],
      detail: {
        title: 'Entrada del Usuario',
        bullets: ['Micrófono se activa para escuchar.', 'STT genera texto y lo envía a InputRouter (junto con entrada opcional de teclado).']
      }
    },
    {
      id: 'cls-2',
      label: '3. Flujo RAG',
      highlightNodes: ['n-inp', 'n-llm', 'n-rag', 'n-db'],
      highlightEdges: ['e5', 'e6', 'e7'],
      activeParticles: ['e5', 'e6', 'e7'],
      detail: {
        title: 'Inyección de Contexto',
        bullets: ['InputRouter envía la query al LLMController.', 'El LLM no responde aún; primero pide información al RAGManager.', 'RAGManager busca vectores en VectorDatabase.']
      }
    },
    {
      id: 'cls-3',
      label: '4. Retorno RAG',
      highlightNodes: ['n-db', 'n-rag', 'n-llm'],
      highlightEdges: ['e8', 'e9'],
      activeParticles: ['e8', 'e9'],
      detail: {
        title: 'Recuperación de Documentos',
        bullets: ['Base de datos devuelve Markdown crudo.', 'RAGManager inyecta los fragmentos oficiales en el prompt del LLM.']
      }
    },
    {
      id: 'cls-4',
      label: '5. Generación y Voz',
      highlightNodes: ['n-llm', 'n-aud', 'n-ui', 'n-ava'],
      highlightEdges: ['e10', 'e10b', 'e11'],
      activeParticles: ['e10', 'e10b', 'e11'],
      detail: {
        title: 'Respuesta Natural',
        bullets: ['LLM genera respuesta y la envía al chat y a TTS.', 'AudioProcessor recibe el audio TTS y anima a AvatarController (Lip-Sync).']
      }
    },
    {
      id: 'cls-5',
      label: '6. Bucle Cerrado',
      highlightNodes: ['n-ava', 'n-ui', 'n-vis'],
      highlightEdges: ['e12', 'e13'],
      activeParticles: ['e12', 'e13'],
      detail: {
        title: 'Ciclo de Vida Continuo',
        bullets: ['AvatarController termina de hablar y libera a UI.', 'UI vuelve a modo escucha (loop) esperando nueva interacción.', 'Ningún nodo queda suelto en el sistema.']
      }
    }
  ]
};
