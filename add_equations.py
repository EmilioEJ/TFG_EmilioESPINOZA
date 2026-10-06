import re

def main():
    filepath = "/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Capítulos/03_Implementación.tex"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the \textit typo (\t interpreted as tab in previous python run)
    content = content.replace("\textitchunks", "\\textit{chunks}")
    content = content.replace("	extit{chunks}", "\\textit{chunks}")
    content = content.replace("	extit{streams}", "\\textit{streams}")
    content = content.replace("	extit{Top-3}", "\\textit{Top-3}")
    content = content.replace("	extit{manos libres}", "\\textit{manos libres}")

    # Inject Equation 1 (Presence)
    target1 = r"1. Recibir fotogramas ligeros vía WebSockets y calcular el área del \\textit\{bounding box\} del rostro para determinar presencia activa."
    replacement1 = r"""1. Recibir fotogramas ligeros vía WebSockets y calcular el área del \textit{bounding box} del rostro para determinar presencia activa, de acuerdo al siguiente modelo lógico:

\begin{equation}
\label{eq:presence}
Estado = 
\begin{cases} 
Activo, & \text{si } (W_{box} \times H_{box}) > \tau_{pixeles} \\
Reposo, & \text{de lo contrario}
\end{cases}
\end{equation}
\addeqtolist{Cálculo lógico para detección de presencia del usuario vía WebSockets}"""
    content = content.replace(target1, replacement1)

    # Inject Latency Equations
    target2 = r"La conjunción de APIs de inferencia ultrarrápida (Groq/Whisper) fue clave para este logro operativo."
    replacement2 = r"""La conjunción de APIs de inferencia ultrarrápida (Groq/Whisper) fue clave para este logro operativo.

Para evaluar la reducción de latencia de forma rigurosa y determinar la fiabilidad del sistema en producción, se aplicaron las siguientes fórmulas estadísticas sobre los registros de telemetría:

\begin{equation}
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
\end{equation}
\addeqtolist{Media aritmética de la latencia (TTFB)}

\begin{equation}
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
\end{equation}
\addeqtolist{Desviación estándar de los tiempos de respuesta}

\begin{equation}
IC_{95} = 1.96 \times \left( \frac{s}{\sqrt{n}} \right)
\end{equation}
\addeqtolist{Intervalo de Confianza al 95\%}

Estos cálculos garantizan que el sistema responde de forma estable dentro de los intervalos de confianza permitidos (Tabla~\ref{tab:registro_telemetria})."""
    content = content.replace(target2, replacement2)

    # Inject Hit Rate Equation
    target3 = r"Los resultados globales de la muestra estadística arrojaron una Media de Latencia ($\bar{x}$) de 3571 ms y una precisión semántica (\textit{Hit Rate}) del 90,0\%, validando formalmente el Requerimiento No Funcional de Rendimiento establecido."
    replacement3 = r"""Para evaluar rigurosamente el motor de recuperación semántica sin necesidad de reentrenar (\textit{fine-tuning}) el LLM, se utilizó la siguiente fórmula matemática:

\begin{equation}
\text{Hit Rate} = \left( \frac{\text{Consultas Correctas}}{N_{total}} \right) \times 100
\end{equation}
\addeqtolist{Tasa de Acierto de Recuperación Semántica (Hit Rate)}

Los resultados globales de la muestra estadística arrojaron una Media de Latencia ($\bar{x}$) de 3571 ms y una precisión semántica (\textit{Hit Rate}) del 90,0\%, validando formalmente el Requerimiento No Funcional de Rendimiento establecido."""
    if target3 in content:
        content = content.replace(target3, replacement3)
    else:
        # Fallback if target3 is different
        target3_alt = r"A nivel del Motor de IA, la exactitud y capacidad resolutiva se cuantificó a través de un \textit{Hit Rate}. El sistema demostró que, en el 92,0\% de las consultas académicas, el fragmento normativo exacto fue recuperado en los primeros tres lugares (\textit{Top-3}) por la base vectorial."
        replacement3_alt = r"""A nivel del Motor de IA, la exactitud y capacidad resolutiva se cuantificó a través de un \textit{Hit Rate}, que evalúa rigurosamente el motor de recuperación semántica de la siguiente manera:

\begin{equation}
\text{Hit Rate} = \left( \frac{\text{Consultas Correctas}}{N_{total}} \right) \times 100
\end{equation}
\addeqtolist{Tasa de Acierto de Recuperación Semántica (Hit Rate)}

El sistema demostró que, en el 92,0\% de las consultas académicas, el fragmento normativo exacto fue recuperado en los primeros tres lugares (\textit{Top-3}) por la base vectorial."""
        content = content.replace(target3_alt, replacement3_alt)


    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success")

if __name__ == "__main__":
    main()
