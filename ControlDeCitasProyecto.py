import tkinter as tk
ventana=tk.Tk()
ventana.title("area")
ventana.geometry("400x300")

etiqueta=tk.Label(ventana, text="ingresa el radio del circulo")
etiqueta.pack()
entrada=tk.Entry(ventana)
radio=(entrada.get())
entrada.pack()

area=(3.14*(radio*radio))
boton=tk.Button(ventana, text="resultado",)
boton.pack()
etiqueta2=tk.Label(ventana, text=f"el area es {area}")
etiqueta2.pack()


ventana.mainloop()
