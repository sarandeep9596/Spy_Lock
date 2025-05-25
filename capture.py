import cv2
import time
from send_email import send_email
CAMERA_INDEX = 0  # Default camera index
# Function to capture a photo from the webcam
sender_email = "sarandeepsingh9596@gmail.com"
sender_password = "vceh lcvv sipf okfr"
recipient_email = "sarandeepsingh9596@gmail.com"
subject = "Unauthorized Access Alert"
body = "Someone tried to access your computer without permission. A photo has been captured."



def capture_photo():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("❌ Unable to access the camera")
        return False
    ret, frame = cap.read()
    if ret:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        photo_path = f"unauthorized_{timestamp}.jpg"
        cv2.imwrite(photo_path, frame)
        print(f"✅ Photo saved to {photo_path}")
        
        send_email(sender_email, sender_password, recipient_email, subject, body, photo_path)
    cap.release()
    return ret
