import cv2
import numpy as np

def fatiamento(img: np.ndarray) -> list[np.ndarray]:
    planos = []
    for i in range(8):
        plano = (img >> i) & 1
        plano = (plano * 255).astype(np.uint8)
        planos.append(plano)
    return planos

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

    planos1 = fatiamento(gray1)
    planos2 = fatiamento(gray2)

    for i, plano in enumerate(planos1):
        cv2.imshow(f"lena_fatiamento_{i}", plano)

    for i, plano in enumerate(planos2):
        cv2.imshow(f"img_aluno_fatiamento_{i}", plano)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

