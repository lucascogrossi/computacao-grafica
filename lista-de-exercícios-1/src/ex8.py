"""
Implemente a equalização de histograma. Utilize-o nas imagens “lena.png”,
“unequalized.jpg” e “img_aluno”.
"""

import cv2
import numpy as np
import os

def equalizacao_histograma(img: np.ndarray) -> np.ndarray:
    hist_ac_norm = histograma_acumulado_normalizado(img)
    s = np.floor(255 * hist_ac_norm).astype('uint8')
    img_eq = s[img]
    return img_eq

def histograma(img: np.ndarray) -> np.ndarray:
    hist = np.zeros(256, dtype=int)
    for i in range(256):
        hist[i] = np.sum(img == i)
    return hist

def histograma_acumulado(img: np.ndarray) -> np.ndarray:
    hist = histograma(img)
    return np.cumsum(hist)

def histograma_acumulado_normalizado(img: np.ndarray) -> np.ndarray:
    hist_acc = histograma_acumulado(img)
    return hist_acc / hist_acc[-1]

def grayscale(img: np.ndarray) -> np.ndarray:
    return ((img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3).astype('uint8')

if __name__ == "__main__":

    # lena.png
    img1 = cv2.imread('../images/lena.png')
    gray1 = grayscale(img1)
    eq1 = equalizacao_histograma(gray1)
    cv2.imshow('Lena - Original vs Equalizado', np.hstack((gray1, eq1)))

    # img_aluno.png
    img2 = cv2.imread('../images/img_aluno.png')
    gray2 = grayscale(img2)
    eq2 = equalizacao_histograma(gray2)
    cv2.imshow('Img Aluno - Original vs Equalizado', np.hstack((gray2, eq2)))

    # unequalized.jpg
    img3 = cv2.imread('../images/unequalized.jpg')
    gray3 = grayscale(img3)
    eq3 = equalizacao_histograma(gray3)
    cv2.imshow('Unequalized - Original vs Equalizado', np.hstack((gray3, eq3)))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
