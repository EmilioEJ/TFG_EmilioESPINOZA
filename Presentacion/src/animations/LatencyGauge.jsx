import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Activity, Brain, Volume2 } from 'lucide-react';

export const LatencyGauge = () => {
  const [phase, setPhase] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setPhase(prev => (prev + 1) % 4);
    }, 3000);
    return () => clearInterval(timer);
  }, []);

  const metrics = [
    { title: "Transcripción (STT)", value: 300, icon: <Activity size={24} />, color: "#3B82F6", label: "ms", activeAt: 1 },
    { title: "Búsqueda (RAG)", value: 150, icon: <Database size={24} />, color: "#8B5CF6", label: "ms", activeAt: 2 },
    { title: "Generación + TTS", value: 800, icon: <Volume2 size={24} />, color: "#F59E0B", label: "ms", activeAt: 3 }
  ];

  const total = phase === 0 ? 0 : 
                phase === 1 ? 300 : 
                phase === 2 ? 450 : 1250;

  // Circumference calculation for SVG Gauge
  const radius = 120;
  const circumference = 2 * Math.PI * radius;
  // Max is 1500ms (1.5s), representing full circle
  const maxTime = 1500;
  const strokeDashoffset = circumference - (total / maxTime) * circumference;

  return (
    <div className="w-full h-full flex flex-col items-center justify-center bg-gray-50 p-8 rounded-2xl">
      <h2 className="text-3xl font-black text-purple-700 mb-2">Desglose de Latencia</h2>
      <p className="text-gray-500 mb-10">Meta conversacional: Menor a 1.5 Segundos</p>

      <div className="flex flex-col md:flex-row gap-16 items-center">
        
        {/* SVG Circular Gauge */}
        <div className="relative w-[300px] h-[300px] flex items-center justify-center">
          <svg className="w-full h-full transform -rotate-90">
            {/* Background Circle */}
            <circle
              cx="150" cy="150" r={radius}
              stroke="#E5E7EB" strokeWidth="20" fill="none"
            />
            {/* Progress Circle */}
            <motion.circle
              cx="150" cy="150" r={radius}
              stroke="#F97316" strokeWidth="20" fill="none"
              strokeLinecap="round"
              strokeDasharray={circumference}
              animate={{ strokeDashoffset }}
              transition={{ duration: 0.8, ease: "easeOut" }}
            />
          </svg>
          
          <div className="absolute flex flex-col items-center">
            <span className="text-5xl font-black text-gray-800 tabular-nums tracking-tighter">
              {(total / 1000).toFixed(2)}
            </span>
            <span className="text-xl font-bold text-gray-400 mt-1">Segundos</span>
          </div>
        </div>

        {/* Legend / Breakdown */}
        <div className="flex flex-col gap-6 w-full max-w-sm">
          {metrics.map((m, idx) => {
            const isActive = phase >= m.activeAt;
            return (
              <div 
                key={idx} 
                className={`flex items-center gap-4 p-4 rounded-xl border-2 transition-all duration-500 ${
                  isActive ? 'bg-white border-gray-200 shadow-sm' : 'bg-transparent border-transparent opacity-40'
                }`}
              >
                <div 
                  className="w-12 h-12 rounded-full flex items-center justify-center text-white"
                  style={{ backgroundColor: isActive ? m.color : '#9CA3AF' }}
                >
                  {m.icon}
                </div>
                <div className="flex-1">
                  <div className={`font-bold ${isActive ? 'text-gray-900' : 'text-gray-500'}`}>
                    {m.title}
                  </div>
                  <div className="text-sm font-mono text-gray-500 mt-1">
                    {isActive ? m.value : 0} {m.label}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

// Quick Database icon fallback since it wasn't imported at the top
const Database = ({ size }) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
    <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
    <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
  </svg>
);
