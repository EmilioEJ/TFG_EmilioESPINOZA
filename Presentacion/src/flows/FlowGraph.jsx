import React, { useMemo } from 'react';
import { buildEdge, layoutLabels } from './geometry';
import { getFlowIcon } from './icons';
import { useFlowPlayer } from './useFlowPlayer';
import FlowStepper from './FlowStepper';
import FlowDetail from './FlowDetail';

/* Dos partículas desfasadas por arista: leen como un caudal de datos y no como una sola bolita. */
const PARTICLE_OFFSETS = ['0s', '0.75s'];

const EdgeParticles = ({ pathId, dur }) =>
  PARTICLE_OFFSETS.map((begin) => (
    <circle key={begin} className="flow-particle" r="6">
      <animateMotion dur={dur} begin={begin} repeatCount="indefinite" calcMode="linear">
        <mpath href={`#${pathId}`} xlinkHref={`#${pathId}`} />
      </animateMotion>
    </circle>
  ));

const FlowNode = ({ node, state, dim }) => {
  const Icon = getFlowIcon(node.icon);

  return (
    <div
      className={`flow-node ${state ? `is-${state}` : ''} ${dim ? 'is-dim' : ''}`}
      style={{
        left: `${node.x}%`,
        top: `${node.y}%`,
        width: `${node.w}%`,
        height: `${node.h}%`
      }}
    >
      <div className="flow-node-icon">
        <Icon />
      </div>
      <div className="flow-node-title">{node.title}</div>
      {node.tech && <div className="flow-node-tech">{node.tech}</div>}
      {node.detail && <div className="flow-node-detail">{node.detail}</div>}
    </div>
  );
};

/**
 * Diagrama de grafo animado paso a paso: zonas, nodos y aristas con partículas de datos
 * viajando por las aristas de la etapa activa.
 */
export const FlowGraph = ({ spec, isActive }) => {
  const { viewBox: vb, steps } = spec;
  const { step, goTo, replay, reduced } = useFlowPlayer(steps.length, isActive, {
    interval: spec.interval
  });

  const current = steps[step];

  const edges = useMemo(() => {
    const byId = Object.fromEntries(spec.nodes.map((n) => [n.id, n]));
    return spec.edges.map((e) => buildEdge(e, byId, vb)).filter(Boolean);
  }, [spec, vb]);

  const activeNodes = new Set(current.nodes || []);
  const activeEdges = new Set(current.edges || []);
  const nodeStates = current.nodeStates || {};
  const edgeStates = current.edgeStates || {};

  /* Los rótulos se recolocan en cada etapa: sólo se rotulan las aristas activas, así que la
     posición óptima depende de cuáles estén encendidas. */
  const labelPos = useMemo(
    () =>
      layoutLabels(
        edges.filter((e) => activeEdges.has(e.id) && e.label && edgeStates[e.id] !== 'blocked'),
        { nodes: spec.nodes, zones: spec.zones, viewBox: vb }
      ),
    [edges, current, spec, vb] // eslint-disable-line react-hooks/exhaustive-deps
  );
  const arrowOn = `${spec.id}-arrow-on`;
  const arrowOff = `${spec.id}-arrow-off`;

  return (
    <div className="flow-shell">
      <div className="flow-canvas-wrap">
        <div className="flow-canvas" style={{ '--flow-ar': vb.w / vb.h }}>
          <svg className="flow-edges" viewBox={`0 0 ${vb.w} ${vb.h}`} aria-hidden="true">
            <defs>
              {[arrowOff, arrowOn].map((id) => (
                <marker
                  key={id}
                  id={id}
                  viewBox="0 0 10 10"
                  refX="9"
                  refY="5"
                  markerWidth="6"
                  markerHeight="6"
                  orient="auto-start-reverse"
                >
                  <path d="M 0 1 L 9 5 L 0 9 z" className={id === arrowOn ? 'arrow-on' : 'arrow-off'} />
                </marker>
              ))}
            </defs>

            {(spec.zones || []).map((z) => (
              <g key={z.id} className={`flow-zone tone-${z.tone || 'slate'}`}>
                <rect
                  x={(z.x / 100) * vb.w}
                  y={(z.y / 100) * vb.h}
                  width={(z.w / 100) * vb.w}
                  height={(z.h / 100) * vb.h}
                  rx="16"
                />
                <text x={(z.x / 100) * vb.w + 14} y={(z.y / 100) * vb.h + 22}>
                  {z.label}
                </text>
              </g>
            ))}

            {edges.map((e) => {
              const on = activeEdges.has(e.id);
              const state = edgeStates[e.id];
              const pathId = `${spec.id}-${e.id}`;

              return (
                <g
                  key={e.id}
                  data-edge={e.id}
                  className={`flow-edge ${on ? 'is-on' : ''} ${state ? `is-${state}` : ''}`}
                >
                  <path
                    id={pathId}
                    d={e.d}
                    markerEnd={`url(#${on ? arrowOn : arrowOff})`}
                  />
                  {on && !reduced && state !== 'blocked' && (
                    <EdgeParticles pathId={pathId} dur={spec.particleDur || '1.5s'} />
                  )}
                </g>
              );
            })}
          </svg>

          {spec.nodes.map((n) => (
            <FlowNode
              key={n.id}
              node={n}
              state={nodeStates[n.id]}
              dim={!activeNodes.has(n.id)}
            />
          ))}

          {/* Rótulos en una capa POR ENCIMA de los nodos. Van aquí y no dentro del SVG de
              trazados porque los nodos son HTML y se pintan sobre el SVG: si el rótulo cae
              sobre una caja, quedaría oculto. Cada uno lleva un chip opaco detrás, de modo
              que al posarse sobre su propia línea la interrumpe limpiamente en vez de
              quedar tachado por ella. */}
          <svg className="flow-labels" viewBox={`0 0 ${vb.w} ${vb.h}`} aria-hidden="true">
            {edges.map((e) => {
              const on = activeEdges.has(e.id);
              const state = edgeStates[e.id];

              /* El aspa de enlace cortado va sobre el punto medio real del trazo. */
              if (state === 'blocked') {
                return (
                  <g key={e.id} data-edge={e.id} className="flow-edge is-blocked">
                    <g className="flow-edge-break" transform={`translate(${e.midX} ${e.midY})`}>
                      <circle r="13" />
                      <path d="M -6 -6 L 6 6 M 6 -6 L -6 6" />
                    </g>
                  </g>
                );
              }

              const pos = labelPos[e.id];
              if (!e.label || !on || !pos) return null;

              return (
                <g key={e.id} data-edge={e.id} className="flow-edge is-on">
                  {pos.tirante && (
                    <line
                      className="flow-edge-leader"
                      x1={pos.x}
                      y1={pos.y}
                      x2={pos.ancla.x}
                      y2={pos.ancla.y}
                    />
                  )}
                  <rect
                    className="flow-edge-chip"
                    x={pos.box.x}
                    y={pos.box.y}
                    width={pos.box.w}
                    height={pos.box.h}
                    rx="6"
                  />
                  <text className="flow-edge-label" x={pos.x} y={pos.y}>
                    {e.label}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>
      </div>

      <aside className="flow-side">
        <FlowStepper steps={steps} current={step} onSelect={goTo} />
        <FlowDetail step={current} index={step} total={steps.length} reduced={reduced} />
        <button type="button" className="flow-hint" onClick={replay}>
          <kbd>↑</kbd> <kbd>↓</kbd> recorrer · <kbd>R</kbd> reiniciar
        </button>
      </aside>
    </div>
  );
};

export default FlowGraph;
