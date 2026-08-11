import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS for lines
css_addition = """
  .connectors path, .connectors line {
    stroke: #ececef !important;
    transition: stroke 0.8s ease;
  }
  .connectors path.in, .connectors line.in {
    stroke: #12121a !important;
  }
  #arrow path {
    fill: #ececef;
    transition: fill 0.8s ease;
  }
  #arrow.in path {
    fill: #12121a;
  }
"""
content = content.replace("/* ---------------- EXPERTISE ---------------- */", "/* ---------------- EXPERTISE ---------------- */\n" + css_addition)

# 2. Add classes to SVG lines
# Intro to 01
content = content.replace('<path d="M 380 180 Q 550 50 740 100"', '<path class="l1" d="M 380 180 Q 550 50 740 100"')
# 01 to 02
content = content.replace('<line x1="740"', '<line class="l2" x1="740"')
# 02 to 03
content = content.replace('<line x1="340" y1="700"', '<line class="l3" x1="340" y1="700"')
# 03 to 04
content = content.replace('<line x1="720" y1="980"', '<line class="l4" x1="720" y1="980"')
# 04 to 05
content = content.replace('<line x1="340" y1="1260"', '<line class="l5" x1="340" y1="1260"')

# 3. Update the JavaScript intersection observer
old_js = """
  // Intersection Observer for scroll animations
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ if(e.isIntersecting) e.target.classList.add('in'); });
  }, {threshold:0.15});
"""
new_js = """
  // Intersection Observer for scroll animations
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ 
      if(e.isIntersecting) {
        e.target.classList.add('in'); 
        
        // Trigger lines in Expertise section when cards appear
        if(e.target.classList.contains('c1')) {
            document.querySelector('.l1').classList.add('in');
            document.querySelector('#arrow').classList.add('in');
        }
        if(e.target.classList.contains('c2')) document.querySelector('.l2').classList.add('in');
        if(e.target.classList.contains('c3')) document.querySelector('.l3').classList.add('in');
        if(e.target.classList.contains('c4')) document.querySelector('.l4').classList.add('in');
        if(e.target.classList.contains('c5')) document.querySelector('.l5').classList.add('in');
      }
    });
  }, {threshold:0.15});
"""
content = content.replace(old_js.strip(), new_js.strip())

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Line animations added successfully")
