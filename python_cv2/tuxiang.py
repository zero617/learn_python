import cv2
import numpy as np


# from PIL import Image


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img__ = cv2.imread("2.jpg")
img_ = cv2.cvtColor(img__, cv2.COLOR_BGR2RGB)
# img_cp = img_.copy()
cv_show('img', img_)

img_gray = cv2.cvtColor(img_, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(img_gray, 125, 350)
cv_show('img', edges)
cv2.imwrite('heibai.png', edges)

lines = cv2.HoughLinesP(edges,  # 输入图像
                        1,  # 累加器分辨率
                        np.pi / 180,  # 角度分辨率
                        60,  # 确定直线之前收到的最小投票数
                        minLineLength=100,  # 直线的最小长度
                        maxLineGap=20)  # 直线上允许的最大缝隙
line = lines[:, 0, :]
for x1, y1, x2, y2 in line[:]:
    cv2.line(img_,  # 输入图像
             (x1, y1),  # 起点
             (x2, y2),  # 终点
             (255, 0, 0),  # 颜色
             1)  # 宽度
cv_show('img', img_)
cv2.imwrite('nihe.png', img_)


