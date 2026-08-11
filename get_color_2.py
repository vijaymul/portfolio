import cv2
import numpy as np

video_path = r'c:\Users\abhijeett\OneDrive\Desktop\Chai_Aur_Degree.mp4'
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
if ret:
    h, w, _ = frame.shape
    print(f"Video resolution: {w}x{h}")
    # Sample from middle edges
    pixels = {
        "mid-top": frame[10, w//2],
        "mid-bottom": frame[-10, w//2],
        "mid-left": frame[h//2, 10],
        "mid-right": frame[h//2, -10],
        "center": frame[h//2, w//2]
    }
    for name, p in pixels.items():
        b, g, r = p
        print(f"{name}: #{r:02x}{g:02x}{b:02x}")
else:
    print("Failed to read video")
cap.release()
