import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Remove CSS animation block
css_to_remove = """  /* Logo Animation */
  .b1 { animation: b1 3.5s infinite; opacity:0; }
  .b2 { animation: b2 3.5s infinite; opacity:0; }
  .b3 { animation: b3 3.5s infinite; opacity:0; }
  .b4 { animation: b4 3.5s infinite; opacity:0; }
  .b5 { animation: b5 3.5s infinite; opacity:0; }
  .arr { animation: drawArr 3.5s infinite; stroke-dasharray: 40; stroke-dashoffset: 40; opacity:0; }
  @keyframes b1 { 0%, 95%, 100%{opacity:0} 5%, 90%{opacity:1} }
  @keyframes b2 { 0%, 10%, 95%, 100%{opacity:0} 15%, 90%{opacity:1} }
  @keyframes b3 { 0%, 20%, 95%, 100%{opacity:0} 25%, 90%{opacity:1} }
  @keyframes b4 { 0%, 30%, 95%, 100%{opacity:0} 35%, 90%{opacity:1} }
  @keyframes b5 { 0%, 40%, 95%, 100%{opacity:0} 45%, 90%{opacity:1} }
  @keyframes drawArr {
    0%, 45%, 95%, 100% { stroke-dashoffset: 40; opacity:0; }
    46% { opacity:1; }
    65%, 90% { stroke-dashoffset: 0; opacity:1; }
  }"""
c = c.replace(css_to_remove, "")

# 2. Replace SVG
old_svg = '<svg viewBox="0 0 24 24" width="100%" height="100%"><rect class="b1" x="1" y="16" width="2.5" height="4" rx="1" fill="var(--rust)"/><rect class="b2" x="5.5" y="13" width="2.5" height="7" rx="1" fill="var(--gold-soft)"/><rect class="b3" x="10" y="10" width="2.5" height="10" rx="1" fill="var(--gold)"/><rect class="b4" x="14.5" y="7" width="2.5" height="13" rx="1" fill="var(--text-muted)"/><rect class="b5" x="19" y="4" width="2.5" height="16" rx="1" fill="var(--green-good)"/><path class="arr" d="M2 13 L20 3 L16 3 M20 3 L20 7" stroke="var(--text-light)" stroke-width="1.3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
new_svg = '<svg viewBox="0 0 24 24" width="100%" height="100%"><rect x="1" y="16" width="2.5" height="4" rx="1" fill="var(--rust)" opacity="0"><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.9;1" dur="3.5s" repeatCount="indefinite"/></rect><rect x="5.5" y="13" width="2.5" height="7" rx="1" fill="var(--gold-soft)" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.1;0.15;0.9;1" dur="3.5s" repeatCount="indefinite"/></rect><rect x="10" y="10" width="2.5" height="10" rx="1" fill="var(--gold)" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.2;0.25;0.9;1" dur="3.5s" repeatCount="indefinite"/></rect><rect x="14.5" y="7" width="2.5" height="13" rx="1" fill="var(--text-muted)" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.3;0.35;0.9;1" dur="3.5s" repeatCount="indefinite"/></rect><rect x="19" y="4" width="2.5" height="16" rx="1" fill="var(--green-good)" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.4;0.45;0.9;1" dur="3.5s" repeatCount="indefinite"/></rect><path d="M2 13 L20 3 L16 3 M20 3 L20 7" stroke="var(--text-light)" stroke-width="1.3" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40" stroke-dashoffset="40" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.45;0.46;0.9;1" dur="3.5s" repeatCount="indefinite"/><animate attributeName="stroke-dashoffset" values="40;40;0;0;40" keyTimes="0;0.46;0.65;0.9;1" dur="3.5s" repeatCount="indefinite"/></path></svg>'
c = c.replace(old_svg, new_svg)

# 3. Increase .ic font size
c = c.replace('.navitem .ic{font-size:17px;}', '.navitem .ic{font-size:20px;}')

# 4. Replace Emojis
c = c.replace('<div class="ic">⌂</div>Home', '<div class="ic">🏠</div>Home')
c = c.replace('<div class="ic">◔</div>Portfolio', '<div class="ic">📊</div>Portfolio')
c = c.replace('<div class="ic">⋯</div>More', '<div class="ic">⚙️</div>More')

with open('index.html', 'w') as f:
    f.write(c)
