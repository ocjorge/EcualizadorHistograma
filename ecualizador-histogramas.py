import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog

def calcular_e_imprimir_frecuencias(imagen, tipo):
    """Calcula e imprime las frecuencias (histograma) de una imagen"""
    # Calcula el histograma de la imagen
    hist = cv2.calcHist([imagen], [0], None, [256], [0, 256])
    
    # Normaliza el histograma
    hist_normalizado = hist / float(imagen.size)
    
    print(f"\n----- Frecuencias {tipo} -----")
    for i in range(256):
        if hist[i][0] > 0:  # Solo imprime valores de frecuencia mayores que cero
            print(f"Intensidad {i}: Frecuencia = {int(hist[i][0])}, Frecuencia Normalizada = {hist_normalizado[i][0]:.6f}")

def seleccionar_imagen():
    # Abre el explorador de archivos para seleccionar una imagen
    ruta_imagen = filedialog.askopenfilename(
        title="Seleccionar Imagen",
        filetypes=(("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp"), ("Todos los archivos", "*.*"))
    )
    
    if ruta_imagen:
        # Lee la imagen seleccionada
        imagen = cv2.imread(ruta_imagen)
        if imagen is None:
            print("Error al cargar la imagen")
            return
        
        # Convierte la imagen a escala de grises (la ecualización requiere una imagen en escala de grises)
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        
        # Ecualiza la imagen usando cv2.equalizeHist()
        imagen_ecualizada = cv2.equalizeHist(gray)
        
        # Calcula e imprime las frecuencias para las imágenes original y ecualizada
        calcular_e_imprimir_frecuencias(gray, "Originales")
        calcular_e_imprimir_frecuencias(imagen_ecualizada, "Ecualizadas")
        
        # Convierte las imágenes BGR a RGB para visualizarlas con matplotlib
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
        # Crea una figura con 2 filas y 2 columnas de subplots
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        
        # Muestra la imagen original
        axs[0, 0].imshow(gray, cmap='gray')
        axs[0, 0].set_title('Imagen Original')
        axs[0, 0].axis('off')
        
        # Muestra el histograma original
        hist_original = cv2.calcHist([gray], [0], None, [256], [0, 256])
        axs[0, 1].bar(range(256), hist_original.ravel(), width=1, color='gray')
        axs[0, 1].set_title('Histograma Original')
        axs[0, 1].set_xlim([0, 256])
        
        # Muestra la imagen ecualizada
        axs[1, 0].imshow(imagen_ecualizada, cmap='gray')
        axs[1, 0].set_title('Imagen Ecualizada')
        axs[1, 0].axis('off')
        
        # Muestra el histograma ecualizado
        hist_ecualizado = cv2.calcHist([imagen_ecualizada], [0], None, [256], [0, 256])
        axs[1, 1].bar(range(256), hist_ecualizado.ravel(), width=1, color='gray')
        axs[1, 1].set_title('Histograma Ecualizado')
        axs[1, 1].set_xlim([0, 256])
        
        # Ajusta el espaciado entre subplots
        plt.tight_layout()
        
        # Crea una ventana de Tkinter
        ventana = tk.Toplevel(root)
        ventana.title("Imagen Original vs. Ecualizada")
        
        # Integra la figura de matplotlib en la ventana de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Crea la ventana principal de Tkinter
root = tk.Tk()
root.title("Seleccionar Imagen para Ecualización")
root.geometry("300x100")

# Botón para seleccionar una imagen
btn_seleccionar = tk.Button(root, text="Seleccionar Imagen", command=seleccionar_imagen)
btn_seleccionar.pack(pady=20)

# Inicia el bucle principal de la interfaz
root.mainloop()
