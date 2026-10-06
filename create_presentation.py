import collections.abc
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    
    # Optional: Change slide size to Widescreen (16:9)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Helper function
    def add_slide_bullets(title, bullets, img_path=None):
        layout = prs.slide_layouts[1] if img_path is None else prs.slide_layouts[5] # 1 is Title+Body, 5 is Title Only
        slide = prs.slides.add_slide(layout)
        
        # Title
        title_shape = slide.shapes.title
        title_shape.text = title
        
        if img_path is None:
            # Body
            body_shape = slide.placeholders[1]
            tf = body_shape.text_frame
            tf.clear()
            for b in bullets:
                p = tf.add_paragraph()
                p.text = b
                p.font.size = Pt(28)
                p.space_after = Pt(14)
                p.level = 0
        else:
            # Add image
            if os.path.exists(img_path):
                # Try to center image below title
                slide.shapes.add_picture(img_path, Inches(0.5), Inches(1.5), width=Inches(7))
            
            # Add text box for bullets
            if bullets:
                txBox = slide.shapes.add_textbox(Inches(8), Inches(1.5), Inches(5), Inches(5))
                tf = txBox.text_frame
                for b in bullets:
                    p = tf.add_paragraph()
                    p.text = b
                    p.font.size = Pt(24)
                    p.space_after = Pt(14)
                    p.level = 0

        return slide

    def add_full_image(title, img_path):
        slide = prs.slides.add_slide(prs.slide_layouts[5])
        slide.shapes.title.text = title
        if os.path.exists(img_path):
            slide.shapes.add_picture(img_path, Inches(2), Inches(1.5), height=Inches(5.5))
        return slide

    # 1. Portada
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = "Asistente Virtual Inteligente con Avatar 3D, Visión Artificial y RAG"
    slide.placeholders[1].text = "Defensa de Tesis\nPaulo Emilio Espinoza Jiménez\nIngeniería en Tecnologías de la Información"
    if os.path.exists("Logos/LOGO-UTI-1.png"):
        slide.shapes.add_picture("Logos/LOGO-UTI-1.png", Inches(0.5), Inches(0.5), width=Inches(2))

    # 2. Instrucciones para el usuario (diapositiva temporal)
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "¡Atención! (Borrar esta diapositiva)"
    tf = slide.placeholders[1].text_frame
    tf.text = "Para activar las animaciones de 'clic a clic' que solicitaste:"
    p = tf.add_paragraph()
    p.text = "1. Selecciona todo el texto de una diapositiva (Ctrl+E)."
    p = tf.add_paragraph()
    p.text = "2. Ve a la pestaña 'Animaciones' arriba en PowerPoint."
    p = tf.add_paragraph()
    p.text = "3. Haz clic en 'Aparecer'."
    p = tf.add_paragraph()
    p.text = "4. ¡Listo! Al presentar, cada punto aparecerá con un clic, ideal para explicar paso a paso."

    # 3. El Problema
    add_slide_bullets("¿Cuál es el Problema Actual?", [
        "Estudiantes pierden tiempo buscando normativas o mallas curriculares.",
        "Los sistemas actuales (PDFs, webs institucionales) son estáticos y lentos.",
        "Dudas frecuentes saturan al personal de secretaría.",
        "Falta un sistema proactivo y amigable que responda de inmediato."
    ])

    # 4. Nuestra Solución
    add_slide_bullets("Nuestra Solución: Asistente Inteligente", [
        "Un Asistente Virtual 3D interactivo y accesible 24/7.",
        "Responde preguntas en lenguaje natural (como un humano).",
        "Conoce exactamente los reglamentos y la información de la institución.",
        "Detecta visualmente al usuario para iniciar la conversación."
    ])

    # 5. IA Generativa (Explicación para no expertos)
    add_slide_bullets("Concepto Clave: IA Generativa", [
        "¿Qué es? Una tecnología que puede 'crear' texto, entender preguntas y conversar (ej. ChatGPT).",
        "Problema: Las IAs normales inventan cosas ('alucinan') cuando no saben una respuesta.",
        "Tampoco conocen documentos privados de nuestra institución.",
        "¿Cómo lo solucionamos? Con la tecnología RAG."
    ])

    # 6. ¿Qué es RAG?
    add_slide_bullets("¿Qué es RAG? (Generación Aumentada por Recuperación)", [
        "Es como darle a la IA un 'libro de reglas abierto' antes de que responda.",
        "1. El estudiante hace una pregunta.",
        "2. El sistema 'Busca' (Recuperación) en nuestros PDF oficiales.",
        "3. Le pasamos esos párrafos exactos a la IA.",
        "4. La IA 'Genera' una respuesta precisa sin inventar nada."
    ])

    # 7. Avatar 3D y Visión Artificial
    add_slide_bullets("Interactividad: Avatar 3D y Visión Artificial", [
        "Visión Artificial: Usamos la cámara para saber si hay una persona enfrente.",
        "Si detecta a alguien, el Asistente se 'despierta' y saluda.",
        "Avatar 3D: Da un rostro humano, habla con voz sintetizada y mueve los labios (lipsync).",
        "Hace que la tecnología se sienta más cercana y menos fría."
    ])

    # 8. Metodología
    add_slide_bullets("¿Cómo se construyó? (Metodología)", [
        "Metodología DSRM (Ciencia de Diseño): Enfoque en crear un producto (artefacto) que resuelva un problema real.",
        "Marco de Trabajo Scrum: Desarrollo ágil, paso a paso (Sprints).",
        "Mejoras constantes probando el asistente varias veces."
    ])

    # 9. Arquitectura (Contexto)
    add_full_image("Arquitectura del Sistema (Vista General)", "Logos/nuevo_diagrama_contexto.jpeg")

    # 10. Arquitectura (Software)
    add_full_image("Arquitectura del Software (Cliente - Servidor)", "Logos/diagrama_arquitectura_software.jpeg")

    # 11. El Motor RAG (Base de Datos Vectorial)
    add_full_image("¿Cómo se busca la información? (Motor Vectorial)", "Logos/Diagrama de base de datos vectorial.jpeg")

    # 12. Modelos de IA Utilizados
    add_slide_bullets("El 'Cerebro' del Sistema", [
        "Para entender los textos (Embeddings): Usamos 'paraphrase-multilingual-MiniLM'. Es excelente entendiendo español.",
        "Para responder (LLM): Usamos 'Nemotron' (de Nvidia).",
        "Se ejecuta localmente, lo que asegura total privacidad de los datos."
    ])

    # 13. Interfaz del Estudiante (Chat)
    add_full_image("Interfaz del Estudiante: Chat por Texto", "Logos/Seccion_Chatear.png")

    # 14. Interfaz del Estudiante (Conversacional/Voz)
    add_full_image("Interfaz del Estudiante: Chat por Voz y Avatar", "Logos/Seccion_Conversacional.png")

    # 15. Interfaz del Administrador
    add_full_image("Interfaz del Administrador: Subir Documentos", "Logos/Seccion_AdminRAG.png")

    # 16. Resultados: Precisión de Respuestas
    add_slide_bullets("Resultados: ¿Es preciso respondiendo?", [
        "Medimos el 'Hit Rate' (Tasa de acierto).",
        "El sistema logró un 92.0% de acierto al encontrar el reglamento correcto.",
        "Casi siempre entrega la información exacta que el estudiante pidió."
    ])

    # 17. Resultados: Tiempo de Respuesta
    add_slide_bullets("Resultados: ¿Es rápido?", [
        "Medimos el TTFB (Tiempo hasta el primer byte).",
        "El promedio es de 450 milisegundos (¡Menos de medio segundo!).",
        "La conversación se siente muy natural y sin pausas largas, gracias a la tecnología WebSockets."
    ])

    # 18. Resultados: Usabilidad (Evaluación de Estudiantes)
    add_full_image("Resultados: Usabilidad (Encuesta a Estudiantes)", "Logos/PREGUNTA1.png")

    # 19. Resultados: Usabilidad (Detalles)
    add_slide_bullets("¿Qué opinaron los estudiantes?", [
        "13 estudiantes evaluaron el prototipo.",
        "Alta calificación en Facilidad de Uso.",
        "Confirmaron que la experiencia con el Avatar 3D es mucho más atractiva que un buscador tradicional."
    ])

    # 20. Conclusiones Principales
    add_slide_bullets("Conclusiones Principales", [
        "RAG funciona: Permite que la IA use documentos institucionales sin cometer errores.",
        "Privacidad total: Todo corre en servidores locales, sin pagar por consultas a la nube.",
        "Multimodal: La combinación de Texto, Voz, Visión y Avatar 3D transforma el servicio estudiantil."
    ])

    # 21. Impacto y Trabajo Futuro
    add_slide_bullets("Impacto y Futuro", [
        "Reduce la carga operativa en secretaría y mejora la experiencia del alumno.",
        "A futuro: Se puede integrar directamente con el sistema de notas para respuestas personalizadas.",
        "Se puede añadir soporte para más idiomas."
    ])

    # 22. Demostración
    slide = prs.slides.add_slide(prs.slide_layouts[5]) # Title only
    slide.shapes.title.text = "Demostración del Sistema"
    txBox = slide.shapes.add_textbox(Inches(3), Inches(3), Inches(7), Inches(2))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = "(Espacio reservado para mostrar el software en vivo)"
    p.font.size = Pt(32)
    p.font.italic = True

    # 23. Preguntas
    slide = prs.slides.add_slide(prs.slide_layouts[0]) # Title slide
    slide.shapes.title.text = "¿Preguntas?"
    slide.placeholders[1].text = "¡Gracias por su atención!"

    prs.save("Presentacion_Defensa_Tesis.pptx")
    print("Presentación guardada exitosamente como Presentacion_Defensa_Tesis.pptx")

if __name__ == '__main__':
    create_presentation()
