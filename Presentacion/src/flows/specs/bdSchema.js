export const bdSchemaSpec = {
  id: 'bd-schema',
  viewBox: { w: 1000, h: 600 },
  interval: 2200,

  zones: [
    { id: 'z-db', label: 'Estructura NoSQL (ChromaDB)', x: 10, y: 5, w: 80, h: 90, class: 'tone-orange' }
  ],

  nodes: [
    { id: 'n-coll', label: 'ChromaDB_Collection\n"carrera_ti_indoamerica"', icon: 'Database', x: 50, y: 20, w: 35, h: 18 },
    { id: 'n-doc', label: 'VectorDocument\n- id [PK]\n- document\n- embedding', icon: 'FileText', x: 30, y: 60, w: 25, h: 28 },
    { id: 'n-meta', label: 'MetadataJSON\n- source\n- page\n- tipo_documento', icon: 'Braces', x: 70, y: 60, w: 25, h: 28 }
  ],

  edges: [
    { id: 'e1', from: 'n-coll', to: 'n-doc', label: '1..N (Contiene)' },
    { id: 'e2', from: 'n-doc', to: 'n-meta', label: '1..1 (Anida)' }
  ],

  particles: [
    { edgeId: 'e1', count: 2, color: 'var(--uti-cyan)' },
    { edgeId: 'e2', count: 1, color: 'var(--uti-orange)' }
  ],

  steps: [
    {
      id: 'bd-0',
      label: 'Colección',
      highlightNodes: ['n-coll'],
      highlightEdges: [],
      activeParticles: [],
      detail: {
        title: 'Namespace de Datos',
        bullets: ['Todos los vectores de la carrera se almacenan en una misma Collection de ChromaDB.']
      }
    },
    {
      id: 'bd-1',
      label: 'Documento Vectorial',
      highlightNodes: ['n-coll', 'n-doc'],
      highlightEdges: ['e1'],
      activeParticles: ['e1'],
      detail: {
        title: 'Desnormalización',
        bullets: ['Cada registro contiene el "document" (texto) y su "embedding" (matriz de floats) en el mismo nivel para cálculos rápidos en RAM.']
      }
    },
    {
      id: 'bd-2',
      label: 'Metadatos (JSON)',
      highlightNodes: ['n-doc', 'n-meta'],
      highlightEdges: ['e2'],
      activeParticles: ['e2'],
      detail: {
        title: 'Objeto Anidado',
        bullets: ['Permite pre-filtrar consultas (ej. buscar solo "tipo_documento: Normativa") antes de calcular la distancia matemática.']
      }
    }
  ]
};
