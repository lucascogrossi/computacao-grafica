"""
Implemente o operador logarítmico e utilize-o nas imagens “lena.png” e “img_aluno”.
"""

import cv2
import numpy as np

def logaritmico(img: np.ndarray, c: float = 1.0) -> np.ndarray:
    img_log = c * np.log1p(img.astype(np.float64))
    img_log = normalizacao(img_log)
    return img_log.astype(np.uint8)

def normalizacao(img: np.ndarray, c: int = 0, d: int = 255) -> np.ndarray:
    a = img.min()
    b = img.max()
    normalizado = ((img - a) * ((d - c) / (b - a)) + c).astype(np.uint8)
    return normalizado

if __name__ == "__main__":
    img1 = cv2.imread('../images/lena.png')
    img2 = cv2.imread('../images/img_aluno.png')

    log1 = logaritmico(img1)
    log2 = logaritmico(img2)

    cv2.imshow("lena_log", log1)
    cv2.imshow("img_aluno_log", log2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

