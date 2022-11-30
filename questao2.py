import cv2
import numpy as np
#import matplotlib as plt

#Abrir imagem e salvar uma nova imagem em tom de cinza - Questao 2
path = './gundam_woman.jpg'

def abrirImagem():
    imagem = cv2.imread(path)
    cv2.imshow('img', imagem)
    convertGray(imagem)
    cv2.waitKey(0)


def convertGray(image):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagem cinza', imageGray)
    #Salvando imagem em tons de cinza
    cv2.imwrite('./grayImage.jpg', imageGray)
    cv2.waitKey(0)

print(abrirImagem())
