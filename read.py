import cv2 as cv

# img=cv.imread('Image/h.jpg')
# cv.imshow('Cat', img)
Capture=cv.VideoCapture('Vid/v1.mp4')

while True:
    isTrue , frame = Capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()

cv.waitKey(0)


    
