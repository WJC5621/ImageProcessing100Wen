#读取图像，然后将$\text{RGB}$通道替换成$\text{BGR}$通道
import cv2
import sys
import numpy as np
img = cv2.imread("../img/imori.jpg")
cv2.imshow("imori",img)
red = img[:,:,2]
img[:,:,2] = img[:,:,0]
img[:,:,0] = red
cv2.imshow("answer_1.jpg",img)
cv2.imwrite("../answers_image/answer_1.jpg",img)
cv2.waitKey()