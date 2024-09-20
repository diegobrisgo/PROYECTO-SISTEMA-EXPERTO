# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 01:01:08 2024

@author: Efrain Jimenez M
"""

import cv2
import numpy as np

img1=np.zeros((400,600),dtype=np.uint8)
img1[100:300,200:400]=255
img2=np.zeros((400,600),dtype=np.uint8)
img2=cv2.circle(img2, (300,200), 125, (255),-1)

#AND
AND = cv2.bitwise_and(img1, img2)
cv2.imshow('AND', AND)
#OR
OR = cv2.bitwise_or(img1, img2)
cv2.imshow('OR',OR)
#NOT
NOT = cv2.bitwise_not(img1)
cv2.imshow('NOT', NOT)
#XOR
XOR = cv2.bitwise_xor(img1, img2)
cv2.imshow('XOR', XOR)

cv2.imwrite('img1.jpg', img1)
cv2.imwrite('img2.jpg', img2)
cv2.imwrite('and.jpg', AND)
cv2.imwrite('OR.jpg', OR)
cv2.imwrite('NOT.jpg', NOT)
cv2.imwrite('XOR.jpg', XOR)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()