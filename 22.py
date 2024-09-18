import tkinter as tk
#Crear la ventana y ponerle titulo
ventana = tk.Tk()
ventana.title ("Mi primera ventana")
#etiquetas
etiqueta = tk.Label(ventana , text= "Hola")
etiqueta.pack()
etiqueta1 = tk.Label(ventana , text= "Mi nombre es Erik")
etiqueta1.pack()
etiqueta2 = tk.Label(ventana , text= "Mi apellido es Requerey")
etiqueta2.pack()
etiqueta3 = tk.Label(ventana , text= "y tengo 14 años")
etiqueta3.pack()

#entrada de texto pequeño
entrada = tk.Entry(ventana)
entrada.pack()

#Entrada de texto grande (height es altura y width es ancho)
texto = tk.Text(ventana , height=5 , width=30)
texto.pack()


#ejecutar la ventana
ventana.mainloop()
