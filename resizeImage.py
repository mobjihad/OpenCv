import cv2 as cv

def reScaleImg(frame, scale = 0.7):

    Width = int(frame.shape[1]*scale)
    Height= int(frame.shape[0]*scale)

    dimension = (Width,Height)

    return cv.resize(frame, dimension , interpolation =cv.INTER_AREA)


img = cv.imread("Image/h.jpg")

Resized_Image = reScaleImg(img)

cv.imshow("Normal Image",img)
cv.imshow("Resized Image",Resized_Image)

cv.waitKey(0)

        