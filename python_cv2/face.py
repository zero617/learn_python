# 人脸识别（图片、摄像头）
import cv2
# import numpy as np


# 图片中人脸识别
def Face_Detect_Pic(image):

    # 中值滤波
    image = cv2.medianBlur(image, 5)

    # 1、转灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # cv2.imshow("gray", gray)

    # 2、训练一组人脸
    face_detector = cv2.CascadeClassifier(
        "D:/code/learn_python/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")

    # 3、检测人脸（用灰度图检测，返回人脸矩形坐标(4个角)）
    faces_rect = face_detector.detectMultiScale(gray, 1.05, 3)
    #                                          灰度图  图像尺寸缩小比例  至少检测次数（若为3，表示一个目标至少检测到3次才是真正目标）
    # print("人脸矩形坐标faces_rect：", faces_rect)

    # 4、遍历每个人脸，画出矩形框
    dst = image.copy()
    for x, y, w, h in faces_rect:
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 3)  # 画出矩形框

    # 显示
    cv2.imshow("dst", dst)
    # imgs = np.hstack([img, dst])
    # cv2.imshow("result", imgs)

    return dst


# 摄像头中人脸识别
def Face_Detect_Cam():
    # 打开摄像头
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0：本地摄像头    1：外接摄像头

    while True:
        # 1、按帧读取视频
        ret, frame = capture.read()  # frame为每一帧的图像

        # 2、左右翻转（否则向左右移动的时候，对象右左移动，反着移）
        frame = cv2.flip(frame, 1)

        # 3、对每一帧图像人脸识别
        result = Face_Detect_Pic(frame)

        # q键退出（设置读帧间隔时间）
        if cv2.waitKey(1) & 0XFF == ord("q"):
            break


if __name__ == "__main__":
    # 读取图片
    # img = cv2.imread("xg.jpg")
    # img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
    # Face_Detect_Pic(img)  # 人脸识别（图片）

    # 人脸识别（视频）
    Face_Detect_Cam()

    cv2.waitKey(0)
