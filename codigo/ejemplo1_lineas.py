# Meredith Aguirre NC = 0013

import cv2
import numpy as np

# Cargar imagen
imagen = cv2.imread("imagenes/tigrejaz.jpg")

# Verificar que la imagen exista
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes
bordes = cv2.Canny(gris, 50, 150)

# Detectar líneas mediante Hough
lineas = cv2.HoughLinesP(
    bordes,
    1,
    np.pi / 180,
    threshold=100,
    minLineLength=100,
    maxLineGap=10
)

# Crear copia de la imagen
resultado = imagen.copy()

# Dibujar líneas
if lineas is not None:

    for linea in lineas:
        x1, y1, x2, y2 = linea.ravel()

        cv2.line(
            resultado,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            2
        )

# Mostrar resultados
cv2.imshow("Imagen original", imagen)
cv2.imshow("Bordes", bordes)
cv2.imshow("Lineas detectadas", resultado)

# Guardar resultado
cv2.imwrite(
    "resultados/tigrejaz_lineas2.jpg",
    resultado
)

print("Deteccion de lineas terminada.")

if lineas is not None:
    print("Cantidad de segmentos detectados:", len(lineas))
else:
    print("No se detectaron lineas.")

print("Resultado guardado en:")
print("resultados/tigrejaz_lineas2.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()