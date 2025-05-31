import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
ventana=tk.Tk()
ventana.title("inicio")
ventana.geometry("1024x640")
ventana.config(bg="gray")
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40)).pack(pady=20)

class registrar:
    def __init__(self, nombre, apellido1, apellido2, curp, sexo, edad, telefono, cargo):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.curp = curp
        self.sexo = sexo
        self.edad = edad
        self.telefono = telefono
        self.cargo = cargo
    def datos(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2} a sido registrado exitosamente"

def registrar_usuario():
 nombre = en_nombre.get()
 apellido1 = en_apellido1.get()
 apellido2 = en_apellido2.get()
 curp = en_curp.get()
 sexo = en_sexo.get()
 edad = en_edad.get()
 telefono = en_telefono.get()
 cargo = en_cargo.get()

 registro = registrar(nombre, apellido1, apellido2, curp, sexo, edad, telefono, cargo)
 mensaje = registro.datos()
 messagebox.showinfo("Datos Registrados", mensaje)

def mostrar_formulario(event):
    seleccion = combo.get()
    if seleccion == "Registrarse":

     tk.Label(ventana,text="Nombre: ", font=("Calibri", 10), bg="gray").pack(pady=0)
     global en_nombre
     en_nombre=tk.Entry(ventana, font=("Calibri", 10))
     en_nombre.pack(pady=8)

     tk.Label(ventana, text="Apellido paterno: ", font=("Calibri", 10), bg="gray").pack()
     global en_apellido1
     en_apellido1=tk.Entry(ventana, font=("Calibri", 10))
     en_apellido1.pack(pady=8)

     tk.Label(ventana, text="Apellido materno: ", font=("Calibri", 10), bg="gray").pack()
     global en_apellido2
     en_apellido2=tk.Entry(ventana, font=("Calibri", 10))
     en_apellido2.pack(pady=8)

     tk.Label(ventana, text="CURP: ",font=("Calibri", 10), bg="gray").pack()
     global en_curp
     en_curp=tk.Entry(ventana, show="*", font=("Calibri", 10))
     en_curp.pack(pady=8)

     valor=tk.StringVar()
     global en_sexo
     en_sexo=tk.OptionMenu(ventana, valor, "masculino", "femenino", "otro").pack

     tk.Label(ventana, text="Edad: ",font=("Calibri", 10), bg="gray").pack()
     global en_edad
     en_edad=tk.Entry(ventana, font=("Calibri", 10))
     en_edad.pack(pady=8)

     tk.Label(ventana, text="Telefono: ",font=("Calibri", 10), bg="gray").pack()
     global en_telefono
     en_telefono=tk.Entry(ventana, show="*", font=("Calibri", 10))
     en_telefono.pack(pady=8)

     tk.Label(ventana, text="Cargo: ",font=("Calibri", 10), bg="gray").pack()
     global en_cargo
     en_cargo=tk.Entry(ventana, show="*", font=("Calibri", 10))
     en_cargo.pack(pady=8)

     boton_registrar = tk.Button(ventana, text="Registrar", command=registrar_usuario)
     boton_registrar.pack(pady=10)

tk.Label(ventana, text="¿Que quieres hacer?", bg="gray", font=("Calibri", 20)).pack(pady=5)
combo = ttk.Combobox(ventana, values=["Registrarse", "Agendar cita", "ingresar (acceso solo a personal)"], font=("Calibri, 15"))
combo.pack(pady=5)
combo.current(0)

formulario_frame = tk.Frame(ventana, bg="gray")
formulario_frame.pack(pady=20)

combo.bind("<<ComboboxSelected>>", mostrar_formulario)


ventana.mainloop()

