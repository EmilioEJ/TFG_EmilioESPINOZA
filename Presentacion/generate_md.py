import re
from bs4 import BeautifulSoup

def generate_slide_order_md():
    with open('/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    slides = soup.find_all('section', class_='slide')
    
    md_content = "# Orden Actual de las Diapositivas\n\nA continuación se presenta la lista actualizada de diapositivas en la presentación, reflejando todos los cambios, reordenamientos y eliminaciones realizados.\n\n"
    
    count = 1
    for slide in slides:
        # Check if it's the cover slide
        cover_title = slide.find(class_='cover-title')
        if cover_title:
            title = cover_title.get_text(separator=' ', strip=True)
            kicker = slide.find(class_='cover-eyebrow')
            kicker_text = kicker.get_text(strip=True) if kicker else 'Portada'
            md_content += f"## Slide {count} | Kicker: {kicker_text} — Título: {title}\n"
            count += 1
            continue
            
        kicker = slide.find(class_='kicker')
        headline = slide.find(class_='headline')
        
        if headline:
            kicker_text = kicker.get_text(strip=True) if kicker else 'Sin Subtema'
            headline_text = headline.get_text(separator=' ', strip=True)
            md_content += f"## Slide {count} | Kicker: {kicker_text} — Título: {headline_text}\n"
            count += 1

    with open('/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/orden_slides_actualizado.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("Markdown generado.")

if __name__ == '__main__':
    generate_slide_order_md()
