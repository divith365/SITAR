import re

with open('index.html', 'r') as f:
    c = f.read()

# Update .snapshot block
old_snapshot = """  .snapshot{
    background:
      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='200' viewBox='0 0 400 200'%3E%3Cpolyline points='10,160 70,130 130,145 190,90 250,100 310,45 390,20' fill='none' stroke='%23D4A647' stroke-opacity='0.16' stroke-width='3'/%3E%3Ccircle cx='390' cy='20' r='5' fill='%23D4A647' fill-opacity='0.25'/%3E%3Ctext x='250' y='175' font-family='Georgia,serif' font-size='70' fill='%23D4A647' fill-opacity='0.07'%3E%E2%82%B9%3C/text%3E%3C/svg%3E"),
      var(--ink);
    background-repeat:no-repeat;
    background-position:right -10px bottom -10px;
    background-size:78%;
    color:var(--text-light);
    margin:-1px 20px 0; border-radius:var(--radius);
    padding:16px 18px; position:relative; overflow:hidden;
    box-shadow:0 14px 28px rgba(11,43,38,.25);
    flex-shrink:0;
  }"""

new_snapshot = """  .snapshot{
    background:
      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='200' viewBox='0 0 400 200'%3E%3Cpolyline points='10,160 70,130 130,145 190,90 250,100 310,45 390,20' fill='none' stroke='%23D4A647' stroke-opacity='0.16' stroke-width='3'/%3E%3Ccircle cx='390' cy='20' r='5' fill='%23D4A647' fill-opacity='0.25'/%3E%3Ctext x='250' y='175' font-family='Georgia,serif' font-size='70' fill='%23D4A647' fill-opacity='0.07'%3E%E2%82%B9%3C/text%3E%3C/svg%3E"),
      var(--ink);
    background-repeat:no-repeat;
    background-position:right -10px bottom -10px;
    background-size:78%;
    color:var(--text-light);
    margin:-1px 20px -35px; border-radius:var(--radius);
    padding:16px 18px; position:relative; overflow:hidden;
    box-shadow:0 14px 28px rgba(11,43,38,.25);
    flex-shrink:0;
    transform: scale(0.7);
    transform-origin: center top;
  }"""
c = c.replace(old_snapshot, new_snapshot)

# Update texts
old_texts = """  .snapshot-label{font-family:var(--mono); font-size:9px; letter-spacing:.13em; text-transform:uppercase; color:var(--text-muted);}
  .snapshot-amt{font-family:var(--display); font-size:14px; font-weight:600; margin:3px 0 12px; color:var(--gold-soft);}
  .snapshot-row{display:flex; gap:10px; flex-wrap:nowrap; justify-content:space-between;}
  .snapshot-stat{min-width:0;}
  .snapshot-stat .v{font-family:var(--mono); font-size:13.5px; font-weight:600; color:var(--text-light); white-space:nowrap;}
  .snapshot-stat .l{font-size:9.5px; color:var(--text-muted); margin-top:2px; white-space:nowrap;}"""

new_texts = """  .snapshot-label{font-family:var(--mono); font-size:9px; letter-spacing:.13em; text-transform:uppercase; color:#f1aeb5;}
  .snapshot-amt{font-family:var(--display); font-size:14px; font-weight:600; margin:3px 0 12px; background:linear-gradient(90deg, #f7d273, #ff8a00); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
  .snapshot-row{display:flex; gap:10px; flex-wrap:nowrap; justify-content:space-between;}
  .snapshot-stat{min-width:0;}
  .snapshot-stat .v{font-family:var(--mono); font-size:13.5px; font-weight:600; color:#5ee7df; white-space:nowrap;}
  .snapshot-stat .l{font-size:9.5px; color:#b490ca; margin-top:2px; white-space:nowrap;}"""
c = c.replace(old_texts, new_texts)

with open('index.html', 'w') as f:
    f.write(c)
