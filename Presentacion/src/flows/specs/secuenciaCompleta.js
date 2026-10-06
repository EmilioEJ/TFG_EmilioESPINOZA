export const secuenciaCompletaSpec = {
  id: 'sec-completa',
  viewBox: { w: 1200, h: 800 },
  interval: 2200,

  actors: [
    { id: 'est', label: 'Estudiante', icon: 'User', x: 8 },
    { id: 'frt', label: 'Frontend', icon: 'LayoutDashboard', x: 22 },
    { id: 'bck', label: 'Backend', icon: 'Server', x: 38 },
    { id: 'grq', label: 'Groq API', icon: 'Activity', x: 52 },
    { id: 'db',  label: 'ChromaDB', icon: 'Database', x: 66 },
    { id: 'llm', label: 'LLM Local', icon: 'Brain', x: 80 },
    { id: 'elv', label: 'ElevenLabs', icon: 'Volume2', x: 94 }
  ],

  messages: [
    { id: 'm1', from: 'est', to: 'frt', y: 15, label: '1. Se acerca a la cámara' },
    { id: 'm2', from: 'frt', to: 'bck', y: 22, label: '2. Envía frame (WebSockets)' },
    { id: 'm3', from: 'bck', to: 'frt', y: 29, label: '3. PRESENCIA_DETECTADA', isReturn: true },
    
    { id: 'm4', from: 'est', to: 'frt', y: 40, label: 'Habla (pregunta)' },
    { id: 'm5', from: 'frt', to: 'bck', y: 47, label: '5. Envía Blob de audio' },
    
    { id: 'm6', from: 'bck', to: 'grq', y: 55, label: '6. Envía audio para STT' },
    { id: 'm7', from: 'grq', to: 'bck', y: 62, label: '7. Retorna texto (query)', isReturn: true },
    
    { id: 'm8', from: 'bck', to: 'db',  y: 70, label: '8. Busca contexto semántico' },
    { id: 'm9', from: 'db', to: 'bck', y: 77, label: '9. Retorna chunks relevantes', isReturn: true },
    
    { id: 'm10', from: 'bck', to: 'llm', y: 85, label: '10. Prompt + Contexto + Query' },
    { id: 'm11', from: 'llm', to: 'bck', y: 92, label: '11. Genera respuesta textual', isReturn: true },
    
    { id: 'm12', from: 'bck', to: 'elv', y: 100, label: '12. Envía texto para TTS' },
    { id: 'm13', from: 'elv', to: 'bck', y: 107, label: '13. Retorna chunk de audio', isReturn: true },
    
    { id: 'm14', from: 'bck', to: 'frt', y: 115, label: '14. Envía audio en Base64' },
    { id: 'm15', from: 'frt', to: 'est', y: 122, label: '15. Reproduce audio y lip-sync' }
  ],

  steps: [
    {
      id: 'sq-0',
      label: 'Detección',
      activeMessages: ['m1', 'm2', 'm3'],
      detail: {
        title: 'Presencia (WebSockets)',
        bullets: ['El estudiante se acerca a la cámara.', 'Frontend envía frames y Backend dispara PRESENCIA_DETECTADA.']
      }
    },
    {
      id: 'sq-1',
      label: 'Captura y STT',
      activeMessages: ['m4', 'm5', 'm6', 'm7'],
      detail: {
        title: 'Voz a Texto',
        bullets: ['Frontend activa micrófono y envía el Blob de audio.', 'Backend usa la API de Groq para obtener el texto (query).']
      }
    },
    {
      id: 'sq-2',
      label: 'RAG y LLM',
      activeMessages: ['m8', 'm9', 'm10', 'm11'],
      detail: {
        title: 'Generación Aumentada',
        bullets: ['Backend busca contexto semántico en ChromaDB.', 'ChromaDB retorna chunks (Hit Rate).', 'LLM genera respuesta textual basada en el contexto.']
      }
    },
    {
      id: 'sq-3',
      label: 'TTS y Salida',
      activeMessages: ['m12', 'm13', 'm14', 'm15'],
      detail: {
        title: 'Texto a Voz',
        bullets: ['Backend delega generación de voz a ElevenLabs.', 'Frontend recibe Base64 y reproduce audio animando los labios (lip-sync).']
      }
    }
  ]
};
