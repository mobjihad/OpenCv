import cv2 as cv
import numpy as np

Blank = np.zeros((700,700,3),dtype='uint8')
cv.rectangle(Blank,(0,0),(700,300),(0,255,0),thickness=-1)
cv.circle(Blank, (350,150),60,(0,0,255),thickness=-1)
cv.imshow('Blank',Blank)
cv.waitKey(0)


