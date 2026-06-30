import re

with open('index.html', 'r') as f:
    c = f.read()

# Current base string that is in all of them
old_villas = "linear-gradient(rgba(11,43,38,0.2), rgba(11,43,38,0.95)), url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400&q=80')"
new_villas = "linear-gradient(rgba(100,30,10,0.6), rgba(100,30,10,0.95)), url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400&q=80')"

old_apts = "linear-gradient(rgba(11,43,38,0.2), rgba(11,43,38,0.95)), url('https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=400&q=80')"
new_apts = "linear-gradient(rgba(15,25,45,0.6), rgba(15,25,45,0.95)), url('https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=400&q=80')"

old_layout = "linear-gradient(rgba(11,43,38,0.2), rgba(11,43,38,0.95)), url('https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=400&q=80')"
new_layout = "linear-gradient(rgba(30,60,40,0.6), rgba(30,60,40,0.95)), url('https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=400&q=80')"

old_rest = "linear-gradient(rgba(11,43,38,0.2), rgba(11,43,38,0.95)), url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400&q=80')"
new_rest = "linear-gradient(rgba(60,20,60,0.6), rgba(60,20,60,0.95)), url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400&q=80')"

old_resort = "linear-gradient(rgba(11,43,38,0.2), rgba(11,43,38,0.95)), url('https://images.unsplash.com/photo-1582610116397-edb318620f90?w=400&q=80')"
new_resort = "linear-gradient(rgba(10,50,60,0.6), rgba(10,50,60,0.95)), url('https://images.unsplash.com/photo-1582610116397-edb318620f90?w=400&q=80')"

old_micro = "linear-gradient(rgba(11,43,38,0.2), rgba(11,43,38,0.95)), url('https://images.unsplash.com/photo-1579621970588-a3f5ce5a0cad?w=400&q=80')"
new_micro = "linear-gradient(rgba(80,50,10,0.6), rgba(80,50,10,0.95)), url('https://images.unsplash.com/photo-1579621970588-a3f5ce5a0cad?w=400&q=80')"

c = c.replace(old_villas, new_villas)
c = c.replace(old_apts, new_apts)
c = c.replace(old_layout, new_layout)
c = c.replace(old_rest, new_rest)
c = c.replace(old_resort, new_resort)
c = c.replace(old_micro, new_micro)

with open('index.html', 'w') as f:
    f.write(c)
