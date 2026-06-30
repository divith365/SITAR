import re

with open('index.html', 'r') as f:
    c = f.read()

# Replace all background:#fff; with a softer creamy white
c = c.replace('background:#fff;', 'background:#FBF8F1;')

with open('index.html', 'w') as f:
    f.write(c)
