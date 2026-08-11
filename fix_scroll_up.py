import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update .pin CSS to be a centered circle with a white ring and grey center
old_pin = """.exp-card .pin{ 
    width:9px; height:9px; border-radius:50%; margin-bottom:12px;
    background:var(--line); 
    transition: background 0.6s ease;
  }
  .exp-card.in .pin{ 
    background:rgba(255,255,255,0.5); 
  }"""
new_pin = """.exp-card .pin {
    display: block;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    margin: 0 auto 16px;
    background: #e2e8f0;
    border: 3px solid rgba(255,255,255,0.8);
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.15), 0 2px 5px rgba(0,0,0,0.1);
    transition: border-color 0.6s ease;
  }
  .exp-card.in .pin {
    border-color: rgba(255,255,255,0.95);
  }"""
content = content.replace(old_pin, new_pin)

# If old_pin wasn't matched because of whitespace, let's use regex
if old_pin not in content:
    content = re.sub(r'\.exp-card \.pin\s*\{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.exp-card\.in \.pin\s*\{.*?\}', '', content, flags=re.DOTALL)
    content = content.replace("/* Delays for the \"one by one\" fill effect */", new_pin + "\n  /* Delays for the \"one by one\" fill effect */")

# 2. Remove the c5 override I added earlier
c5_override = """/* Keep Card 5 white with a red border instead of filling it solid red */
  .exp-card.c5.in {
    background-position: top !important; /* Stays white */
    color: var(--ink) !important; /* Text stays dark */
    border-color: var(--red) !important; /* Border turns red */
  }
  .exp-card.c5.in .pin {
    background: var(--red) !important;
  }"""
content = content.replace(c5_override, "")

# 3. Update the JavaScript intersection observer to handle else (remove class)
new_js = """
  // Intersection Observer for scroll animations (general)
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ 
      if(e.isIntersecting) {
        e.target.classList.add('in'); 
      } else {
        e.target.classList.remove('in');
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
            let l1 = document.querySelector('.l1'); if(l1) l1.classList.add('in');
            let arr = document.querySelector('#arrow'); if(arr) arr.classList.add('in');
        }
        if(e.target.classList.contains('c2')) { let l2 = document.querySelector('.l2'); if(l2) l2.classList.add('in'); }
        if(e.target.classList.contains('c3')) { let l3 = document.querySelector('.l3'); if(l3) l3.classList.add('in'); }
        if(e.target.classList.contains('c4')) { let l4 = document.querySelector('.l4'); if(l4) l4.classList.add('in'); }
        if(e.target.classList.contains('c5')) { let l5 = document.querySelector('.l5'); if(l5) l5.classList.add('in'); }
      } else {
        e.target.classList.remove('in'); 
        
        if(e.target.classList.contains('c1')) {
            let l1 = document.querySelector('.l1'); if(l1) l1.classList.remove('in');
            let arr = document.querySelector('#arrow'); if(arr) arr.classList.remove('in');
        }
        if(e.target.classList.contains('c2')) { let l2 = document.querySelector('.l2'); if(l2) l2.classList.remove('in'); }
        if(e.target.classList.contains('c3')) { let l3 = document.querySelector('.l3'); if(l3) l3.classList.remove('in'); }
        if(e.target.classList.contains('c4')) { let l4 = document.querySelector('.l4'); if(l4) l4.classList.remove('in'); }
        if(e.target.classList.contains('c5')) { let l5 = document.querySelector('.l5'); if(l5) l5.classList.remove('in'); }
      }
    });
  }, {threshold: 0.1, rootMargin: "-25% 0px -25% 0px"});
  
  document.querySelectorAll('.exp-card').forEach(el=>expIo.observe(el));
"""
pattern = re.compile(r'// Intersection Observer for scroll animations \(general\).*?document\.querySelectorAll\(\'\.exp-card\'\)\.forEach\(el=>expIo\.observe\(el\)\);', re.DOTALL)
content = pattern.sub(new_js.strip(), content)

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Changes applied successfully")
