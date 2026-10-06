import React from 'react';

/* Tira vertical de etapas. Clicable para saltar a cualquier punto del flujo si el tribunal
   pregunta por una etapa concreta. */
export const FlowStepper = ({ steps, current, onSelect }) => (
  <ol className="flow-stepper">
    {steps.map((s, i) => (
      <li key={s.id}>
        <button
          type="button"
          className={`flow-step-chip ${i === current ? 'is-current' : ''} ${i < current ? 'is-done' : ''}`}
          onClick={() => onSelect(i)}
          aria-current={i === current ? 'step' : undefined}
        >
          <span className="flow-step-num">{i + 1}</span>
          <span className="flow-step-label">{s.label}</span>
        </button>
      </li>
    ))}
  </ol>
);

export default FlowStepper;
