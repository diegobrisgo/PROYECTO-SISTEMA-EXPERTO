# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:40:51 2024

@author: Efrain Jimenez M
"""

import cv2
import numpy as np
import imutils

image = cv2.imread('f1.png')
columnas = image.shape[1]
filas = image.shape[0]

M = np.float32([[1,0,10],[0,1,100]])
imageOut = cv2.warpAffine(image,M,(columnas,filas))

Mr = cv2.getRotationMatrix2D((columnas//2,filas//2), 30, 1)
imageOutr= cv2.warpAffine(image, Mr, (columnas,filas))

imageSize = imutils.resize(image, width=300)

print('image.shape=',image.shape)
imageOutCut = image[100:300,100:200]

cv2.imwrite('f1_t.png', imageOut)
cv2.imwrite('f1_r.png', imageOutr)
cv2.imwrite('f1_s.png', imageSize)
cv2.imwrite('f1_c.png', imageOutCut)

cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.imshow('Imagen de salida rotada', imageOutr)
cv2.imshow('Imagen de salida tamano', imageSize)
cv2.imshow('Imagen de salida cortada', imageOutCut)
cv2.waitKey(0)
cv2.destroyAllWindows()