# -*- coding:utf-8 -*-'
import cv2

img = cv2.imread("11.jpg")
#cv2.imshow('gray',img)
cv2.namedWindow('color',cv2.WINDOW_NORMAL)
cv2.imshow("color",img)
cv2.imwrite("saveimg.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()