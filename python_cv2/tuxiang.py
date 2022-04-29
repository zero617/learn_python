import cv2
import numpy as np


# from PIL import Image


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img__ = cv2.imread("2.jpg")
img_ = cv2.cvtColor(img__, cv2.COLOR_BGR2RGB)
img_cp = img_.copy()
img_gray = cv2.cvtColor(img_, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(img_gray, 125, 350)
cv_show('img', img_)
# image2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, image2 = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY)#
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

'''
# 在黑色图像上画一条白线，
# 并且穿过用于检测直线的 Canny 轮廓图。结果是包含了与指定直线相关点的图像
one_line = np.zeros(img.shape, dtype=np.uint8)
cv2.line(one_line, (line[0][0], line[0][1]), (line[0][2], line[0][3]), (255, 255, 255), 3)
# 拆分单通道
B, G, R = cv2.split(one_line)
image4 = Image.fromarray(one_line.astype('uint8')).convert('RGB')
image4.show()
# 和Canny检测结果做“与”运算
bitwise_and = cv2.bitwise_and(edges, B)
image5 = Image.fromarray(bitwise_and.astype('uint8')).convert('RGB')
image5.show()

points = []
for i in range(bitwise_and.shape[0]):
    for j in range(bitwise_and.shape[1]):
        if bitwise_and[i][j] != 0:
            points.append((i, j))
# 拟合直线
points = np.asarray(points)
output = cv2.fitLine(points,  # 输入点集 矩阵形式
                     cv2.DIST_L2,  # 欧式距离，此时与最小二乘法相同
                     0,  # 距离参数，跟所选类型有关系
                     0.01,  # 径向精度
                     0.01)  # 角度精度
# 这个fitLine拟合的有点问题 暂时还没找到原因
image5 = Image.fromarray(img_cp.astype('uint8')).convert('RGB')
image5.show()
'''
