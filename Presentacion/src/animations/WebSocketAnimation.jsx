import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Server, MonitorSmartphone, AudioWaveform } from 'lucide-react';

export const WebSocketAnimation = () => {
  const [toggle, setToggle] = useState(false);

  useEffect(() => {
    const timer = setInterval(() => {
      setToggle(prev => !prev);
    }, 4500);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="w-full h-full flex flex-col items-center justify-center bg-gray-50 p-8 rounded-2xl">
      <h2 className="text-3xl font-black text-purple-700 mb-8">HTTP vs WebSockets en IA</h2>
      
      <div className="flex gap-16 w-full max-w-5xl justify-center items-start">
        
        {/* HTTP Panel */}
        <div className={`flex flex-col items-center p-6 border-2 rounded-2xl transition-colors duration-500 ${!toggle ? 'border-red-400 bg-red-50 shadow-md' : 'border-gray-200 bg-white opacity-50'}`}>
          <h3 className="font-bold text-xl mb-6 text-red-600">HTTP (Bloqueante)</h3>
          
          <div className="flex items-center gap-12 relative h-32">
            <MonitorSmartphone size={40} className={!toggle ? 'text-red-500' : 'text-gray-400'} />
            
            <div className="relative w-48 h-full">
              {/* HTTP Request */}
              <AnimatePresence>
                {!toggle && (
                  <>
                    <motion.div 
                      className="absolute top-8 left-0 flex items-center"
                      initial={{ x: 0, opacity: 0 }}
                      animate={{ x: 192, opacity: [0, 1, 0] }}
                      transition={{ duration: 2, times: [0, 0.2, 1] }}
                    >
                      <div className="bg-red-500 text-white text-xs px-2 py-1 rounded">Audio (Total)</div>
                      <div className="w-4 h-0.5 bg-red-500" />
                    </motion.div>
                    
                    {/* UI Freeze Indicator */}
                    <motion.div
                      className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-xs font-bold text-red-500 bg-red-100 px-2 py-1 rounded"
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ delay: 2, duration: 0.3 }}
                    >
                      UI Congelada...
                    </motion.div>
                  </>
                )}
              </AnimatePresence>
            </div>
            
            <Server size={40} className={!toggle ? 'text-red-500' : 'text-gray-400'} />
          </div>
          <p className="mt-4 text-sm text-center text-red-700 font-medium max-w-[250px]">
            El cliente espera a que termine TODO el proceso de IA para recibir respuesta.
          </p>
        </div>

        {/* WebSocket Panel */}
        <div className={`flex flex-col items-center p-6 border-2 rounded-2xl transition-colors duration-500 ${toggle ? 'border-green-500 bg-green-50 shadow-md' : 'border-gray-200 bg-white opacity-50'}`}>
          <h3 className="font-bold text-xl mb-6 text-green-700">WebSockets (Streaming)</h3>
          
          <div className="flex items-center gap-12 relative h-32">
            <MonitorSmartphone size={40} className={toggle ? 'text-green-600' : 'text-gray-400'} />
            
            <div className="relative w-48 h-full">
              {/* WS Persistent connection line */}
              <div className={`absolute top-1/2 -translate-y-1/2 w-full border-t-2 border-dashed ${toggle ? 'border-green-400' : 'border-gray-200'}`} />
              
              <AnimatePresence>
                {toggle && (
                  <>
                    {/* Streaming Audio Chunks (Req) */}
                    {[0, 1, 2].map((i) => (
                      <motion.div 
                        key={`ws-req-${i}`}
                        className="absolute top-4 left-0 text-green-600"
                        initial={{ x: 0, opacity: 0 }}
                        animate={{ x: 192, opacity: [0, 1, 0] }}
                        transition={{ delay: i * 0.4, duration: 1.2 }}
                      >
                        <AudioWaveform size={20} />
                      </motion.div>
                    ))}
                    
                    {/* Streaming Status (Res) */}
                    {[0, 1, 2].map((i) => (
                      <motion.div 
                        key={`ws-res-${i}`}
                        className="absolute bottom-4 right-0"
                        initial={{ x: 0, opacity: 0 }}
                        animate={{ x: -192, opacity: [0, 1, 0] }}
                        transition={{ delay: 1.5 + (i * 0.4), duration: 1.2 }}
                      >
                        <div className="bg-green-600 text-white text-[10px] px-2 py-0.5 rounded-full">estado</div>
                      </motion.div>
                    ))}
                  </>
                )}
              </AnimatePresence>
            </div>
            
            <Server size={40} className={toggle ? 'text-green-600' : 'text-gray-400'} />
          </div>
          <p className="mt-4 text-sm text-center text-green-800 font-medium max-w-[250px]">
            Conexión bidireccional. El audio se envía en trozos y la UI se actualiza al instante.
          </p>
        </div>
      </div>
    </div>
  );
};
