import cv2

video_path = r'c:\Users\abhijeett\OneDrive\Desktop\Chai_Aur_Degree.mp4'
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
if ret:
    cv2.imwrite(r'c:\Users\abhijeett\OneDrive\Desktop\MY resume\frame.png', frame)
    print("Saved frame.png")
else:
    print("Failed to read video")
cap.release()
