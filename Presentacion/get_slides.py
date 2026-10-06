import re
with open('presentacion_final.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.split(r'<section\b[^>]*class="[^"]*\bslide\b[^"]*"[^>]*>', html)[1:]
for i, slide in enumerate(slides, 1):
    m = re.search(r'<h2[^>]*>(.*?)</h2', slide, re.DOTALL | re.IGNORECASE)
    title = m.group(1).strip() if m else "No title"
    title = re.sub(r'<[^>]+>', '', title).replace('\n', ' ')
    
    # Try to find ID to map it back
    id_m = re.search(r'id="([^"]+)"', html.split(slide)[0].split('<section')[-1])
    slide_id = id_m.group(1) if id_m else "unknown"
    print(f"Slide {i} [{slide_id}]: {title}")
