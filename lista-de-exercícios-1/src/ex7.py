import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Cria pasta para salvar os histogramas
os.makedirs("../output_histogramas", exist_ok=True)

def grayscale(img: np.ndarray) -> np.ndarray:
    return (img[:, :, 0]/3 + img[:, :, 1]/3 + img[:, :, 2]/3).astype('uint8')

def histograma(img: np.ndarray) -> np.ndarray:
    hist = np.zeros(256, dtype=int)
    for i in range(256):
        hist[i] = np.sum(img == i)
    return hist

def histograma_normalizado(img: np.ndarray) -> np.ndarray:
    hist = histograma(img)
    return hist / img.size

def histograma_acumulado(img: np.ndarray) -> np.ndarray:
    hist = histograma(img)
    return np.cumsum(hist)

def histograma_acumulado_normalizado(img: np.ndarray) -> np.ndarray:
    hist_acc = histograma_acumulado(img)
    return hist_acc / hist_acc[-1]

def salvar_histogramas(img_gray, filename_prefix="histograma"):
    hist = histograma(img_gray)
    hist_norm = histograma_normalizado(img_gray)
    hist_acc = histograma_acumulado(img_gray)
    hist_acc_norm = histograma_acumulado_normalizado(img_gray)

    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.title("Histograma")
    plt.bar(range(256), hist, color='gray')

    plt.subplot(2, 2, 2)
    plt.title("Histograma Normalizado")
    plt.bar(range(256), hist_norm, color='gray')

    plt.subplot(2, 2, 3)
    plt.title("Histograma Acumulado")
    plt.bar(range(256), hist_acc, color='gray')

    plt.subplot(2, 2, 4)
    plt.title("Histograma Acumulado Normalizado")
    plt.bar(range(256), hist_acc_norm, color='gray')

    plt.tight_layout()
    plt.savefig(f"../output_histogramas/{filename_prefix}.png")
    plt.close()

if __name__ == "__main__":
    # (i)
    img_unequalized = cv2.imread('../images/unequalized.jpg')
    img_unequalized_gray = grayscale(img_unequalized)
    salvar_histogramas(img_unequalized_gray, "hist_unequalized_gray")

    # (ii)
    img_aluno = cv2.imread('../images/img_aluno.png')
    canais = ['B', 'G', 'R']
    for i, cor in enumerate(canais):
        hist = histograma(img_aluno[:, :, i])
        plt.figure(figsize=(6, 4))
        plt.title(f"Histograma Canal {cor}")
        plt.bar(range(256), hist, color=cor.lower())
        plt.tight_layout()
        plt.savefig(f"../output_histogramas/hist_canal_{cor}.png")
        plt.close()

    # (iii)
    img_aluno_gray = grayscale(img_aluno)
    salvar_histogramas(img_aluno_gray, "hist_img_aluno_gray")
