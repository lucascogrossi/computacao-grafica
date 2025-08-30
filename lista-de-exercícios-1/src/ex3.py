"""
Implemente o ajuste de contraste (normalização) e utilize-o nas imagens “lena.png” e
“img_aluno”.
"""

import cv2
import numpy as np

def normalizacao(img: np.ndarray, c: int = 0, d: int = 255) -> np.ndarray:
    a = img.min()
    b = img.max()
    normalizado = ((img - a) * ((d - c) / (b - a)) + c).astype(np.uint8)
    return normalizado

if __name__ == "__main__":
    img1 = cv2.imread('../images/lena.png')
    img2 = cv2.imread('../images/img_aluno.png')

    normalizacao1 = normalizacao(img1, 0, 100)
    normalizacao2 = normalizacao(img2, 0, 100)

    cv2.imshow("lena_normalizacao", normalizacao1)
    cv2.imshow("img_aluno_normalizacao", normalizacao2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

