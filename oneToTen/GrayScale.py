import cv2
import numpy as np

def grayscale(img):
    rows,cols,ch = img.shape
    for i in range(rows):
        for j in range(cols):
            b = img.item(i, j, 0)
            g = img.item(i, j, 1)
            r = img.item(i, j, 2)
            img.itemset((i,j,0),0.2126*r+0.7152*g+0.0722*b)
            img.itemset((i,j,1),0.2126*r+0.7152*g+0.0722*b)
            img.itemset((i,j,2),0.2126*r+0.7152*g+0.0722*b)

def BGR2GRAY(img):
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]
    return 0.2126*r+0.7152*g+0.0722*b



img = cv2.imread("../img/imori.jpg")
#grayscale(img)
img = BGR2GRAY(img)
cv2.imshow("2",img.astype(np.uint8))
cv2.imwrite("../answers_image/answer_2.jpg",img)
cv2.waitKey()
