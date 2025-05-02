# 🖼️ Ecualización de Histograma con Tkinter y OpenCV

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0%2B-green?logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-informational)](https://www.python.org/downloads/)
[![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)](https://github.com/tuusuario)

Este proyecto permite cargar una imagen desde una interfaz gráfica, visualizar su histograma antes y después de aplicar ecualización de histograma, y mostrar los valores de frecuencia e intensidad. Combina el poder de **OpenCV**, **Matplotlib** y **Tkinter**.

## 📷 Características

- Carga de imágenes con explorador de archivos
- Conversión automática a escala de grises
- Ecualización de histograma (`cv2.equalizeHist`)
- Visualización en tiempo real de:
  - Imagen original y ecualizada
  - Histograma antes y después
- Cálculo e impresión de frecuencias e intensidades

## 🚀 Requisitos

- Python 3.8 o superior
- OpenCV
- NumPy
- Matplotlib
- Tkinter (incluido con Python por defecto)

### Instalación de dependencias

```bash
pip install opencv-python numpy matplotlib
