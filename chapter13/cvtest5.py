# -*- coding:utf-8 -*-'
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

img1 = cv2.imread('33.png')
img = cv2.resize(img1,(240,320),interpolation=cv2.INTER_LINEAR)

faces = face_cascade.detectMultiScale(img,1.2,2)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,x+h),(255,0,0),2)#用颜色为BGR（255,0,0）粗度为2的线条在img画出识别出的矩型
    face_re = img[y:y+h,x:x+w]#抽取出框出的脸部部分，注意顺序y在前
    eyes = eye_cascade.detectMultiScale(face_re)#在框出的脸部部分识别眼睛
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(face_re,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
key = cv2.waitKey(0)
if key==27:
    cv2.destoryWindow('img')