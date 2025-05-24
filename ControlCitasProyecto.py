import tkinter as tk
ventana=tk.Tk()
ventana.title("area")
ventana.geometry("2900x1500")
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40))
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40), bg="gray")
letrero.pack(pady=60)
letrero.pack(pady=100)
def usuario():
    global nombre, apellido1, apellido2, contraseña
    nombre=entrada1.get()
    apellido1=entrada2.get()
    apellido2=entrada3.get()
    contraseña=entrada4.get()

etiqueta=tk.Label(ventana,text="Nombre: ", font=("Calibri", 20), bg="gray", width=10,)
etiqueta.pack(pady=0)
entrada1=tk.Entry(ventana, width=50, font=("Calibri", 15))
entrada1.pack(pady=8)

entiqueta1=tk.Label(ventana, text="Apellido paterno: ", font=("Calibri", 20), bg="gray", width=50)
entiqueta1.pack()
entrada2=tk.Entry(ventana, width=50, font=("Calibri", 15))
entrada2.pack(pady=8)

etiqueta2=tk.Label(ventana, text="Apellido materno: ", font=("Calibri", 20), bg="gray", width=50)
etiqueta2.pack()
entrada3=tk.Entry(ventana, width=50, font=("Calibri", 15))
entrada3.pack(pady=8)

etiqueta3=tk.Label(ventana, text="Contraseña: ",font=("Calibri", 20), bg="gray", width=50)
etiqueta3.pack()
entrada4=tk.Entry(ventana, width=30, font=("Calibri", 15))
entrada4.pack(pady=8)

ventana.mainloop()
