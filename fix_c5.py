import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add exception for c5 so it stays white with red border, instead of turning solid red
css_addition = """
  /* Keep Card 5 white with a red border instead of filling it solid red */
  .exp-card.c5.in {
    background-position: top !important; /* Stays white */
    color: var(--ink) !important; /* Text stays dark */
    border-color: var(--red) !important; /* Border turns red */
  }
  .exp-card.c5.in .pin {
    background: var(--red) !important;
  }
"""
content = content.replace("/* Delays for the \"one by one\" fill effect */", css_addition + "\n  /* Delays for the \"one by one\" fill effect */")

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("c5 updated successfully")
