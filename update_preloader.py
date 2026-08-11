import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the preloader CSS transitions
old_css1 = "transition: opacity 0.8s ease, visibility 0.8s ease;"
new_css1 = "transition: transform 0.9s cubic-bezier(0.7, 0, 0.3, 1), visibility 0.9s;"
content = content.replace(old_css1, new_css1)

old_css2 = "body:not(.preloading) #preloader { opacity: 0; visibility: hidden; pointer-events: none; }"
new_css2 = "body:not(.preloading) #preloader { transform: translateY(-100%); visibility: hidden; pointer-events: none; }"
content = content.replace(old_css2, new_css2)

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Curtain slide up animation added successfully")
