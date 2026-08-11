import re

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add cursor: pointer to reel-toggle
content = content.replace(".reel-toggle{", ".reel-toggle{\n      cursor:pointer;")

# 2. Replace placeholder with video
old_photo = """<div class="hero-photo">
        <div class="hero-photo-placeholder">
          [ Place your cutout portrait image here ]
        </div>
      </div>"""
new_photo = """<div class="hero-photo">
        <video id="heroVideo" src="Chai_Aur_Degree.mp4" autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: contain; mix-blend-mode: normal;"></video>
      </div>"""
# In case whitespace doesn't match perfectly:
if old_photo in content:
    content = content.replace(old_photo, new_photo)
else:
    content = re.sub(r'<div class="hero-photo">.*?</div>\s*</div>', new_photo + '\n    </div>', content, flags=re.DOTALL)

# 3. Add JavaScript for mute/unmute
js_addition = """
  // Video Mute/Unmute Logic
  const reelToggle = document.querySelector('.reel-toggle');
  const heroVideo = document.getElementById('heroVideo');
  if(reelToggle && heroVideo) {
    reelToggle.addEventListener('click', () => {
      heroVideo.muted = !heroVideo.muted;
      if(heroVideo.muted) {
        reelToggle.innerHTML = '<div class="circ"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg></div>UNMUTE REEL';
      } else {
        reelToggle.innerHTML = '<div class="circ"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg></div>MUTE REEL';
      }
    });
  }
"""
content = content.replace('// Preloader logic', js_addition + '\n  // Preloader logic')

with open("c:/Users/abhijeett/OneDrive/Desktop/portfolio.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Video and mute logic added successfully")
