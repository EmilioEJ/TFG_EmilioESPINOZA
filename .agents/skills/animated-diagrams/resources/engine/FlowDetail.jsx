import React, { useState, useEffect, useRef } from 'react';

/* Contador que sube hasta el valor del paso. Es el recurso narrativo de la diapositiva de
   Store-and-Forward: ver crecer los 86.030 puntos retenidos y luego drenarse a cero. */
const MetricCounter = ({ metric, reduced }) => {
  const { value, from = 0, label, suffix = '', animate = true, tone = 'purple' } = metric;
  const [shown, setShown] = useState(animate && !reduced ? from : value);
  const frame = useRef(0);

  useEffect(() => {
    if (!animate || reduced) {
      setShown(value);
      return undefined;
    }

    const duration = 1100;
    const start = performance.now();

    const tick = (now) => {
      const t = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - t, 3);
      setShown(Math.round(from + (value - from) * eased));
      if (t < 1) frame.current = requestAnimationFrame(tick);
    };

    frame.current = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(frame.current);
  }, [value, from, animate, reduced]);

  return (
    <div className={`flow-metric tone-${tone}`}>
      <div className="flow-metric-value">
        {shown.toLocaleString('es-ES')}
        {suffix}
      </div>
      <div className="flow-metric-label">{label}</div>
    </div>
  );
};

/* Panel del paso activo: lo que el ponente va explicando mientras el dato viaja. */
export const FlowDetail = ({ step, index, total, reduced }) => {
  const detail = step.detail || {};

  return (
    <div className="flow-detail" key={step.id}>
      <div className="flow-detail-head">
        <span className="flow-detail-count">
          Paso {index + 1} / {total}
        </span>
        <h3 className="flow-detail-title">{detail.title || step.label}</h3>
      </div>

      {detail.metric && <MetricCounter metric={detail.metric} reduced={reduced} />}

      {detail.bullets && (
        <ul className="flow-detail-bullets">
          {detail.bullets.map((b) => (
            <li key={b}>{b}</li>
          ))}
        </ul>
      )}

      {detail.code && <code className="flow-detail-code">{detail.code}</code>}

      {detail.note && <p className="flow-detail-note">{detail.note}</p>}
    </div>
  );
};

export default FlowDetail;
