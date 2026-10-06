import React, { useState, useEffect, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import ReactMarkdown from 'react-markdown';
import { Maximize, Minimize } from 'lucide-react';
import { slidesData } from './slidesData';

// Map slide indices to the 9 chapters
const chapterMap = [
  { start: 0, end: 0, label: "Portada" },
  { start: 1, end: 4, label: "Capítulo I: Contexto y Planteamiento" },
  { start: 5, end: 6, label: "Estado del Arte y Aporte" },
  { start: 7, end: 10, label: "Metas y Justificación" },
  { start: 11, end: 13, label: "Fundamentación Teórica" },
  { start: 14, end: 17, label: "Capítulo II: Metodología" },
  { start: 18, end: 24, label: "Diseño de Solución" },
  { start: 25, end: 28, label: "Capítulo III: Implementación" },
  { start: 29, end: 31, label: "Capítulo IV: Conclusiones" }
];

const getChapterIndex = (slideIndex) => {
  for (let i = 0; i < chapterMap.length; i++) {
    if (slideIndex >= chapterMap[i].start && slideIndex <= chapterMap[i].end) {
      return i;
    }
  }
  return 0;
};

export const SlideEngine = ({ customDiagrams = {} }) => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [direction, setDirection] = useState(0);
  const [isFullscreen, setIsFullscreen] = useState(false);

  const totalSlides = slidesData.length;

  const navigate = useCallback((newIndex) => {
    if (newIndex >= 0 && newIndex < totalSlides) {
      setDirection(newIndex > currentSlide ? 1 : -1);
      setCurrentSlide(newIndex);
    }
  }, [currentSlide, totalSlides]);

  const handleKeyDown = useCallback((e) => {
    // Only use Right/Left/Space for slide navigation.
    // Up/Down are reserved for the diagram step navigation.
    if (e.key === 'ArrowRight' || e.key === ' ') {
      navigate(currentSlide + 1);
    } else if (e.key === 'ArrowLeft') {
      navigate(currentSlide - 1);
    }
  }, [currentSlide, navigate]);

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
      setIsFullscreen(true);
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
        setIsFullscreen(false);
      }
    }
  };

  const handleEdgeClick = (e) => {
    const { clientX } = e;
    const width = window.innerWidth;
    if (clientX < width * 0.25) {
      navigate(currentSlide - 1);
    } else if (clientX > width * 0.75) {
      navigate(currentSlide + 1);
    }
  };

  const slide = slidesData[currentSlide];
  const currentChapter = getChapterIndex(currentSlide);
  const progress = ((currentSlide + 1) / totalSlides) * 100;

  return (
    <div 
      className="w-full min-h-screen bg-white text-gray-900 flex flex-col relative overflow-hidden select-none"
      onClick={handleEdgeClick}
    >
      {/* Top Progress Bar */}
      <div className="absolute top-0 left-0 w-full h-1 bg-gray-200 z-50">
        <div 
          className="h-full bg-orange-500 transition-all duration-300 ease-out"
          style={{ width: `${progress}%` }}
        />
      </div>

      {/* Left Chapter Rail */}
      <div className="absolute left-4 top-1/2 -translate-y-1/2 flex flex-col gap-3 z-50 pointer-events-none">
        {chapterMap.map((chap, idx) => (
          <div 
            key={idx} 
            className={`w-2.5 h-2.5 rounded-full transition-all duration-300 ${
              idx === currentChapter ? 'bg-orange-500 scale-125' : 'bg-gray-300'
            }`}
            title={chap.label}
          />
        ))}
      </div>

      {/* Fullscreen Button */}
      <button 
        className="absolute top-4 right-4 z-50 p-2 text-gray-500 hover:text-orange-500 transition-colors pointer-events-auto"
        onClick={(e) => { e.stopPropagation(); toggleFullscreen(); }}
      >
        {isFullscreen ? <Minimize size={20} /> : <Maximize size={20} />}
      </button>

      {/* Slide Content Area */}
      <div className="flex-1 w-full max-w-7xl mx-auto px-16 py-12 flex flex-col justify-center relative pointer-events-none">
        <AnimatePresence mode="wait" custom={direction}>
          <motion.div
            key={currentSlide}
            custom={direction}
            initial={{ opacity: 0, x: direction * 50 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -direction * 50 }}
            transition={{ duration: 0.4, ease: "easeInOut" }}
            className="w-full h-full flex flex-col"
          >
            {/* Header */}
            {slide.title && (
              <h1 className="text-4xl md:text-5xl font-black text-purple-700 mb-8 tracking-tight pointer-events-auto">
                {slide.title}
              </h1>
            )}

            {/* Custom Diagram or Markdown */}
            <div className="flex-1 flex flex-col w-full h-full text-lg md:text-2xl text-gray-700 leading-relaxed pointer-events-auto">
              {customDiagrams[currentSlide] ? (
                <div className="flex-1 w-full h-full flex flex-col bg-gray-50 rounded-2xl border border-gray-200 overflow-hidden shadow-xl p-4 sm:p-6">
                  {customDiagrams[currentSlide]}
                </div>
              ) : (
                <ReactMarkdown 
                  components={{
                    h1: ({node, ...props}) => <h1 className="text-4xl font-bold text-purple-700 mb-6" {...props} />,
                    h2: ({node, ...props}) => <h2 className="text-3xl font-bold text-gray-900 mb-4" {...props} />,
                    p: ({node, ...props}) => <p className="mb-4" {...props} />,
                    ul: ({node, ...props}) => <ul className="list-disc pl-8 mb-6 space-y-3" {...props} />,
                    li: ({node, ...props}) => <li {...props} />,
                    strong: ({node, ...props}) => <strong className="font-extrabold text-orange-600" {...props} />,
                  }}
                >
                  {slide.content}
                </ReactMarkdown>
              )}
            </div>
          </motion.div>
        </AnimatePresence>
      </div>

      {/* Slide Counter Footer */}
      <div className="absolute bottom-4 right-6 text-sm font-mono text-gray-400 z-50 pointer-events-none">
        {currentSlide + 1} / {totalSlides}
      </div>
    </div>
  );
};
