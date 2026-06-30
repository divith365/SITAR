import re

with open('index.html', 'r') as f:
    c = f.read()

# Update Sector Card CSS
old_css = """  .sector-card{
    background:#fff; border:1px solid #e4ddc9; border-radius:14px;
    padding:14px; cursor:pointer; transition:transform .15s;
    position:relative;
  }
  .sector-card:active{transform:scale(.97);}
  .sector-icon{font-size:22px;}
  .sector-name{font-family:var(--display); font-weight:600; font-size:15px; margin-top:8px;}
  .sector-rate{font-family:var(--mono); font-size:11px; color:var(--green-good); margin-top:4px;}"""

new_css = """  .bg-villas { background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400&q=80') center/cover; }
  .bg-apartments { background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=400&q=80') center/cover; }
  .bg-layout { background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=400&q=80') center/cover; }
  .bg-restaurants { background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400&q=80') center/cover; }
  .bg-resorts { background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1582610116397-edb318620f90?w=400&q=80') center/cover; }
  .bg-microfinance { background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1579621970588-a3f5ce5a0cad?w=400&q=80') center/cover; }
  .sector-card{
    background:#fff; border:none; border-radius:14px;
    padding:14px; cursor:pointer; transition:transform .15s, opacity .15s;
    position:relative; overflow:hidden;
    box-shadow:0 4px 10px rgba(0,0,0,0.25);
  }
  .sector-card:active{transform:scale(.92); opacity:0.85;}
  .sector-icon{font-size:22px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));}
  .sector-name{font-family:var(--display); font-weight:600; font-size:15px; margin-top:8px; color:#fff; text-shadow:0 2px 4px rgba(0,0,0,0.8);}
  .sector-rate{font-family:var(--mono); font-size:11.5px; color:#00e5ff; margin-top:4px; text-shadow:0 2px 4px rgba(0,0,0,0.8); font-weight:600;}"""

c = c.replace(old_css, new_css)

# Update HTML classes
c = c.replace('<div class="sector-card" onclick="openSector(\'Villas\',', '<div class="sector-card bg-villas" onclick="openSector(\'Villas\',')
c = c.replace('<div class="sector-card" onclick="openSector(\'Apartments\',', '<div class="sector-card bg-apartments" onclick="openSector(\'Apartments\',')
c = c.replace('<div class="sector-card" onclick="openSector(\'Layout Development\',', '<div class="sector-card bg-layout" onclick="openSector(\'Layout Development\',')
c = c.replace('<div class="sector-card" onclick="openSector(\'Restaurants\',', '<div class="sector-card bg-restaurants" onclick="openSector(\'Restaurants\',')
c = c.replace('<div class="sector-card" onclick="openSector(\'Resorts\',', '<div class="sector-card bg-resorts" onclick="openSector(\'Resorts\',')
c = c.replace('<div class="sector-card" onclick="openSector(\'Microfinance\',', '<div class="sector-card bg-microfinance" onclick="openSector(\'Microfinance\',')

with open('index.html', 'w') as f:
    f.write(c)
