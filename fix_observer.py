import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove 'reveal' class from exp-card elements
content = content.replace('class="exp-card c1 reveal"', 'class="exp-card c1"')
content = content.replace('class="exp-card c2 reveal"', 'class="exp-card c2"')
content = content.replace('class="exp-card c3 reveal"', 'class="exp-card c3"')
content = content.replace('class="exp-card c4 reveal"', 'class="exp-card c4"')
content = content.replace('class="exp-card c5 reveal"', 'class="exp-card c5"')

# 2. Rewrite the JS section
old_js = """
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
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
"""

new_js = """
  // Intersection Observer for scroll animations (general)
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ 
      if(e.isIntersecting) {
        e.target.classList.add('in'); 
      }
    });
  }, {threshold:0.15});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

  // Dedicated Intersection Observer for Expertise Cards
  // rootMargin ensures it only triggers when the card enters the middle 50% of the screen
  const expIo = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ 
      if(e.isIntersecting) {
        e.target.classList.add('in'); 
        
        // Trigger lines in Expertise section when cards appear
        if(e.target.classList.contains('c1')) {
            let l1 = document.querySelector('.l1');
            if(l1) l1.classList.add('in');
            let arr = document.querySelector('#arrow');
            if(arr) arr.classList.add('in');
        }
        if(e.target.classList.contains('c2')) { let l2 = document.querySelector('.l2'); if(l2) l2.classList.add('in'); }
        if(e.target.classList.contains('c3')) { let l3 = document.querySelector('.l3'); if(l3) l3.classList.add('in'); }
        if(e.target.classList.contains('c4')) { let l4 = document.querySelector('.l4'); if(l4) l4.classList.add('in'); }
        if(e.target.classList.contains('c5')) { let l5 = document.querySelector('.l5'); if(l5) l5.classList.add('in'); }
      }
    });
  }, {threshold: 0.1, rootMargin: "-25% 0px -25% 0px"});
  
  document.querySelectorAll('.exp-card').forEach(el=>expIo.observe(el));
"""
# Need to use a generic replace without exact whitespace, or regex, or just replace the block.
# I'll use regex to replace everything between "// Intersection Observer for scroll animations" and "document.querySelectorAll('.reveal').forEach(el=>io.observe(el));"

pattern = re.compile(r'// Intersection Observer for scroll animations.*?document\.querySelectorAll\(\'\.reveal\'\)\.forEach\(el=>io\.observe\(el\)\);', re.DOTALL)
content = pattern.sub(new_js.strip(), content)

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("JS updated successfully")
