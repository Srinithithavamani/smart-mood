import cv2
from emotion_detector import predict_emotion_from_image

img_path = r"D:\Aitech-django\smartmoods\smartapp\ai\test\happy\PrivateTest_95094.jpg"

img = cv2.imread(img_path)

print("Image loaded:", img is not None)

if img is None:
    print("Image not found:", img_path)
else:
    cv2.imshow("Test Image", img)
    cv2.waitKey(2000)

    mood, conf = predict_emotion_from_image(img)
    print("Detected mood:", mood, "confidence:", conf)
