import tkinter as tk
ventana=tk.Tk()
ventana.title("area")
ventana.geometry("2900x1500")
letrero=tk.Label(ventana, text="Bienvenido", font=("Times New Roman", 40))
letrero.pack(pady=100)

ventana.mainloop()
