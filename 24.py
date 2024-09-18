import tkinter as tk
def addNumber
ventana = tk.Tk()
ventana.title ("Calculadora")

ventana = tk.Tk()
entryNumero1 = tk.Entry(ventana)
entryNumero1.grid(row=0 , column=0)
tk.Button(ventana , text="1", width=5).grid(row=1 , column = 0)
tk.Button(ventana , text="2", width=5).grid(row=1 , column = 1)
tk.Button(ventana , text="3", width=5).grid(row=1 , column = 2)

tk.Button(ventana , text="4", width=5).grid(row=2 , column = 0)
tk.Button(ventana , text="5", width=5).grid(row=2 , column = 1)
tk.Button(ventana , text="6", width=5).grid(row=2 , column = 2)

tk.Button(ventana , text="7", width=5).grid(row=3 , column = 0)
tk.Button(ventana , text="8", width=5).grid(row=3 , column = 1)
tk.Button(ventana , text="9", width=5).grid(row=3 , column = 2)







ventana.mainloop()