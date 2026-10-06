import { useState, useEffect, useCallback, useRef } from 'react';

const prefersReducedMotion = () =>
  typeof window !== 'undefined' &&
  window.matchMedia &&
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/**
 * Control de reproducción compartido por todos los diagramas de flujo.
 *
 * Al entrar a la diapositiva el flujo arranca en el paso 0 y avanza solo hasta el último,
 * donde se detiene: durante la defensa no interesa que el diagrama siga moviéndose mientras
 * se responde al tribunal. Cualquier interacción manual (teclas ↑/↓ o clic en el stepper)
 * cancela el avance automático.
 */
export function useFlowPlayer(stepCount, isActive, { interval = 2400 } = {}) {
  const reduced = useRef(prefersReducedMotion()).current;
  const [step, setStep] = useState(0);
  const [playing, setPlaying] = useState(!reduced);

  const clamp = useCallback(
    (i) => Math.max(0, Math.min(stepCount - 1, i)),
    [stepCount]
  );

  /* Manual: fija el paso y corta el autoplay. */
  const goTo = useCallback(
    (i) => {
      setPlaying(false);
      setStep(clamp(i));
    },
    [clamp]
  );

  const next = useCallback(() => goTo(step + 1), [goTo, step]);
  const prev = useCallback(() => goTo(step - 1), [goTo, step]);
  const replay = useCallback(() => {
    setStep(0);
    setPlaying(true);
  }, []);

  /* La diapositiva se remonta al navegar hacia ella (ver la key de visitas en App), pero
     este reset cubre además el caso de que el componente sobreviva al cambio. */
  useEffect(() => {
    if (isActive) {
      setStep(0);
      setPlaying(!reduced);
    }
  }, [isActive, reduced]);

  useEffect(() => {
    if (!isActive || !playing) return undefined;
    if (step >= stepCount - 1) {
      setPlaying(false);
      return undefined;
    }
    const timer = setTimeout(() => setStep((s) => Math.min(s + 1, stepCount - 1)), interval);
    return () => clearTimeout(timer);
  }, [isActive, playing, step, stepCount, interval]);

  /* ↑/↓ recorren los pasos del flujo. ←/→ los deja libres para navegar entre
     diapositivas, que es lo que ya escucha App. */
  useEffect(() => {
    if (!isActive) return undefined;

    const onKeyDown = (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        goTo(step + 1);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        goTo(step - 1);
      } else if (e.key === 'r' || e.key === 'R') {
        e.preventDefault();
        replay();
      }
    };

    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [isActive, step, goTo, replay]);

  return { step, playing, goTo, next, prev, replay, reduced };
}
