from matplotlib import pyplot as plt
import numpy as np
import cv2

#Definindo caminhos e propriedades da imagem
path = '../src/graos.jpg'
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equal_img = cv2.equalizeHist(img)
    
def histogramaEEqualizacao():
    plt.figure()
    plt.title("Histograma Original")
    plt.xlabel("Intensidade")
    plt.ylabel("Qtde de Pixels")
    plt.hist(img.ravel(), 256, [0,256])
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)
    plt.figure()
    plt.title("Histograma Equalizado")
    plt.xlabel("Intensidade")
    plt.ylabel("Qtde de Pixels")
    plt.hist(equal_img.ravel(), 256, [0,256])
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)

print(histogramaEEqualizacao())
