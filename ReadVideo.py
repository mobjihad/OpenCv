import cv2


cap = cv2.VideoCapture("Vid/v1.mp4")

while True:
    success, image = cap.read()
    cv2.imshow("Video",image)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break