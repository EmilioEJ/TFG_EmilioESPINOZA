import re

path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# We want to remove section with id="slide-30" completely
# We know it starts exactly at <section class="slide" data-ch="6" id="slide-30">
# and ends right before <section class="slide" data-ch="6" id="slide-31">

start_str = '<section class="slide" data-ch="6" id="slide-30">'
end_str = '</section>\n<section class="slide" data-ch="6" id="slide-31">'

if start_str in html and end_str in html:
    idx_start = html.find(start_str)
    # We want to remove up to the end of the </section>, so before the start of slide-31
    idx_end = html.find('<section class="slide" data-ch="6" id="slide-31">', idx_start)
    if idx_end != -1:
        html = html[:idx_start] + html[idx_end:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Slide 24 (id: slide-30) removed successfully!")
    else:
        print("Could not find the end of slide-30")
else:
    print("Could not find the start or end string for slide-30")

