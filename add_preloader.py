import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add class="preloading" to body
content = content.replace("<body>", '<body class="preloading">')

# 2. Add Preloader HTML right after <body class="preloading">
preloader_html = """
<div id="preloader">
  <div class="loader-text" data-text="ABHIJEET">ABHIJEET</div>
</div>
"""
content = content.replace('<body class="preloading">', '<body class="preloading">\n' + preloader_html)

# 3. Add Preloader CSS
preloader_css = """
  /* ---------------- PRELOADER ---------------- */
  body.preloading { overflow: hidden; }
  #preloader {
    position: fixed; inset: 0; background: var(--red);
    z-index: 99999; display: flex; align-items: center; justify-content: center;
    transition: opacity 0.8s ease, visibility 0.8s ease;
  }
  .loader-text {
    font-size: clamp(50px, 12vw, 120px); font-weight: 800; color: transparent;
    -webkit-text-stroke: 2px rgba(255, 255, 255, 0.3); position: relative; letter-spacing: 0.05em;
  }
  .loader-text::before {
    content: attr(data-text); position: absolute; left: 0; top: 0;
    color: #ffd700; -webkit-text-stroke: 0px transparent; white-space: nowrap;
    overflow: hidden; width: 0%;
    animation: fillText 2.2s cubic-bezier(0.7, 0, 0.3, 1) forwards;
  }
  @keyframes fillText { 0% { width: 0%; } 100% { width: 100%; } }
  body:not(.preloading) #preloader { opacity: 0; visibility: hidden; pointer-events: none; }
"""
content = content.replace('/* ---------------- NAV ---------------- */', preloader_css + '\n  /* ---------------- NAV ---------------- */')

# 4. Add Preloader JS
preloader_js = """
  // Preloader logic
  window.addEventListener('load', () => {
    setTimeout(() => {
      document.body.classList.remove('preloading');
    }, 2500); // Fades out shortly after the text fills
  });
"""
content = content.replace('// Intersection Observer for scroll animations', preloader_js + '\n  // Intersection Observer for scroll animations')

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Preloader added successfully")
