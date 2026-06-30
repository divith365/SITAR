import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Update Snapshot Scale
old_scale = 'transform: scale(0.7);\n    transform-origin: center top;\n  }'
new_scale = 'transform: scale(0.8);\n    transform-origin: center top;\n  }'
c = c.replace(old_scale, new_scale)

# Fix margin for 0.8 scale
old_margin = 'margin:-1px 20px -35px;'
new_margin = 'margin:-1px 20px -20px;'
c = c.replace(old_margin, new_margin)

# 2. Update Card Background Shades (Use ink overlay instead of pure black)
old_villas = "linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7))"
new_villas = "linear-gradient(rgba(11,43,38,0.2), rgba(11,43,38,0.95))"
c = c.replace(old_villas, new_villas) # This replaces it for all 6 cards since they use the same gradient string

# 3. Update Font for sector-rate (Up to...)
old_rate_css = ".sector-rate{font-family:var(--mono); font-size:11.5px; color:#00e5ff; margin-top:4px; text-shadow:0 2px 4px rgba(0,0,0,0.8); font-weight:600;}"
new_rate_css = ".sector-rate{font-family:var(--display); font-size:12px; color:#f7d273; margin-top:5px; text-shadow:0 2px 5px rgba(0,0,0,1); font-weight:700; letter-spacing:0.03em;}"
c = c.replace(old_rate_css, new_rate_css)

with open('index.html', 'w') as f:
    f.write(c)
