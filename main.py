import cv2
import numpy as np
#import matplotlib as plt

#Abrir a imagem - Questão 1
def abrirImagem():
    image = cv2.imread('gundam_woman.jpg')
    cv2.imshow('img', image)
    cv2.waitKey(0)


print(abirImagem())

