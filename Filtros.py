# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:05:26 2024

@author: Diego
"""

import cv2
import numpy as np
# Carga una imagen en escala de grises
image =cv2.imread('ajolote.jpg')
isize = cv2.resize(image, (400,300))

kernel = 3
tamano_kernel=3
#-------------------------Ruido Gaussiano----------------------------------


# Especifica la media y la desviación estándar del ruido gaussiano
media = 0
desviacion_estandar = 25

# Genera ruido gaussiano
ruido_gaussiano = np.random.normal(media, desviacion_estandar, isize.shape)

# Añade el ruido a la imagen
RGauss = np.clip(isize + ruido_gaussiano, 0, 255).astype(np.uint8)

# Muestra la imagen original y la imagen con ruido
cv2.imshow('Original', isize)
cv2.imshow('Con Ruido Gaussiano', RGauss)



#--------------------Sal y pimienta-------------------------------

image = cv2.imread('ajolote.jpg')
isize = cv2.resize(image, (400, 300))

# Probabilidad de aparición de ruido
probabilidad_sal = 0.05  # Porcentaje de píxeles blancos
probabilidad_pimienta = 0.05  # Porcentaje de píxeles negros

# Copia de la imagen para aplicar el ruido
RuidoSyP = isize.copy()

# Número total de píxeles de ruido para sal y pimienta
numero_pimienta = int(np.ceil(probabilidad_pimienta * isize.shape[0] * isize.shape[1]))
numero_sal = int(np.ceil(probabilidad_sal * isize.shape[0] * isize.shape[1]))

# Se aplica ruido pimienta (negros)
for i in range(numero_pimienta):
    x = np.random.randint(0, isize.shape[0])
    y = np.random.randint(0, isize.shape[1])
    RuidoSyP[x][y] = 0

# Se aplica ruido sal (blancos)
for i in range(numero_sal):
    x = np.random.randint(0, isize.shape[0])
    y = np.random.randint(0, isize.shape[1])
    RuidoSyP[x][y] = 255

cv2.imshow('Con Ruido Sal y Pimienta', RuidoSyP)


cv2.imwrite('ajoloteO.jpg', isize)
cv2.imwrite('ajoloteGauss.jpg', RGauss)
cv2.imwrite('ajoloteSyP.jpg',RuidoSyP )

imagenGauss =cv2.imread('ajoloteGauss.jpg')
imageSyP = cv2.imread('ajoloteSyP.jpg')
#Filtro Gaussiano
fGauss = cv2.GaussianBlur(imagenGauss,(5,5), 0)
cv2.imshow('Filtro Gaussiano del ruido Gauss', fGauss)
cv2.imwrite('Filtro Gaussiano del ruido Gauss.jpg',fGauss)

fGaussPS =  cv2.GaussianBlur(imageSyP,(5,5), 0)
cv2.imshow('Filtro Gaussiano del ruido Pimienta', fGaussPS)
cv2.imwrite('Filtro Gaussiano del ruido Pimienta.jpg',fGaussPS)
#Filtro mediana
fMediana = cv2.medianBlur(imagenGauss,5)
cv2.imshow('Filtro Mediana del ruido Gauss', fMediana)
cv2.imwrite('Filtro Mediana del ruido Gauss.jpg',fMediana)

fMedianaPS = cv2.medianBlur(imageSyP,5)
cv2.imshow('Filtro Mediana del ruido Pimienta', fMedianaPS)
cv2.imwrite('Filtro Mediana del ruido Pimienta.jpg',fMedianaPS)
#Filtro media

fMedia = cv2.blur(imagenGauss, (kernel, kernel))
cv2.imshow('Filtro Media del ruido Gauss', fMedia)
cv2.imwrite('Filtro Media del ruido Gauss.jpg',fMedia)

fMediaPS = cv2.blur(imageSyP, (kernel, kernel))
cv2.imshow('Filtro Media del ruido Pimienta', fMediaPS)
cv2.imwrite('Filtro Media del ruido Pimienta.jpg',fMediaPS)

#Filtro minimo
kernel1 = np.ones((tamano_kernel, tamano_kernel), np.uint8)

# Aplicar el filtro mínimo usando la función cv2.erode
fMini = cv2.erode(imagenGauss, kernel1)
cv2.imshow('Filtro Minimo del ruido Gauss', fMini)
cv2.imwrite('Filtro Minimo del ruido Gauss.jpg',fMini)

fMiniPS = cv2.erode(imageSyP, kernel1)
cv2.imshow('Filtro Minimo del ruido PIMIENTA', fMiniPS)
cv2.imwrite('Filtro Minimo del ruido PIMIENTA.jpg',fMiniPS)
#FILTRO MINIMO
kernel = np.ones((kernel, kernel), np.uint8)

# Aplicar el filtro máximo utilizando la función cv2.dilate
fMaxi = cv2.dilate(imagenGauss, kernel)
cv2.imshow('Filtro Maxi del ruido Gauss', fMaxi)
cv2.imwrite('Filtro Maxi del ruido Gauss.jpg',fMaxi)

fMaxiPS = cv2.dilate(imageSyP, kernel)
cv2.imshow('Filtro Maxi del ruido PIMIENTA', fMaxiPS)
cv2.imwrite('Filtro Maxi del ruido PIMIENTA.jpg',fMaxiPS)

cv2.waitKey(0)
cv2.destroyAllWindows()
