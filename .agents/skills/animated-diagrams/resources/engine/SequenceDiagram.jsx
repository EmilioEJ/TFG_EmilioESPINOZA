import React, { useMemo } from 'react';
import { getFlowIcon } from './icons';
import { useFlowPlayer } from './useFlowPlayer';
import FlowStepper from './FlowStepper';
import FlowDetail from './FlowDetail';

const HEADER_H = 118;
const ROW_H = 46;
const PAD_BOTTOM = 26;
const VB_W = 1000;

/**
 * Diagrama de secuencia animado. A diferencia del grafo, aquí el orden temporal *es* el
 * contenido: los mensajes se revelan acumulativamente y los de la etapa activa se resaltan.
 */
export const SequenceDiagram = ({ spec, isActive }) => {
  const { actors, messages, steps } = spec;
  const { step, goTo, replay, reduced } = useFlowPlayer(steps.length, isActive, {
    interval: spec.interval
  });

  const vbH = HEADER_H + messages.length * ROW_H + PAD_BOTTOM;
  const current = steps[step];

  const layout = useMemo(() => {
    const lane = VB_W / actors.length;
    const xOf = Object.fromEntries(actors.map((a, i) => [a.id, (i + 0.5) * lane]));
    const rows = messages.map((m, i) => ({ ...m, y: HEADER_H + i * ROW_H + ROW_H / 2 }));
    return { lane, xOf, rows };
  }, [actors, messages]);

  /* Un mensaje ya "ocurrió" si pertenece a esta etapa o a cualquiera anterior. */
  const revealed = useMemo(() => {
    const set = new Set();
    for (let i = 0; i <= step; i++) steps[i].messages.forEach((id) => set.add(id));
    return set;
  }, [steps, step]);

  const activeMessages = new Set(current.messages);
  const arrowOn = `${spec.id}-seq-on`;
  const arrowOff = `${spec.id}-seq-off`;

  return (
    <div className="flow-shell">
      <div className="flow-canvas-wrap">
        <div className="flow-canvas is-sequence" style={{ '--flow-ar': VB_W / vbH }}>
          <svg className="flow-edges" viewBox={`0 0 ${VB_W} ${vbH}`} aria-hidden="true">
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

            {actors.map((a) => (
              <line
                key={a.id}
                className="flow-lifeline"
                x1={layout.xOf[a.id]}
                y1={HEADER_H - 12}
                x2={layout.xOf[a.id]}
                y2={vbH - 10}
              />
            ))}

            {layout.rows.map((m) => {
              const on = activeMessages.has(m.id);
              const shown = revealed.has(m.id);
              const cls = `flow-msg is-${m.kind} ${on ? 'is-on' : ''} ${shown ? '' : 'is-hidden'}`;

              if (m.kind === 'note') {
                const xs = m.over.map((id) => layout.xOf[id]);
                const x1 = Math.min(...xs) - layout.lane * 0.34;
                const x2 = Math.max(...xs) + layout.lane * 0.34;
                return (
                  <g key={m.id} className={cls}>
                    <rect x={x1} y={m.y - 15} width={x2 - x1} height="30" rx="8" />
                    <text x={(x1 + x2) / 2} y={m.y + 5}>
                      {m.label}
                    </text>
                  </g>
                );
              }

              if (m.kind === 'self') {
                const x = layout.xOf[m.from];
                const w = layout.lane * 0.3;
                return (
                  <g key={m.id} className={cls}>
                    <path
                      d={`M ${x} ${m.y - 11} L ${x + w} ${m.y - 11} L ${x + w} ${m.y + 8} L ${x + 4} ${m.y + 8}`}
                      markerEnd={`url(#${on ? arrowOn : arrowOff})`}
                    />
                    {/* inline: la clase .flow-msg-label fija text-anchor: middle y el atributo no la vence */}
                    <text className="flow-msg-label" x={x + w + 14} y={m.y + 1} style={{ textAnchor: 'start' }}>
                      {m.label}
                    </text>
                  </g>
                );
              }

              const from = layout.xOf[m.from];
              const to = layout.xOf[m.to];
              const dir = to > from ? 1 : -1;

              return (
                <g key={m.id} className={cls}>
                  <line
                    x1={from + 5 * dir}
                    y1={m.y}
                    x2={to - 7 * dir}
                    y2={m.y}
                    markerEnd={`url(#${on ? arrowOn : arrowOff})`}
                  />
                  <text className="flow-msg-label" x={(from + to) / 2} y={m.y - 9}>
                    {m.label}
                  </text>
                  {m.sub && (
                    <text className="flow-msg-sub" x={(from + to) / 2} y={m.y + 15}>
                      {m.sub}
                    </text>
                  )}
                </g>
              );
            })}
          </svg>

          {actors.map((a, i) => {
            const Icon = getFlowIcon(a.icon);
            const on = current.actors ? current.actors.includes(a.id) : true;
            return (
              <div
                key={a.id}
                className={`flow-actor ${on ? '' : 'is-dim'}`}
                style={{
                  left: `${((i + 0.5) / actors.length) * 100}%`,
                  width: `${(1 / actors.length) * 100 - 2}%`,
                  height: `${((HEADER_H - 28) / vbH) * 100}%`
                }}
              >
                <div className="flow-actor-icon">
                  <Icon />
                </div>
                <div className="flow-actor-label">{a.label}</div>
                {a.sub && <div className="flow-actor-sub">{a.sub}</div>}
              </div>
            );
          })}
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

export default SequenceDiagram;
