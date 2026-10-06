import React from 'react';
import { SlideEngine } from './SlideEngine';
import { FlowGraph, SequenceDiagram } from './flows';
import { 
  arquitecturaAsistenteSpec,
  contextoAsistenteSpec,
  estadosAvatarSpec,
  pipelineRagSpec,
  bdSchemaSpec,
  clasesBackendSpec,
  secuenciaCompletaSpec
} from './flows';

import { 
  CosineAnimation, 
  SprintTimeline, 
  WebSocketAnimation, 
  LatencyGauge 
} from './animations';

function App() {
  // Aquí podemos mapear los índices de las diapositivas con sus diagramas custom.
  const customDiagrams = {
    13: <CosineAnimation />,
    15: <SprintTimeline />,
    18: <FlowGraph spec={arquitecturaAsistenteSpec} isActive={true} />,
    19: <FlowGraph spec={contextoAsistenteSpec} isActive={true} />,
    20: <FlowGraph spec={estadosAvatarSpec} isActive={true} />,
    21: <WebSocketAnimation />,
    22: <FlowGraph spec={pipelineRagSpec} isActive={true} />,
    23: <FlowGraph spec={bdSchemaSpec} isActive={true} />,
    24: <FlowGraph spec={clasesBackendSpec} isActive={true} />,
    26: <SequenceDiagram spec={secuenciaCompletaSpec} isActive={true} />,
    28: <LatencyGauge />
  };

  return (
    <SlideEngine customDiagrams={customDiagrams} />
  );
}

export default App;
