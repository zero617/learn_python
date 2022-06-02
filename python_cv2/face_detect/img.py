import sys

import cv2
import numpy as np


# 图片中人脸识别
def Face_Detect_Pic(image):
    # 中值滤波
    image_MF = cv2.medianBlur(image, 5)

    # 1、转灰度图
    gray = cv2.cvtColor(image_MF, cv2.COLOR_RGB2GRAY)
    gray = cv2.equalizeHist(gray)

    # 2、训练一组人脸
    face_detector = cv2.CascadeClassifier(
        "D:/code/learn_python/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")

    # 3、检测人脸（用灰度图检测，返回人脸矩形坐标(4个角)）
    faces_rect = face_detector.detectMultiScale(gray, 1.1, 3)
    # 灰度图  图像尺寸缩小比例  表示构成检测目标的相邻矩形的最小个数 (默认为 3 个)
    # print("人脸矩形坐标faces_rect：", faces_rect)

    # 4、遍历每个人脸，画出矩形框
    dst = image.copy()
    for x, y, w, h in faces_rect:
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 3)  # 画出矩形框
        cv2.putText(dst, "face", (x + 7, y - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

    # 显示
    result = np.hstack([img, dst])
    cv2.imshow("result", result)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img = cv2.imread("th.jpg")
    Face_Detect_Pic(img)
    sys.exit(1)
