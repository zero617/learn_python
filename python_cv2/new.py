import cv2

img = cv2.imread('1.png', 1)
cv2.imshow('imshow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
