import cv2 as cv 

def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1]*scale)
    height = int(frame.shape[0]* scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions , interpolation = cv.INTER_AREA)

Capture=cv.VideoCapture('Vid/v1.mp4')

while True:
    isTrue , frame = Capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('video', frame)
    cv.imshow("Resized Vide", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()

cv.waitKey(0)