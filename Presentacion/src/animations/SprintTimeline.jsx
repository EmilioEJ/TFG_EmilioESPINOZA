import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Database, Brain, Webcam, Rocket, MonitorCheck } from 'lucide-react';

export const SprintTimeline = () => {
  const [activeSprint, setActiveSprint] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setActiveSprint((prev) => (prev + 1) % 5);
    }, 3500);
    return () => clearInterval(timer);
  }, []);

  const sprints = [
    {
      id: 1,
      title: "Fase 1",
      name: "Data Engineering",
      icon: <Database size={24} />,
      desc: "Recopilación documental y limpieza de datos (PDFs a Markdown)."
    },
    {
      id: 2,
      title: "Fase 2",
      name: "Pipeline RAG",
      icon: <Brain size={24} />,
      desc: "Construcción de ChromaDB y vectorización (Embeddings)."
    },
    {
      id: 3,
      title: "Fase 3",
      name: "Multimodalidad",
      icon: <Webcam size={24} />,
      desc: "Desarrollo de interfaces visuales y de voz (Groq STT/TTS)."
    },
    {
      id: 4,
      title: "Fase 4",
      name: "Integración",
      icon: <MonitorCheck size={24} />,
      desc: "Pruebas de estrés, ajuste de latencia y prevención de alucinaciones."
    },
    {
      id: 5,
      title: "Fase 5",
      name: "Despliegue",
      icon: <Rocket size={24} />,
      desc: "Empaquetado en Docker Compose y validación final."
    }
  ];

  return (
    <div className="w-full h-full flex flex-col items-center justify-center bg-gray-50 p-8 rounded-2xl">
      <h2 className="text-3xl font-black text-purple-700 mb-12">Plan de Trabajo (Metodología Ágil)</h2>
      
      <div className="w-full max-w-4xl relative flex items-center justify-between">
        {/* Connecting Line */}
        <div className="absolute left-0 right-0 h-1 bg-gray-200 top-6 -z-10" />
        <motion.div 
          className="absolute left-0 h-1 bg-orange-500 top-6 -z-10" 
          initial={{ width: "0%" }}
          animate={{ width: `${(activeSprint / (sprints.length - 1)) * 100}%` }}
          transition={{ duration: 0.5, ease: "easeInOut" }}
        />

        {sprints.map((sprint, idx) => {
          const isActive = idx === activeSprint;
          const isPast = idx < activeSprint;
          
          return (
            <div key={sprint.id} className="flex flex-col items-center relative w-32">
              <motion.div 
                className={`w-12 h-12 rounded-full flex items-center justify-center border-4 shadow-sm z-10 transition-colors duration-300 ${
                  isActive ? 'bg-orange-500 border-orange-200 text-white shadow-orange-500/50' : 
                  isPast ? 'bg-purple-600 border-purple-200 text-white' : 
                  'bg-white border-gray-300 text-gray-400'
                }`}
                animate={isActive ? { scale: [1, 1.2, 1] } : { scale: 1 }}
                transition={isActive ? { repeat: Infinity, duration: 2 } : {}}
              >
                {sprint.icon}
              </motion.div>
              
              <div className="mt-4 text-center">
                <div className={`font-mono text-sm font-bold ${isActive || isPast ? 'text-purple-700' : 'text-gray-400'}`}>
                  {sprint.title}
                </div>
                <div className={`font-bold mt-1 text-sm ${isActive ? 'text-gray-900' : 'text-gray-500'}`}>
                  {sprint.name}
                </div>
              </div>

              {/* Popup Description */}
              <AnimatePresence>
                {isActive && (
                  <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: 10 }}
                    className="absolute top-28 w-64 bg-white border border-gray-200 shadow-xl rounded-xl p-4 text-center z-20 pointer-events-none"
                  >
                    <p className="text-gray-700 text-sm leading-relaxed">{sprint.desc}</p>
                    <div className="absolute -top-2 left-1/2 -translate-x-1/2 w-4 h-4 bg-white border-l border-t border-gray-200 rotate-45" />
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          );
        })}
      </div>
    </div>
  );
};
