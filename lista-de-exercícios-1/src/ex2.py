"""
Implemente o algoritmo que gera o negativo e utilize-o nas imagens “lena.png” e
“img_aluno”
"""

import cv2
import numpy as np

def negativo(img: np.ndarray) -> np.ndarray:
    return 255 - img

if __name__ == "__main__":
    img1 = cv2.imread('../images/lena.png')
    img2 = cv2.imread('../images/img_aluno.png')

    cv2.imshow("lena", img1)
    cv2.imshow("img_aluno", img2)

    negativo1 = negativo(img1)
    negativo2 = negativo(img2)

    cv2.imshow("lena_negativo", negativo1)
    cv2.imshow("img_aluno_negativo", negativo2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

