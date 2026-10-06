import re

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Slide Contenido: 4 a la izquierda, 4 a la derecha
old_ol = '<ol class="agenda-list" style="margin-top:20px; display:flex; flex-direction:column; gap: 10px;">'
new_ol = '<ol class="agenda-list" style="margin-top:40px; display:grid; grid-template-rows: repeat(4, auto); grid-auto-flow: column; gap: 20px 40px;">'
if old_ol in html:
    html = html.replace(old_ol, new_ol)
else:
    print("Could not find the <ol> in Contenido")

# 2. Eliminar la slide 16 (Base de datos vectorial - slide-25)
start_str = '<section class="slide" data-ch="5" id="slide-25">'
# We need to find the end of this section. It ends right before id="slide-22"
end_str = '</section>\n<section class="slide" data-ch="5" id="slide-22">'
if start_str in html and end_str in html:
    idx_start = html.find(start_str)
    idx_end = html.find('<section class="slide" data-ch="5" id="slide-22">', idx_start)
    if idx_end != -1:
        html = html[:idx_start] + html[idx_end:]
        print("Slide 16 (Base de datos vectorial) eliminada")
else:
    print("Could not find slide-25 or slide-22")

# 3. Quitar la fila de carga operativa humana en slide-table5
row_to_remove = """<div class="card" style="display:flex; justify-content:space-between; align-items:center; box-shadow:0 10px 30px rgba(0,0,0,0.05);">
<div style="flex:1;"><b>Carga operativa humana</b><p style="font-size:12px; color:var(--ink-faint);">Resolución de dudas recurrentes</p></div>
<div style="flex:1; text-align:center; color:var(--ink-soft); text-decoration:line-through;">100 h/mes</div>
<div style="flex:1; text-align:right; font-size:32px; font-weight:bold; color:var(--orange-500);">Ahorro <span data-count="85" data-suffix="h">0</span></div>
</div>"""

if row_to_remove in html:
    html = html.replace(row_to_remove, '')
    print("Fila de 'Carga operativa humana' eliminada")
else:
    print("Could not find the row 'Carga operativa humana'")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
