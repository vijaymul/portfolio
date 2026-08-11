import cv2
import numpy as np
from collections import Counter

video_path = r'c:\Users\abhijeett\OneDrive\Desktop\Chai_Aur_Degree.mp4'
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
if ret:
    # Resize for faster processing
    small_frame = cv2.resize(frame, (100, 100))
    # Reshape to a list of pixels
    pixels = small_frame.reshape(-1, 3)
    # Convert pixels to hex strings
    hex_pixels = [f"#{r:02x}{g:02x}{b:02x}" for b, g, r in pixels]
    # Find most common colors
    counts = Counter(hex_pixels)
    print("Most common colors:")
    for color, count in counts.most_common(5):
        print(f"{color}: {count} pixels")
else:
    print("Failed to read video")
cap.release()
