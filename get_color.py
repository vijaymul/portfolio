import cv2

video_path = r'c:\Users\abhijeett\OneDrive\Desktop\Chai_Aur_Degree.mp4'
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
if ret:
    # Assuming top-left pixel is background color
    b, g, r = frame[0, 0]
    print(f"Top-left pixel: #{r:02x}{g:02x}{b:02x}")
    # Also get bottom-left
    b, g, r = frame[-1, 0]
    print(f"Bottom-left pixel: #{r:02x}{g:02x}{b:02x}")
    # Also get top-right
    b, g, r = frame[0, -1]
    print(f"Top-right pixel: #{r:02x}{g:02x}{b:02x}")
else:
    print("Failed to read video")
cap.release()
