import tkinter as tk
import csv
from tkinter import messagebox
from tkinter import ttk
ventana=tk.Tk()
ventana.title("inicio")
ventana.geometry("660x640")
ventana.config(bg="gray")
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40), bg="gray").pack(pady=8)
valor=tk.StringVar()
valor.set("Elige una opcion")

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
     correo = en_correo.get()
     telefono = en_telefono.get()
     especialidad = en_especialidad.get()
     if not all([nombre, apellido1,apellido2,correo,telefono,especialidad]):
        raise ValueError("Todos los campos son obligatorios")
     
     cita_medica = cita(nombre, apellido1, apellido2, correo, telefono, especialidad)
     mnsj = cita_medica.consulta()
     messagebox.showinfo("cita agendada", mnsj)

     with open("citas_agendadas.csv", "a", newline="", encoding="utf-8") as archivo:
         writer = csv.writer(archivo)
         writer.writerow([nombre, apellido1, apellido2, correo, telefono, especialidad])

 except ValueError as e:
    messagebox.showwarning("error", "todos los campos son obligatorios")

def mostrar_citas(ventana_ns):
   frame_tabla=tk.Frame(ventana_ns)
   frame_tabla.pack(pady=10, padx=10, fill="both", expand=True)
   columnas=("Nombre", "Apellido Paterno", "Apellido materno", "Correo", "Telefono", "Especialista a consultar")
   tree=ttk.Treeview(frame_tabla, columns=columnas, show="headings")
   tree.pack(fill="both", expand=True)
   for col in columnas:
      tree.heading(col, text=col)
      tree.column(col, anchor="center", width=150)
   try:
      with open("citas_agendadas.csv","r", encoding="utf-8")as archivo:
         reader=csv.reader(archivo)
         for fila in reader:
            tree.insert("","end", values=fila)
   except FileNotFoundError:
      messagebox.showwarning("Error", "No hay citas agendadas o no existe el archivo")

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

    if seleccion == "Agendar cita":
     tk.Label(formulario_frame,text="Nombre: ", font=("Calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_nombre=tk.Entry(formulario_frame, font=("Calibri", 12))
     en_nombre.grid(row=0, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido paterno: ", font=("Calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido1=tk.Entry(formulario_frame, font=("Calibri", 12))
     en_apellido1.grid(row=1, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido materno: ", font=("Calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido2=tk.Entry(formulario_frame, font=("Calibri", 12))
     en_apellido2.grid(row=2, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text=" Numero telefonico:", font=("calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_telefono=tk.Entry(formulario_frame, font=("calibri", 12))
     en_telefono.grid(row=4, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Correo electronico:", font=("calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_correo=tk.Entry(formulario_frame, font=("calibri", 12))
     en_correo.grid(row=5, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text=" Ingrese el espacialista a consultar: ", font=("calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_especialidad=tk.Entry(formulario_frame, font=("calibri", 12))
     en_especialidad.grid(row=6, column=1, padx=10, pady=10)

     tk.Button(formulario_frame, text="Agendar Cita", command=agendar).grid(row=8, column=1, pady=10, padx=10)

    elif seleccion == "Afiliarse":
     tk.Label(formulario_frame,text="Nombre: ", font=("Calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_nombre=tk.Entry(formulario_frame, font=("Calibri", 12))
     en_nombre.grid(row=0, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido paterno: ", font=("Calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido1=tk.Entry(formulario_frame, font=("Calibri", 12))
     en_apellido1.grid(row=1, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Apellido materno: ", font=("Calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_apellido2=tk.Entry(formulario_frame, font=("Calibri", 12))
     en_apellido2.grid(row=2, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="CURP: ",font=("Calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_curp=tk.Entry(formulario_frame, font=("Calibri", 12))
     en_curp.grid(row=3, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Correo electronico:", font=("calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_correo=tk.Entry(formulario_frame, font=("calibri", 12))
     en_correo.grid(row=4, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text="Domicilio:", font=("calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_domicilio=tk.Entry(formulario_frame, font=("calibri", 12))
     en_domicilio.grid(row=5, column=1, padx=10, pady=10)

     tk.Label(formulario_frame, text=" Numero telefonico:", font=("calibri", 13), bg="gray").grid(pady=10, padx=10, sticky="e")
     en_telefono=tk.Entry(formulario_frame, font=("calibri", 12))
     en_telefono.grid(row=6, column=1, padx=10, pady=10)

     tk.Button(formulario_frame, text="Siguiente", command=afiliarse).grid(row=7, column=1, pady=10, padx=10)

    elif seleccion == "Ingresar (acceso solo a personal)":

        frame = tk.Frame(formulario_frame, bg="lightgray", bd=4, relief="groove")
        frame.pack(pady=10, padx=10)
        valor = tk.StringVar()
        valor.set("Elige una opcion")
        tk.Label(frame, text="¿Quien esta ingresando?", bg="lightgray", font=("calibri", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.OptionMenu(frame, valor, "Medico o enfermero(a)", "Administracion", "Recursos humanos", "Archivos").grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Usuario:", bg="lightgray", font=("calibri", 13)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        en_usuario = tk.Entry(frame, font=("Calibri", 12))
        en_usuario.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frame, text="Contraseña:", bg="lightgray", font=("calibri", 13)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        en_contraseña = tk.Entry(frame, show="*", font=("Calibri", 12))
        en_contraseña.grid(row=2, column=1, padx=10, pady=10)

        def verificar_acceso():
            usuario_ingresado = en_usuario.get()
            contraseña_ingresada = en_contraseña.get()
            admin = Usuario()
            if admin.verificar(usuario_ingresado, contraseña_ingresada):
                perfil=valor.get()
                if perfil=="Medico o enfermero(a)":
                   ventana_medicos()
                elif perfil=="Administracion":
                   ventana_administracion()
                elif perfil=="Recursos humanos":
                   ventana_rh()
                elif perfil=="Archivos":
                   ventana_archivos()
                else:
                   messagebox.showwarning("Error de seleccion", "Por favor, seleccione un perfil pra ingresar")
            else:
                messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

        tk.Button(frame, text="Ingresar", command=verificar_acceso).grid(row=3, column=0, pady=10, padx=10, columnspan=3)
    
def ventana_medicos():
    ventana2 = tk.Toplevel(ventana)
    ventana2.title("Personal")
    ventana2.geometry("550x300")
    ventana2.config(bg="lightblue")
    info_frame = tk.Frame(ventana2, bg="lightgray", bd=4, relief="groove")
    info_frame.pack(pady=20, padx=20)
    tk.Button(info_frame, text="Ver expedientes").grid(row=0, column=0, padx=10, pady=10)
    tk.Button(info_frame, text="Citas agendadas", command=lambda:mostrar_citas(ventana2)).grid(row=0, column=1, padx=10, pady=10)

def ventana_administracion():
   ventana3=tk.Toplevel(ventana)
   ventana3.title("Administracion")
   ventana3.geometry("500x400")
   ventana3.config(bg="lightyellow")
   frame1=tk.Frame(ventana3, bg="lightgray", bd=4, relief="groove")
   frame1.pack(padx=10, pady=10,)
   tk.Button(frame1, text="Ver", ).grid(row=0, column=0, padx=10, pady=10)

def ventana_rh():
   ventana4=tk.Toplevel(ventana)
   ventana4.title("Recursos Humanos")
   ventana4.geometry("500x400")
   ventana4.config(bg="lightyellow")
   frame2=tk.Frame(ventana4, bg="lightgray", bd=4, relief="groove")
   frame2.pack(padx=20,pady=20)
   tk.Button(frame2, text="Registro de personal").grid(row=0, column=0, padx=10, pady=10)
   tk.Button(frame2, text="Base de datos Personal").grid(row=0, column=1, padx=10, pady=10)

def ventana_archivos():
   ventana5=tk.Toplevel(ventana)
   ventana5.title("Archivos")
   ventana5.geometry("500x400")
   ventana5.config(bg="lightyellow")
   frame3=tk.Frame(ventana5, bg="lightgray", bd=4, relief="groove")
   frame3.pack(padx=20, pady=20)
   tk.Button(frame3, text="")


tk.Label(ventana, text="¿Que quieres hacer?", bg="gray", font=("Calibri", 20)).pack(pady=5)
combo = ttk.Combobox(ventana, values=["Agendar cita", "Afiliarse", "Ingresar (acceso solo a personal)"], font=("Calibri, 13"))
combo.pack(pady=5)
combo.current(0)

formulario_frame = tk.Frame(ventana, bg="gray")
formulario_frame.pack(pady=20)

combo.bind("<<ComboboxSelected>>", mostrar_formulario)

ventana.mainloop()
