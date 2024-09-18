import tkinter as tk
def sumar():
    num1 = float(entryNumero1.get())
    num2 = float(entryNumero2.get())
    calculo = num1 + num2
    lblTotalResult.config(text=calculo)

ventana = tk.Tk()
ventana.title ("Calculadora")
lblNumero1 = tk.Label(ventana , text= "Dame el primer numero")
lblNumero1.pack()

entryNumero1 = tk.Entry(ventana)
entryNumero1.pack()

lblNumero2 = tk.Label(ventana , text= "Dame el segundo numero numero")
lblNumero2.pack()

entryNumero2 = tk.Entry(ventana)
entryNumero2.pack()

tk.Button(ventana, text= "Sumar", command=sumar).pack()

lblResult = tk.Label(ventana , text="Resultado:").pack()
lblTotalResult = tk.Label(ventana , text="0")
lblTotalResult.pack()


ventana.mainloop()