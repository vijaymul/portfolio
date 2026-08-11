import cv2
import numpy as np

img = cv2.imread(r'c:\Users\abhijeett\OneDrive\Desktop\MY resume\hero_image.png')
# Get a few pixels from the top background
pixels = [
    img[10, 10], img[10, img.shape[1]//2], img[10, -10]
]
for p in pixels:
    b, g, r = p
    print(f"#{r:02x}{g:02x}{b:02x}")
