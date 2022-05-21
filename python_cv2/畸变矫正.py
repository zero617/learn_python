"""畸变矫正"""

import cv2
import numpy as np

K = np.zeros((3, 3))
K[0, 0] = 1201.58
K[1, 1] = 1201.72
K[0, 2] = 1019.59
K[1, 2] = 807.568
K[2, 2] = 1

distCoeffs = np.float32([-0.0911113, 0.0852054, 1.79509e-06, 0.000242446])

img = cv2.imread('wq.jpg')
img_undistored = cv2.undistort(img, K, distCoeffs)

# out = cv2.undistort(img, mtx, dist, None, mtx)
cv2.imshow("1", img_undistored)
cv2.waitKey()