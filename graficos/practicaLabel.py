from tkinter import *

#nuestra raiz
root = Tk()

#creamos un frame, se especifica el contenedor padre, en este caso root que es la raiz
miFrame = Frame(root, width=800, height=800)
miFrame.pack()
miImage = PhotoImage(file=r"C:\Users\Reptiliano\Documents\GitHub\CursoPython\graficos\PXAH.gif")
# miLabel = Label(miFrame, text="Hello work")
# miLabel.place(x=100, y=100)
#es lo mismo que el codigo de las dos lineas superiores ⬆️⬆️⬆️
# Label(miFrame, text="Hello work", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=100)
Label(miFrame, image=miImage).place(x=10, y=10)

#png y gif por defecto de lo contrario se necesita importar paquetes para eso
root.mainloop()

