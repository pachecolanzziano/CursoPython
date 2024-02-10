#tenemos varias opciones para posicion relleno bordes y tamaños etc de la raiz o de los frame
from tkinter import *
# configuracion de la razi
raiz = Tk()
raiz.title("Ventana de Prueba")
raiz.resizable(1,1)
# raiz.iconbitmap("gato.ico")
raiz.geometry("650x350")
raiz.config(bg="blue")

# configuracion de frame
miFrame = Frame()
miFrame.pack(side="top", anchor="n")
miFrame.pack(fill="y", expand="True")

miFrame.config(bg="red")
miFrame.config(width="650", height="350")


raiz.mainloop()