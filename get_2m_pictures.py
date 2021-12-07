# -*- coding: utf-8 -*-
"""


@author: 张理官
"""
import cv2
import numpy as np
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
i=0
while True:
    ret,frame = cap1.read()#左边
    ret2,frame2 = cap2.read()#右边
#    for i in range(0,479):
#        for j in range(0,int(639/2)):
#            frame[i,j] = frame[i][j]+frame[i][639-j]
#            frame[i][639-j] = frame[i,j] - frame[i][639-j]
#            frame[i][j] = frame[i,j] - frame[i][639-j]
    k=cv2.waitKey(1)
    if k==27:
        break
    elif k==ord('s'):
        cv2.imwrite('D:/biyesheji/2m/left_pictures/'+'left_'+str(i)+'.jpg',frame)
        cv2.imwrite('D:/biyesheji/2m/right_pictures/'+'right_'+str(i)+'.jpg',frame2)
        i+=1
    cv2.imshow('zuo',frame)
    cv2.imshow('you',frame2)
    if cv2.waitKey(1)&0xFF ==ord('q'):
        break
cap1.release()
cap2.release()
cv2.destoryAllWindows()