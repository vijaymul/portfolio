import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update min-height of exp-collage
content = content.replace("min-height:1500px;", "min-height:1700px;")

# Update CSS top positions
content = content.replace(".exp-card.c2{ top:300px;", ".exp-card.c2{ top:460px;")
content = content.replace(".exp-card.c3{ top:580px;", ".exp-card.c3{ top:740px;")
content = content.replace(".exp-card.c4{ top:860px;", ".exp-card.c4{ top:1020px;")
content = content.replace(".exp-card.c5{ top:1140px;", ".exp-card.c5{ top:1300px;")
content = content.replace("top: 960px;", "top: 1600px;") # exp-tagline

# Update SVG
content = content.replace('viewBox="0 0 1040 1500"', 'viewBox="0 0 1040 1700"')
content = content.replace('x1="740" y1="280" x2="340" y2="400"', 'x1="740" y1="280" x2="340" y2="520"')
content = content.replace('x1="340" y1="580" x2="720" y2="680"', 'x1="340" y1="700" x2="720" y2="820"')
content = content.replace('x1="720" y1="880" x2="340" y2="980"', 'x1="720" y1="980" x2="340" y2="1080"')
content = content.replace('x1="340" y1="1140" x2="700" y2="1240"', 'x1="340" y1="1260" x2="700" y2="1360"')

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Overlap fixed")
