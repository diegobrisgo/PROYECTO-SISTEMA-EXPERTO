# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:37:14 2024

@author: Efrain Jimenez M
"""

import cv2
import numpy as np
cap=cv2.VideoCapture(0)

imagen=cv2.imread("ladrillos.jpg",0)
Kernel=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
m,n=imagen.shape
filtrada=np.zeros_like(imagen)

for x in range(m-2):
    for y in range(n-2):
        res=np.sum(imagen[x:x+3,y:y+3]*Kernel)
        if abs(res)>50:
            filtrada[x,y]=255
        

cv2.imshow("Ori",imagen)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("filtrada",filtrada)
cv2.imwrite("filtrada.jpg",filtrada)
cv2.waitKey()
cv2.destroyAllWindows()