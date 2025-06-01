import tkinter as tk
import csv
from tkinter import messagebox
from tkinter import ttk
ventana=tk.Tk()
ventana.title("inicio")
ventana.geometry("1024x640")
ventana.config(bg="gray")
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40), bg="gray").pack(pady=20)

class afiliacion:
   def __init__(self, nombre, apellido1, apellido2, curp, correo, domicilio, telefono):
      self.nombre=nombre
      self.apellido1=apellido1
      self.apellido2=apellido2
      self.curp=curp
      self.correo=correo
      self.domicilio=domicilio
      self.telefono=telefono
   def afiliacion_exitosa(self):
      return f"has sido afiliado exitosamente"
   def num(self):
      identificador=format(id(afiliacion), "x")
      return f"tu numero de afiliacion es: {identificador}"
def afiliarse():
   try:
      nombre= en_nombre.get()
      apellido1=en_apellido1.get()
      apellido2=en_apellido2.get()
      curp=en_curp.get()
      correo=en_correo.get()
      domicilio=en_domicilio.get()
      telefono=en_telefono.get()
      if not all([nombre,apellido1,apellido2,curp,correo,domicilio,telefono]):
         raise ValueError("Todos los campos son obligatorios")
      afiliado=afiliacion(nombre,apellido1,apellido2,curp,correo,domicilio,telefono)
      mensaje=afiliado.afiliacion_exitosa()
      folio=afiliado.num()
      messagebox.showinfo("Afilicion exitosa", f"{mensaje}\n, {folio}")
   except ValueError as e:
      messagebox.showwarning("error", str(e))

class cita:
   def __init__(self, nombre, apellido1, apellido2, correo, telefono, especialidad):
      self.nombre=nombre
      self.apellido1=apellido1
      self.apellido2=apellido2
      self.correo=correo
      self.telefono=telefono
      self.especialidad=especialidad
   def consulta(self):
      return f"{self.nombre}, {self.apellido1}, {self.apellido2}, ha agendado una cita con un {self.especialidad}"
   
def agendar():
 try:
     nombre = en_nombre.get()
     apellido1 = en_apellido1.get()
     apellido2 = en_apellido2.get()
     curp = en_curp.get()
     correo = en_correo.get()
     telefono = en_telefono.get()
     especialidad = en_especialidad.get()
     if not all([nombre, apellido1,apellido2,curp,correo,telefono,especialidad]):
        raise ValueError("Todos los campos son obligatorios")
     
     cita_medica = cita(nombre, apellido1, apellido2, correo, telefono, especialidad)
     mnsj = cita_medica.consulta()
     messagebox.showinfo("cita agendada", mnsj)

     with open("citas_agendadas.csv", "a", newline="", encoding="utf-8") as archivo:
         writer = csv.writer(archivo)
         writer.writerow([nombre, apellido1, apellido2, curp, correo, telefono, especialidad])

 except ValueError as e:
    messagebox.showwarning("error", "todos los campos son obligatorios")


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
 try:
     nombre = en_nombre.get()
     apellido1 = en_apellido1.get()
     apellido2 = en_apellido2.get()
     curp = en_curp.get()
     sexo = valor.get()
     edad = en_edad.get()
     telefono = en_telefono.get()
     cargo = en_cargo.get()
     if not all([nombre, apellido1, apellido2, curp, sexo, edad, telefono, cargo]):
        raise ValueError("Todos los campos son obligatorios")
     registro = registrar(nombre, apellido1, apellido2, curp, sexo, edad, telefono, cargo)
     mensaje = registro.datos()
     messagebox.showinfo("Datos Registrados", mensaje)

     with open("usuarios_registrados.csv", "a", newline="", encoding="utf-8") as archivo:
         writer = csv.writer(archivo)
         writer.writerow([nombre, apellido1, apellido2, curp, sexo, edad, telefono, cargo])


 except ValueError as e:
    messagebox.showwarning("error", "no se pudo completar el registro, porfavor intente de nuevo")

class Usuario:
   def __init__(self, usuario="admin", contraseña="1234"):
      self.usuario=usuario
      self.contraseña=contraseña
   def verificar(self, usuario, contraseña):
      return self.usuario==usuario and self.contraseña==contraseña

def mostrar_formulario(event):
    seleccion = combo.get()
    for widget in formulario_frame.winfo_children():
     widget.destroy()

    global en_nombre, en_apellido1, en_apellido2, en_curp, en_telefono, en_correo, en_especialidad
    global en_sexo, valor, en_edad, en_cargo, en_domicilio

    if seleccion == "Registrarse":

     tk.Label(formulario_frame,text="Nombre: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_nombre=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_nombre.grid(row=0, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido paterno: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido1=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_apellido1.grid(row=1, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido materno: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido2=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_apellido2.grid(row=2, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="CURP: ",font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_curp=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_curp.grid(row=3, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Sexo:", bg="gray").grid(pady=10, padx=10, sticky="e")
     valor = tk.StringVar()
     valor.set("Seleccionar")
     en_sexo = tk.OptionMenu(formulario_frame, valor, "Masculino", "Femenino", "Otro")
     en_sexo.grid(row=4, column=1, padx=10, pady=10)
     
     tk.Label(formulario_frame, text="Edad: ",font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_edad=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_edad.grid(row=5, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Telefono: ",font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_telefono=tk.Entry(formulario_frame, show="*", font=("Calibri", 10))
     en_telefono.grid(row=6, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Cargo: ",font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_cargo=tk.Entry(formulario_frame, show="*", font=("Calibri", 10))
     en_cargo.grid(row=7, column=1, padx=10, pady=10)

     boton_registrar = tk.Button(formulario_frame, text="Registrar", command=registrar_usuario)
     boton_registrar.grid(row=8, column=1, padx=10, pady=10)

    elif seleccion == "Agendar cita":
     tk.Label(formulario_frame,text="Nombre: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_nombre=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_nombre.grid(row=0, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido paterno: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido1=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_apellido1.grid(row=1, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido materno: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido2=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_apellido2.grid(row=2, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="CURP: ",font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_curp=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_curp.grid(row=3, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text=" Numero telefonico:", font=("calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_telefono=tk.Entry(formulario_frame, font=("calibri", 10))
     en_telefono.grid(row=4, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Correo electronico:", font=("calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_correo=tk.Entry(formulario_frame, font=("calibri", 10))
     en_correo.grid(row=5, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text=" Ingrese el espacialista a consultar: ", font=("calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_especialidad=tk.Entry(formulario_frame, font=("calibri", 10))
     en_especialidad.grid(row=6, column=1, padx=10, pady=10)

     tk.Button(formulario_frame, text="Agendar Cita", command=agendar).grid(row=8, column=1, pady=10, padx=10)

    elif seleccion == "Afiliarse":
     tk.Label(formulario_frame,text="Nombre: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_nombre=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_nombre.grid(row=0, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido paterno: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido1=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_apellido1.grid(row=1, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido materno: ", font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido2=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_apellido2.grid(row=2, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="CURP: ",font=("Calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_curp=tk.Entry(formulario_frame, font=("Calibri", 10))
     en_curp.grid(row=3, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Correo electronico:", font=("calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_correo=tk.Entry(formulario_frame, font=("calibri", 10))
     en_correo.grid(row=4, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Domicilio:", font=("calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_domicilio=tk.Entry(formulario_frame, font=("calibri", 10))
     en_domicilio.grid(row=5, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text=" Numero telefonico:", font=("calibri", 10), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_telefono=tk.Entry(formulario_frame, font=("calibri", 10))
     en_telefono.grid(row=6, column=1, padx=10, pady=10)

     tk.Button(formulario_frame, text="Siguiente", command=afiliarse).grid(row=7, column=1, pady=10, padx=10)

    elif seleccion == "Ingresar (acceso solo a personal)":
        tk.Label(formulario_frame, text="Usuario:", bg="gray").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        en_usuario = tk.Entry(formulario_frame, font=("Calibri", 10))
        en_usuario.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(formulario_frame, text="Contraseña:", bg="gray").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        en_contraseña = tk.Entry(formulario_frame, show="*", font=("Calibri", 10))
        en_contraseña.grid(row=1, column=1, padx=10, pady=10)

        def verificar_acceso():
            usuario_ingresado = en_usuario.get()
            contraseña_ingresada = en_contraseña.get()
            admin = Usuario()
            if admin.verificar(usuario_ingresado, contraseña_ingresada):
                messagebox.showinfo("Acceso permitido", "Bienvenido al sistema")
                abrir_ventana_personal()
            else:
                messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

        tk.Button(formulario_frame, text="Ingresar", command=verificar_acceso).grid(row=2, column=1, pady=10)

     
def abrir_ventana_personal():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Panel del Personal")
    nueva_ventana.geometry("400x300")
    nueva_ventana.config(bg="lightblue")
    tk.Label(nueva_ventana, text="Bienvenido al área del personal", font=("Calibri", 15), bg="lightblue").pack(pady=20)
    

tk.Label(ventana, text="¿Que quieres hacer?", bg="gray", font=("Calibri", 20)).pack(pady=5)
combo = ttk.Combobox(ventana, values=["Registrarse", "Agendar cita", "Afiliarse", "Ingresar (acceso solo a personal)"], font=("Calibri, 15"))
combo.pack(pady=5)
combo.current(0)

formulario_frame = tk.Frame(ventana, bg="gray")
formulario_frame.pack(pady=20)

combo.bind("<<ComboboxSelected>>", mostrar_formulario)

ventana.mainloop()
