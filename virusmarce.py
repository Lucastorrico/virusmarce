import tkinter as tk
import pyautogui 
import time
import winsound
# Crear ventana
root = tk.Tk()
root.overrideredirect(True)       # Quita bordes
root.wm_attributes("-topmost", True)  # Siempre encima
root.config(bg="black")

# Cargar imagen (usa PNG con transparencia si querés)
imagen = tk.PhotoImage(file="marce.png")
label = tk.Label(root, image=imagen, bg="black")
label.pack()

# Posición inicial de la ventana
x_ventana, y_ventana = 100, 100

   
def seguir_mouse():
    global x_ventana, y_ventana
    
    # Posición actual del mouse
    x_mouse, y_mouse = pyautogui.position()

    # Calcular movimiento suave (interpolación)
    velocidad = 0.1  # cuanto más chico, más lento persigue
    x_ventana += (x_mouse - x_ventana) * velocidad
    y_ventana += (y_mouse - y_ventana) * velocidad

    # Mover ventana
    root.geometry(f"+{int(x_ventana)}+{int(y_ventana)}")

    # Repetir
    root.after(10, seguir_mouse)
def musica():
 winsound.PlaySound("SE-ESCUCHA-LENTOOOO___.WAV", winsound.SND_ASYNC)
# Arrancar después de 1s
def accion_click(event):
   musica()
label.bind("<Button-1>", accion_click)
time.sleep(1)
seguir_mouse()

root.mainloop()
