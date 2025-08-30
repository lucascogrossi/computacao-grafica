"""
Implemente o algoritmo de conversão para níveis de cinza e utilize-o nas imagens
“lena.png” e “img_aluno”.
"""

import cv2
import numpy as np

def grayscale(img: np.ndarray) -> np.ndarray:
    c = img[:, :, 0]/ 3 + img[:, :, 1]/ 3 + img[:, :, 2]/ 3
    c = c.astype('uint8')
    return c

if __name__ == "__main__":
    img1 = cv2.imread('../images/lena.png')
    img2 = cv2.imread('../images/img_aluno.png')

    cv2.imshow("lena", img1)
    cv2.imshow("img_aluno", img2)

    gray1 = grayscale(img1)
    gray2 = grayscale(img2)

    cv2.imshow("lena_gray", gray1)
    cv2.imshow("img_aluno_gray", gray2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

