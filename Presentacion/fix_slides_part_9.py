import re

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <ol class="agenda-list" ...> with grid version
pattern = r'<ol class="agenda-list"[^>]*>'
new_ol = '<ol class="agenda-list" style="margin-top:40px; display:grid; grid-template-rows: repeat(4, auto); grid-auto-flow: column; gap: 20px 40px; list-style: none; padding: 0;">'
html = re.sub(pattern, new_ol, html, count=1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Contenido list updated.")
