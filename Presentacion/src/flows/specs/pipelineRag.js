export const pipelineRagSpec = {
  id: 'rag-pipeline',
  viewBox: { w: 1200, h: 600 },
  interval: 2500,

  zones: [
    { id: 'z-etl', label: 'Pipeline de Ingesta (ETL)', x: 2, y: 5, w: 45, h: 90, class: 'tone-slate' },
    { id: 'z-db', label: 'Almacenamiento NoSQL', x: 50, y: 5, w: 15, h: 90, class: 'tone-orange' },
    { id: 'z-query', label: 'Proceso de Recuperación (Consulta)', x: 68, y: 5, w: 30, h: 90, class: 'tone-blue' }
  ],

  nodes: [
    // ETL Ingestion
    { id: 'n-pdf', label: 'Documentos\nPDF', icon: 'FileText', x: 10, y: 20, w: 14, h: 18 },
    { id: 'n-md', label: 'Extracción a MD\n(pymupdf4llm)', icon: 'FileCode2', x: 10, y: 50, w: 16, h: 18 },
    { id: 'n-chunk', label: 'División Chunks\n(MarkdownTextSplitter)', icon: 'Scissors', x: 35, y: 50, w: 18, h: 18 },
    { id: 'n-vec', label: 'Vectorización\n(SentenceTransformer)', icon: 'Braces', x: 35, y: 80, w: 18, h: 18 },

    // Database
    { id: 'n-chroma', label: 'ChromaDB\n(Collection)', icon: 'Database', x: 57, y: 50, w: 12, h: 18 },

    // Query Retrieval
    { id: 'n-q', label: 'Pregunta del\nUsuario', icon: 'HelpCircle', x: 83, y: 20, w: 16, h: 18 },
    { id: 'n-qvec', label: 'Vectorización\nConsulta', icon: 'Braces', x: 83, y: 50, w: 16, h: 18 },
    { id: 'n-cos', label: 'Similitud del\nCoseno', icon: 'Calculator', x: 83, y: 75, w: 16, h: 18 },
    { id: 'n-ctx', label: 'Contexto Relevante\n(Para LLM)', icon: 'TextSelect', x: 83, y: 95, w: 18, h: 14 }
  ],

  edges: [
    { id: 'e1', from: 'n-pdf', to: 'n-md', label: 'Parseo' },
    { id: 'e2', from: 'n-md', to: 'n-chunk', label: 'Seccionado' },
    { id: 'e3', from: 'n-chunk', to: 'n-vec', label: 'Embeddings' },
    { id: 'e4', from: 'n-vec', to: 'n-chroma', label: 'Inserta JSON' },
    
    { id: 'e5', from: 'n-q', to: 'n-qvec', label: 'Embedding' },
    { id: 'e6', from: 'n-qvec', to: 'n-cos', label: 'Vector Query' },
    { id: 'e7', from: 'n-chroma', to: 'n-cos', label: 'Retorna k-Chunks', class: 'is-dashed' },
    { id: 'e8', from: 'n-cos', to: 'n-ctx', label: 'Top-k Results' }
  ],

  particles: [
    { edgeId: 'e1', count: 1, color: 'var(--text-main)' },
    { edgeId: 'e2', count: 3, color: 'var(--uti-cyan)' },
    { edgeId: 'e3', count: 5, color: 'var(--uti-purple)' },
    { edgeId: 'e4', count: 1, color: 'var(--uti-orange)' },
    { edgeId: 'e5', count: 1, color: 'var(--uti-purple)' },
    { edgeId: 'e6', count: 1, color: 'var(--uti-purple)' },
    { edgeId: 'e7', count: 3, color: 'var(--uti-green)' },
    { edgeId: 'e8', count: 1, color: 'var(--text-main)' }
  ],

  steps: [
    {
      id: 'rg-0',
      label: 'ETL - Extracción',
      highlightNodes: ['n-pdf', 'n-md'],
      highlightEdges: ['e1'],
      activeParticles: ['e1'],
      detail: { title: 'Librería: pymupdf4llm', bullets: ['Convierte el PDF académico en formato Markdown, preservando tablas y jerarquía.'] }
    },
    {
      id: 'rg-1',
      label: 'ETL - Chunking',
      highlightNodes: ['n-md', 'n-chunk'],
      highlightEdges: ['e2'],
      activeParticles: ['e2'],
      detail: { title: 'MarkdownTextSplitter', bullets: ['Divide el documento respetando los encabezados H1/H2, para no cortar la semántica a la mitad.'] }
    },
    {
      id: 'rg-2',
      label: 'ETL - Vectorización',
      highlightNodes: ['n-chunk', 'n-vec', 'n-chroma'],
      highlightEdges: ['e3', 'e4'],
      activeParticles: ['e3', 'e4'],
      detail: { title: 'SentenceTransformer', bullets: ['Transforma el texto en una matriz de números y lo inserta en ChromaDB junto con sus metadatos.'] }
    },
    {
      id: 'rg-3',
      label: 'Consulta (Query)',
      highlightNodes: ['n-q', 'n-qvec', 'n-cos'],
      highlightEdges: ['e5', 'e6'],
      activeParticles: ['e5', 'e6'],
      detail: { title: 'Vectorización de la Pregunta', bullets: ['La pregunta hablada se transforma al mismo espacio vectorial matemático.'] }
    },
    {
      id: 'rg-4',
      label: 'Recuperación',
      highlightNodes: ['n-chroma', 'n-cos', 'n-ctx'],
      highlightEdges: ['e7', 'e8'],
      activeParticles: ['e7', 'e8'],
      detail: { title: 'Cálculo del Coseno', bullets: ['ChromaDB retorna los k-chunks más similares matemáticamente, listos para inyectarse al LLM.'] }
    }
  ]
};
