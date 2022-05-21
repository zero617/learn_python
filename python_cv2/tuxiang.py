import cv2
import numpy as np


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 图片道路识别
def race_detect_pic(img):

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(img_gray, 125, 350)
    # cv_show('img', edges)
    # cv2.imwrite('gray.png', edges)

    lines = cv2.HoughLinesP(edges,  # 输入图像
                            1,  # 累加器分辨率
                            np.pi / 180,  # 角度分辨率
                            150,  # 确定直线之前收到的最小投票数
                            minLineLength=100,  # 直线的最小长度
                            maxLineGap=30)  # 直线上允许的最大缝隙
    line = lines[:, 0, :]
    for x1, y1, x2, y2 in line[:]:
        cv2.line(img,  # 输入图像
                 (x1, y1),  # 起点
                 (x2, y2),  # 终点
                 (0, 0, 255),  # 颜色
                 3)  # 宽度
    return img
    # cv_show('img', img)
    # cv2.imwrite('nihe.png', img_)


# 模拟摄像头道路识别
def race_detect_vid():
    vc = cv2.VideoCapture('video2.mp4')

    # 检查是否打开正确
    if vc.isOpened():
        open, frame = vc.read()
    else:
        open = False

    while open:
        ret, frame = vc.read()
        if frame is None:
            break
        if ret:
            result = race_detect_pic(frame)
            cv2.imshow('result', result)
            if cv2.waitKey(100) & 0xFF == 27:
                break
    vc.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # img = cv2.imread("2.jpg")
    race_detect_vid()

    cv2.waitKey()
