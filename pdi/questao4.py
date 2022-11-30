import cv2
import numpy as np
#import matplotlib as plt

#Abrir imagem e salvar uma nova imagem em tom de cinza - Questao 2
path = '../src/gundam_woman.jpg'
pathToSave = '../src/grayImage.jpg'

def abrirImagem():
    imagem = cv2.imread(path)
    cv2.imshow('Imagem original', imagem)
    convertGray(imagem)
    cv2.waitKey(0)


def convertGray(image):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagem cinza', imageGray)
    #Salvando imagem em tons de cinza
    cv2.imwrite(pathToSave, imageGray)
    cv2.waitKey(0)
    print("Image saved in:", pathToSave)

print(abrirImagem())
