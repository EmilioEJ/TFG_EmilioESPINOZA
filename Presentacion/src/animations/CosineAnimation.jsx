import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';

export const CosineAnimation = () => {
  const [step, setStep] = useState(0);

  // Auto-cycle through the animation states
  useEffect(() => {
    const timer = setInterval(() => {
      setStep((prev) => (prev + 1) % 4);
    }, 4000);
    return () => clearInterval(timer);
  }, []);

  const angles = [
    { title: "Texto irrelevante (90°)", aAngle: 0, bAngle: 90, color: "#9CA3AF" },
    { title: "Texto opuesto (180°)", aAngle: 0, bAngle: 180, color: "#EF4444" },
    { title: "Texto muy similar (15°)", aAngle: 0, bAngle: 15, color: "#F97316" },
    { title: "Texto idéntico (0°)", aAngle: 0, bAngle: 0, color: "#22C55E" }
  ];

  const current = angles[step];
  
  // Calculate vector end points based on angles
  const radius = 150;
  const centerX = 200;
  const centerY = 200;
  
  const bRad = (current.bAngle * Math.PI) / 180;
  const bX = centerX + radius * Math.cos(bRad);
  const bY = centerY - radius * Math.sin(bRad);

  const aX = centerX + radius; // angle 0
  const aY = centerY;

  return (
    <div className="w-full h-full flex flex-col items-center justify-center bg-gray-50 p-8">
      <h2 className="text-3xl font-black text-purple-700 mb-2">Similitud del Coseno (ChromaDB)</h2>
      <p className="text-gray-600 text-xl mb-8">
        Mide el ángulo <span className="font-mono text-orange-600 font-bold px-1">θ</span> entre dos vectores semánticos.
      </p>

      <div className="relative w-[400px] h-[300px] flex items-center justify-center bg-white rounded-2xl shadow-sm border border-gray-200">
        <svg width="400" height="300" viewBox="0 0 400 300" className="overflow-visible">
          {/* Grid lines */}
          <line x1="200" y1="50" x2="200" y2="250" stroke="#E5E7EB" strokeWidth="2" strokeDasharray="4 4" />
          <line x1="50" y1="200" x2="350" y2="200" stroke="#E5E7EB" strokeWidth="2" strokeDasharray="4 4" />

          {/* Angle Arc */}
          {current.bAngle > 0 && current.bAngle < 180 && (
            <motion.path
              d={`M ${centerX + 40} ${centerY} A 40 40 0 0 0 ${centerX + 40 * Math.cos(bRad)} ${centerY - 40 * Math.sin(bRad)}`}
              fill="none"
              stroke={current.color}
              strokeWidth="3"
              initial={{ pathLength: 0 }}
              animate={{ pathLength: 1, d: `M ${centerX + 40} ${centerY} A 40 40 0 0 0 ${centerX + 40 * Math.cos(bRad)} ${centerY - 40 * Math.sin(bRad)}` }}
              transition={{ duration: 0.8 }}
            />
          )}

          {/* Vector A (Base / Query) */}
          <line x1={centerX} y1={centerY} x2={aX} y2={aY} stroke="#9333EA" strokeWidth="4" />
          <polygon points={`${aX},${aY} ${aX-10},${aY-5} ${aX-10},${aY+5}`} fill="#9333EA" />
          <text x={aX + 15} y={aY + 5} fill="#9333EA" fontWeight="bold" fontSize="16">Pregunta</text>

          {/* Vector B (Document) */}
          <motion.line
            x1={centerX} y1={centerY}
            animate={{ x2: bX, y2: bY }}
            transition={{ type: "spring", stiffness: 60 }}
            stroke={current.color} strokeWidth="4"
          />
          <motion.polygon
            animate={{ points: `${bX},${bY} ${bX - 10 * Math.cos(bRad) + 5 * Math.sin(bRad)},${bY + 10 * Math.sin(bRad) + 5 * Math.cos(bRad)} ${bX - 10 * Math.cos(bRad) - 5 * Math.sin(bRad)},${bY + 10 * Math.sin(bRad) - 5 * Math.cos(bRad)}` }}
            transition={{ type: "spring", stiffness: 60 }}
            fill={current.color}
          />
          <motion.text
            animate={{ x: bX + 15 * Math.cos(bRad), y: bY - 15 * Math.sin(bRad) }}
            transition={{ type: "spring", stiffness: 60 }}
            fill={current.color} fontWeight="bold" fontSize="16"
          >
            Reglamento
          </motion.text>
        </svg>

        {/* Dynamic Formula Display */}
        <div className="absolute top-6 left-6 right-6 flex justify-between items-center bg-gray-100 px-4 py-2 rounded-lg border border-gray-200">
          <div className="font-mono text-lg font-bold">
            cos(θ) = <span style={{ color: current.color }}>{Math.cos(bRad).toFixed(2)}</span>
          </div>
          <div className="text-sm font-semibold text-gray-700 uppercase tracking-wider">
            {current.title}
          </div>
        </div>
      </div>
    </div>
  );
};
