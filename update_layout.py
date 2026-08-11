import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace EXPERTISE CSS
new_css = """/* ---------------- EXPERTISE ---------------- */
  .expertise{ padding:120px 40px 60px; background:#fff; }
  .exp-intro{ 
    max-width:380px; 
    margin-bottom:40px; 
    position:absolute; 
    top:0; 
    left:20px; 
    z-index:10;
  }
  .exp-intro h2{font-size:clamp(30px,5vw,50px); font-weight:800; line-height:1.12; margin-bottom:18px; letter-spacing:-0.02em;}
  .exp-intro p{color:var(--gray); font-size:15.5px; line-height:1.7; max-width:480px;}

  .exp-collage{
    position:relative;
    max-width:1040px; 
    margin:0 auto;
    min-height:1500px;
  }
  .exp-collage svg.connectors{ position:absolute; inset:0; width:100%; height:100%; pointer-events:none; }
  
  .exp-card{
    position:absolute;
    width:320px;
    border-radius:16px;
    padding:24px;
    box-shadow:0 18px 34px rgba(0,0,0,0.12);
    animation:float 6s ease-in-out infinite;
    opacity:0;
    
    background: linear-gradient(to top, var(--red) 50%, #fff 50%);
    background-size: 100% 200%;
    background-position: top;
    border: 1.5px solid var(--line);
    color: var(--ink);
    
    transition: background-position 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), 
                color 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), 
                opacity 0.6s ease, 
                border-color 0.6s ease,
                box-shadow 0.3s ease;
  }
  .exp-card.in{ 
    opacity:1; 
    background-position: bottom; 
    color:#fff; 
    border-color:var(--red);
  }
  
  .exp-card .pin{ 
    width:9px; height:9px; border-radius:50%; margin-bottom:12px;
    background:var(--line); 
    transition: background 0.6s ease;
  }
  .exp-card.in .pin{ 
    background:rgba(255,255,255,0.5); 
  }
  
  .exp-card .num{ font-family:'Space Mono',monospace; font-size:11px; opacity:0.7; display:block; margin-bottom:8px;}
  .exp-card h3{ font-size:19px; font-weight:700; margin-bottom:12px; line-height:1.3; letter-spacing:-0.01em;}
  .exp-card p{ font-size:12.5px; line-height:1.6; opacity:0.9; }

  /* Delays for the "one by one" fill effect */
  .exp-card.c1{ top:0px; right:20px; left:auto; transform:rotate(4deg); animation-delay:0s; }
  .exp-card.c2{ top:300px; left:20px; transform:rotate(-3deg); animation-delay:.6s; }
  .exp-card.c3{ top:580px; right:20px; left:auto; transform:rotate(2deg); animation-delay:1.2s; }
  .exp-card.c4{ top:860px; left:40px; transform:rotate(-4deg); animation-delay:1.8s; }
  .exp-card.c5{ top:1140px; right:40px; left:auto; transform:rotate(3deg); animation-delay:2.4s; }

  .exp-card.c1.in{ transition-delay: 0s, 0s, 0s, 0s, 0s; }
  .exp-card.c2.in{ transition-delay: 0.15s, 0.15s, 0s, 0.15s, 0s; }
  .exp-card.c3.in{ transition-delay: 0.3s, 0.3s, 0s, 0.3s, 0s; }
  .exp-card.c4.in{ transition-delay: 0.45s, 0.45s, 0s, 0.45s, 0s; }
  .exp-card.c5.in{ transition-delay: 0.6s, 0.6s, 0s, 0.6s, 0s; }

  .exp-tagline {
    position: absolute;
    top: 960px;
    left: 55%;
    transform: translateX(-50%);
    text-align:center; font-weight:700; font-size:22px; color:var(--gray);
  }
  .exp-tagline .accent{color:var(--red);}

  @keyframes float{
    0%,100%{ transform:translateY(0) rotate(var(--r,0deg)); }
    50%{ transform:translateY(-10px) rotate(var(--r,0deg)); }
  }
  .exp-card.c1{--r:4deg;} .exp-card.c2{--r:-3deg;} .exp-card.c3{--r:2deg;} .exp-card.c4{--r:-4deg;} .exp-card.c5{--r:3deg;}

  @media (max-width:900px){
    .exp-collage{min-height:auto;}
    .exp-collage svg.connectors{display:none;}
    .exp-intro {position:static; max-width:100%;}
    .exp-tagline {position:static; transform:none; margin-top:40px;}
    .exp-card{ position:static; width:100%; margin-bottom:18px; transform:none !important; animation:none !important; }
  }

  /* ---------------- TOOLS ---------------- */"""

css_pattern = re.compile(r'/\* ---------------- EXPERTISE ---------------- \*/.*?/\* ---------------- TOOLS ---------------- \*/', re.DOTALL)
content = css_pattern.sub(new_css, content)

# Replace EXPERTISE HTML
new_html = """<section class="expertise" id="expertise">
  <div class="wrap">
    <div class="exp-collage">
      <div class="exp-intro reveal">
        <span class="pill-tag">My Expertise</span>
        <h2>Building Modern Digital Solutions with Code &amp; AI</h2>
        <p>Combining full-stack development, artificial intelligence, and cloud technologies to create scalable and impactful digital experiences.</p>
      </div>
      
      <svg class="connectors" viewBox="0 0 1040 1500" preserveAspectRatio="none">
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#12121a" />
          </marker>
        </defs>
        <!-- Intro to 01 -->
        <path d="M 380 180 Q 550 50 740 100" stroke="#12121a" stroke-width="1.5" stroke-dasharray="6 6" fill="none" marker-end="url(#arrow)"/>
        <!-- 01 to 02 -->
        <line x1="740" y1="280" x2="340" y2="400" stroke="#12121a" stroke-width="1.5" stroke-dasharray="6 6"/>
        <!-- 02 to 03 -->
        <line x1="340" y1="580" x2="720" y2="680" stroke="#12121a" stroke-width="1.5" stroke-dasharray="6 6"/>
        <!-- 03 to 04 -->
        <line x1="720" y1="880" x2="340" y2="980" stroke="#12121a" stroke-width="1.5" stroke-dasharray="6 6"/>
        <!-- 04 to 05 -->
        <line x1="340" y1="1140" x2="700" y2="1240" stroke="#12121a" stroke-width="1.5" stroke-dasharray="6 6"/>
      </svg>

      <div class="exp-card c1 reveal">
        <span class="pin"></span>
        <span class="num">01</span>
        <h3>Frontend Development</h3>
        <p>Building immersive, high-performance web experiences with React, Next.js, TypeScript, JavaScript, Tailwind CSS, GSAP, Framer Motion, Three.js, React Three Fiber, and Lenis. Focused on responsive design, cinematic animations, interactive 3D experiences, and pixel-perfect interfaces that combine storytelling, performance, and exceptional user experiences.</p>
      </div>
      
      <div class="exp-card c2 reveal">
        <span class="pin"></span>
        <span class="num">02</span>
        <h3>Backend Development</h3>
        <p>Engineering robust backend architectures using Node.js, Next.js, Supabase, PostgreSQL, REST APIs, Authentication, Cloudinary, and Edge Functions. Focused on secure data management, optimized server-side logic, seamless media handling, and scalable infrastructure that powers fast, reliable digital products.</p>
      </div>
      
      <div class="exp-card c3 reveal">
        <span class="pin"></span>
        <span class="num">03</span>
        <h3>AI-Powered Development</h3>
        <p>Leveraging Claude, ChatGPT, GitHub Copilot, Cursor, Codeium, OpenAI, Midjourney, Figma AI, and OpenCode to accelerate ideation, wireframing, UI engineering, debugging, code generation, and creative workflows while maintaining high standards for performance, scalability, and code quality.</p>
      </div>
      
      <div class="exp-card c4 reveal">
        <span class="pin"></span>
        <span class="num">04</span>
        <h3>Quality Assurance &amp; Testing</h3>
        <p>Designing test cases, conducting manual &amp; automated testing using Selenium WebDriver &amp; TestNG, and tracking defects in JIRA to ensure software reliability.</p>
      </div>
      
      <div class="exp-card c5 reveal">
        <span class="pin"></span>
        <span class="num">05</span>
        <h3>Cloud &amp; Deployment</h3>
        <p>Deploying and maintaining modern web applications with Vercel, Cloudflare Workers, GitHub, Supabase, Cloudinary, and custom domains. Focused on fast global delivery, scalable infrastructure, secure hosting, media optimization, and seamless deployment workflows.</p>
      </div>

      <p class="exp-tagline">Turning ideas into reality!</p>
    </div>
  </div>
</section>

<section class="tools" id="tools">"""

html_pattern = re.compile(r'<section class="expertise" id="expertise">.*?</section>.*?<section class="tools" id="tools">', re.DOTALL)
content = html_pattern.sub(new_html, content)

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")
