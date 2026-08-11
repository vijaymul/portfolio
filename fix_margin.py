import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to replace the rootMargin of expIo
old_margin = 'rootMargin: "-25% 0px -25% 0px"'
new_margin = 'rootMargin: "10000px 0px -25% 0px"'
content = content.replace(old_margin, new_margin)

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Root margin updated successfully")
