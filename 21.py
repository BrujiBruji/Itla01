import tkinter as tk
# Funcion para mostrar el saludo
def saludar():
    nombre = entrada.get()
    saludo.config(text="Hola, " + nombre + "!")
#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo Personalizado")
#Etiqueta para pedir el nombre
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()
#Cuadro de entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()
#Boton para saludar
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()
#Etiqueta para mostrar el saludo
saludo = tk.Label(ventana, text="")
saludo.pack()
#Iniciar el bucle principal de la aplicacion
ventana.mainloop()