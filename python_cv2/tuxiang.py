import cv2
import numpy as np
from PIL import Image

raw_ = cv2.imread("2.jpg")
raw = cv2.cvtColor(raw_, cv2.COLOR_BGR2RGB)
raw_cp = raw.copy()
raw_gray = cv2.cvtColor(raw, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(raw_gray, 125, 350)
image1 = Image.fromarray(raw.astype('uint8')).convert('RGB')
cv2.imshow('image1', img)
cv2.waitkey(0)
# image1.show()
image2 = Image.fromarray(edges.astype('uint8')).convert('RGB')
# image2.show()
image2.save("heibai.png")
lines = cv2.HoughLinesP(edges,  # 输入图像
                        1,  # 累加器分辨率
                        np.pi / 180,  # 角度分辨率
                        60,  # 确定直线之前收到的最小投票数
                        minLineLength=100,  # 直线的最小长度
                        maxLineGap=20)  # 直线上允许的最大缝隙
line = lines[:, 0, :]
for x1, y1, x2, y2 in line[:]:
    cv2.line(raw,  # 输入图像
             (x1, y1),  # 起点
             (x2, y2),  # 终点
             (255, 0, 0),  # 颜色
             1)  # 宽度
image1 = Image.fromarray(raw.astype('uint8')).convert('RGB')
# image1.show()
image1.save("nihe.png")

'''
# 在黑色图像上画一条白线，
# 并且穿过用于检测直线的 Canny 轮廓图。结果是包含了与指定直线相关点的图像
one_line = np.zeros(raw.shape, dtype=np.uint8)
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
image5 = Image.fromarray(raw_cp.astype('uint8')).convert('RGB')
image5.show()
'''
