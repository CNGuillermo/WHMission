import random
import tkinter as tk
from tkinter import PhotoImage

# Listas de elementos (en este caso, nombres de imágenes)
primaryMission = ['PM1.png', 'PM2.png', 'PM3.png', 'PM4.png', 'PM5.png', 'PM6.png', 'PM7.png', 'PM8.png', 'PM9.png', 'PM10.png']
missionRule = ['MR1.png', 'MR2.png', 'MR3.png', 'MR4.png']
deployment = ['D1.png', 'D2.png', 'D3.png', 'D4.png', 'D5.png']

# Selecciona un elemento al azar de cada lista
elemento_elegido_primaryMission = random.choice(primaryMission)
elemento_elegido_missionRule = random.choice(missionRule)
elemento_elegido_deployment = random.choice(deployment)

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.withdraw()  # Oculta la ventana principal

# Carga las imágenes correspondientes a los elementos elegidos
imagen1 = PhotoImage(file=elemento_elegido_primaryMission)
imagen2 = PhotoImage(file=elemento_elegido_missionRule)
imagen3 = PhotoImage(file=elemento_elegido_deployment)

# Muestra las imágenes en una ventana emergente
ventana_emergente = tk.Toplevel(ventana_principal)
ventana_emergente.title("Esta es tu misión, baboso!")

# Crea un lienzo (Canvas) para mostrar las imágenes en línea
canvas = tk.Canvas(ventana_emergente)
canvas.pack()

# Muestra las imágenes en el lienzo
canvas.create_image(0, 0, anchor=tk.NW, image=imagen1)
canvas.create_image(imagen1.width(), 0, anchor=tk.NW, image=imagen2)
canvas.create_image(2 * imagen1.width(), 0, anchor=tk.NW, image=imagen3)

# Ajusta el tamaño del lienzo según el ancho total de las imágenes
canvas.config(width=3 * imagen1.width(), height=imagen1.height())

# Cierra la ventana principal al cerrar la ventana emergente
ventana_emergente.protocol("WM_DELETE_WINDOW", ventana_principal.destroy)

# Inicia el bucle principal de la ventana
ventana_principal.mainloop()
