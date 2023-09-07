import cv2
print("Imported")


img = cv2.imread("Image/h.jpg")

cv2.imshow("Output",img)
cv2.waitKey(1000)