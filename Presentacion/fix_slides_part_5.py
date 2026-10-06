import re

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Slide 19 (WebSockets tooltips downward)
# Replace bottom:calc(100% + 10px) with top:calc(100% + 10px); bottom:auto;
# Also transform:translateY(8px) -> translateY(-8px) if needed? 
html = html.replace(
    'bottom:calc(100% + 10px); left:0; right:0; background:white; border:2px solid var(--orange-400);',
    'top:calc(100% + 10px); bottom:auto; left:0; right:0; background:white; border:2px solid var(--orange-400);'
)
html = html.replace(
    'bottom:calc(100% + 10px); left:0; right:0; background:white; border:2px solid var(--purple-400);',
    'top:calc(100% + 10px); bottom:auto; left:0; right:0; background:white; border:2px solid var(--purple-400);'
)
# For the transform when hidden vs shown
# When mouseenter: tip.style.transform='translateY(0)'
# When mouseleave: tip.style.transform='translateY(8px)' (Wait, 8px downwards? If top is used, it should be -8px for hidden).
html = html.replace(
    "if(tip){ tip.style.opacity='0'; tip.style.transform='translateY(8px)'; }",
    "if(tip){ tip.style.opacity='0'; tip.style.transform='translateY(-8px)'; }"
)


# 2. Slide 18 (RAG) Move diagram and cards higher
# Currently: <div class="slide-inner" style="max-width:1300px;">
html = html.replace('<section class="slide" data-ch="5" id="slide-24">\n<div class="slide-inner" style="max-width:1300px;">', 
                    '<section class="slide" data-ch="5" id="slide-24">\n<div class="slide-inner" style="max-width:1300px; padding-top: 50px !important;">')
# SVG margin
html = html.replace('<div class="diag diag-large" data-anim="ragflow" id="diagRagFlow" style="margin-top:4px;">', 
                    '<div class="diag diag-large" data-anim="ragflow" id="diagRagFlow" style="margin-top:-20px;">')


# 3. Slide 16 (ChromaDB) Expand text
old_s25_inner = '<div class="slide-inner" style="max-width: 1000px; margin: 0 auto;">'
new_s25_inner = '<div class="slide-inner" style="max-width: 1200px; margin: 0 auto; text-align: center;">'
html = html.replace(old_s25_inner, new_s25_inner)

html = html.replace('<h2 class="headline" style="max-width:40ch">Base de datos vectorial (NoSQL): Diseño del conocimiento en tres capas.</h2>',
                    '<h2 class="headline" style="max-width:none; text-align:center;">Base de datos vectorial (NoSQL): Diseño del conocimiento en tres capas.</h2>')
html = html.replace('<p class="subhead" style="margin-bottom: 30px; max-width: 56ch;">ChromaDB desnormaliza a propósito:',
                    '<p class="subhead" style="margin-bottom: 40px; max-width: none; text-align:center; display:inline-block;">ChromaDB desnormaliza a propósito:')


# 4. Slide 15 (Contexto - slide-20) 
# Fix overlap: move text left and justify
old_ctx_text = '<p class="subhead" style="text-align:center; margin:10px auto 0; max-width:70ch;">El estudiante provee estímulos;'
new_ctx_text = '<p class="subhead" style="text-align:justify; margin:10px 0 0 20px; max-width:75ch;">El estudiante provee estímulos;'
html = html.replace(old_ctx_text, new_ctx_text)
# Optional: remove the extra </section> we found there
html = html.replace('</section>\n</section>\n<section class="slide" data-ch="5" id="slide-25">',
                    '</section>\n<section class="slide" data-ch="5" id="slide-25">')

# 5. Slide 12 (Fases de Desarrollo - slide-fases) 
# Make it larger
old_fases_svg = '<svg height="120" style="overflow:visible;" viewbox="0 0 1000 120" width="100%">'
new_fases_svg = '<svg height="120" style="overflow:visible; transform:scale(1.35); transform-origin:top center; margin-top:40px;" viewbox="0 0 1000 120" width="100%">'
html = html.replace(old_fases_svg, new_fases_svg)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Changes applied successfully!")
