import re

def fix_avatar_hover_bug():
    path = '/home/emilioej/EmilioEJ/TFG_EmilioESPINOZA/Presentacion/presentacion_final.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # The bug is this CSS rule which overwrites the SVG transform="translate(x,y)"
    bad_css = """
.state-node:hover {
  transform: scale(1.05);
}"""
    
    # We replace it with scaling just the circle inside the state-node.
    # We also make sure the tooltip is positioned perfectly.
    good_css = """
.state-node circle {
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.3s ease, stroke 0.3s ease !important;
  transform-origin: center center;
}
.state-node:hover circle {
  transform: scale(1.15);
  filter: drop-shadow(0 10px 20px rgba(98, 36, 184, 0.3));
}
"""
    if bad_css in html:
        html = html.replace(bad_css, good_css)
    else:
        # Just in case it's formatted differently
        html = re.sub(r'\.state-node:hover\s*\{\s*transform:\s*scale\(1\.05\);\s*\}', good_css, html)

    # Let's also make sure the tooltip looks amazing and doesn't flicker
    # We will improve the stateTooltip styling
    tooltip_css_find = 'id="stateTooltip" style="position:absolute; bottom:-40px; left:50%; transform:translateX(-50%); background:var(--purple-50); border:2px solid var(--purple-200); border-radius:12px; padding:20px 30px; font-size:18px; color:var(--ink); text-align:center; width:90%; opacity:0; transition:opacity 0.3s ease; pointer-events:none; z-index:1000; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"'
    tooltip_css_replace = 'id="stateTooltip" style="position:absolute; bottom:-20px; left:50%; transform:translateX(-50%); background:white; border:3px solid var(--purple-400); border-radius:16px; padding:25px 35px; font-size:20px; font-weight:500; color:var(--purple-950); text-align:center; width:100%; opacity:0; transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); pointer-events:none; z-index:1000; box-shadow: 0 15px 40px rgba(83, 52, 127, 0.2);"'
    
    html = html.replace(tooltip_css_find, tooltip_css_replace)
    
    # To fix the JS so the tooltip slides up elegantly when opacity is 1
    js_tooltip_find = """tip.textContent = this.getAttribute('data-tooltip');
        tip.style.opacity = '1';"""
    js_tooltip_replace = """tip.textContent = this.getAttribute('data-tooltip');
        tip.style.opacity = '1';
        tip.style.bottom = '-40px';"""
        
    js_tooltip_hide_find = """tip.style.opacity = '0';"""
    js_tooltip_hide_replace = """tip.style.opacity = '0';
        tip.style.bottom = '-60px';"""

    html = html.replace(js_tooltip_find, js_tooltip_replace)
    html = html.replace(js_tooltip_hide_find, js_tooltip_hide_replace)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Fixed hover bug and improved tooltip UI.")

if __name__ == '__main__':
    fix_avatar_hover_bug()
