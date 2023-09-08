import cv2 as cv
import numpy as np

blank = np.zeros((800,800,3), dtype='uint8')

cv.imshow("Blank",blank)

cv.waitKey(0)

#painting a Certian Area
blank[300:400,700:800] = 0,255,0
cv.imshow("Blank 2 ",blank)
cv.waitKey(0)


#draw a rectanle 
blank2 = np.zeros((800,800,3), dtype='uint8')
cv.rectangle(blank2,(0,0),(250,250),(0,255,0),thickness=-1)
cv.imshow("rectangle",blank2)
cv.waitKey(0)

#draw Circle

blank3 = np.zeros((800,800,3), dtype='uint8')

cv.circle(blank3,(blank3.shape[0]//2,blank3.shape[1]//2),30,(0,0,255),thickness=-1)
cv.imshow('Circle',blank3)
cv.waitKey(0)