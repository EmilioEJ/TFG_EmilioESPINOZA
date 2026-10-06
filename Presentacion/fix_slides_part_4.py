path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# WebSockets text sizes are still a bit small in the SVG (specifically the "Estudiante: Envía audio completo" etc)
old_ws_text1 = '<text class="pop" fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="13" font-weight="600" text-anchor="middle" x="200" y="65">'
new_ws_text1 = '<text class="pop" fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="200" y="65">'
html = html.replace(old_ws_text1, new_ws_text1)

old_ws_text2 = '<text class="pop" fill="var(--ink-soft)" font-family="IBM Plex Sans" font-size="13" font-style="italic" text-anchor="middle" x="500" y="65">'
new_ws_text2 = '<text class="pop" fill="var(--ink-soft)" font-family="IBM Plex Sans" font-size="15" font-style="italic" font-weight="600" text-anchor="middle" x="500" y="65">'
html = html.replace(old_ws_text2, new_ws_text2)

old_ws_text3 = '<text class="pop" fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="13" font-weight="600" text-anchor="middle" x="800" y="65">'
new_ws_text3 = '<text class="pop" fill="var(--orange-700)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="800" y="65">'
html = html.replace(old_ws_text3, new_ws_text3)

old_ws_text4 = '<text class="pop" fill="var(--purple-700)" font-family="IBM Plex Sans" font-size="13" font-weight="600" text-anchor="middle" x="125" y="200">'
new_ws_text4 = '<text class="pop" fill="var(--purple-700)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="125" y="200">'
html = html.replace(old_ws_text4, new_ws_text4)

old_ws_text5 = '<text class="pop" fill="var(--purple-700)" font-family="IBM Plex Sans" font-size="13" font-weight="600" text-anchor="middle" x="560" y="200">'
new_ws_text5 = '<text class="pop" fill="var(--purple-700)" font-family="IBM Plex Sans" font-size="15" font-weight="700" text-anchor="middle" x="560" y="200">'
html = html.replace(old_ws_text5, new_ws_text5)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
