import cv2

def thresh(img, th=128):
    img[img < th] = 0
    img[img >= th] = 255
    return img

img = cv2.imread("../img/imori.jpg",0)
#dst =cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1]
dst = thresh(img)
cv2.imshow("3",dst)
cv2.waitKey()