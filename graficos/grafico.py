from tkinter import *

raiz = Tk()
raiz.title("Ventana de Prueba")
raiz.resizable(1,1)
# raiz.iconbitmap("gato.ico")
raiz.geometry("650x350")
raiz.config(bg="blue")

miFrame = Frame()
miFrame.pack(side="right", anchor="s")
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
raiz.mainloop()