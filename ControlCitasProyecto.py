import tkinter as tk
ventana=tk.Tk()
ventana.title("inicio")
ventana.geometry("2900x1500")
ventana.config(bg="gray")
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40))
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40), bg="gray")
letrero.pack(pady=60)
letrero.pack(pady=100)

def ventana2():
 ventana2=tk.Tk()
 ventana2.title("hola")
 ventana2.geometry("900x900")
 ventana2.config(bg="gray")

etiqueta=tk.Label(ventana,text="Nombre: ", font=("Calibri", 20), bg="gray", width=10,)
etiqueta.pack(pady=0)
entrada1=tk.Entry(ventana, width=50, font=("Calibri", 15))
entrada1.pack(pady=8)

entiqueta1=tk.Label(ventana, text="Apellido paterno: ", font=("Calibri", 20), bg="gray")
entiqueta1.pack()
entrada2=tk.Entry(ventana, font=("Calibri", 15))
entrada2.pack(pady=8)

etiqueta2=tk.Label(ventana, text="Apellido materno: ", font=("Calibri", 20), bg="gray")
etiqueta2.pack()
entrada3=tk.Entry(ventana, font=("Calibri", 15))
entrada3.pack(pady=8)

etiqueta3=tk.Label(ventana, text="Contraseña: ",font=("Calibri", 20), bg="gray")
etiqueta3.pack()
entrada4=tk.Entry(ventana, font=("Calibri", 15))
entrada4.pack(pady=8)

boton=tk.Button(ventana, text="Siguiente", font=("Calibri", 15), command=ventana2)
boton.pack(pady=8)

ventana.mainloop()
