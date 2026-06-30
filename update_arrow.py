import re

with open('index.html', 'r') as f:
    c = f.read()

old_path = '<path d="M2 13 L20 3 L16 3 M20 3 L20 7" stroke="var(--text-light)" stroke-width="1.3" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40" stroke-dashoffset="40" opacity="0">'
new_path = '<path d="M2 13 L20 3 L17.5 3 M20 3 L20 5.5" stroke="#00e5ff" stroke-width="1.1" fill="none" stroke-linecap="round" stroke-linejoin="miter" stroke-dasharray="40" stroke-dashoffset="40" opacity="0">'

c = c.replace(old_path, new_path)

with open('index.html', 'w') as f:
    f.write(c)
