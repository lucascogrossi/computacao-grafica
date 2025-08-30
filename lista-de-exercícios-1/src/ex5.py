"""
Implemente o operador de potência e utilize-o nas imagens “lena.png” e “img_aluno”.
"""

import cv2
import numpy as np

def potencia(img: np.ndarray, c: float = 1.0, gamma: float = 1.0) -> np.ndarray:
    img_pow = c * np.power(img.astype(np.float64), gamma)
    img_pow = normalizacao(img_pow)
    return img_pow.astype(np.uint8)

def normalizacao(img: np.ndarray, c: int = 0, d: int = 255) -> np.ndarray:
    a = img.min()
    b = img.max()
    normalizado = ((img - a) * ((d - c) / (b - a)) + c).astype(np.uint8)
    return normalizado

if __name__ == "__main__":
    img1 = cv2.imread('../images/lena.png')
    img2 = cv2.imread('../images/img_aluno.png')

    cv2.imshow("lena", img1)
    cv2.imshow("img_aluno", img2)

    pot1 = potencia(img1, 2, 2)
    pot2 = potencia(img2, 2, 2)

    cv2.imshow("lena_pot", pot1)
    cv2.imshow("img_aluno_pot", pot2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

