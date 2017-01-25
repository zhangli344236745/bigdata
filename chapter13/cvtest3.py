# -*- coding:utf-8 -*-'
import cv2

def main():
    org = cv2.imread("11.jpg")
    cv2.imshow("image",org)
    cv2.waitKey(0)
    roi = org[20:,100:]
    cv2.imshow("roi",roi)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()