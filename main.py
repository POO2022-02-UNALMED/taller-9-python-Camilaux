from tkinter import END, Tk, Button, Entry
# Configuración ventana principal

root = Tk()
root.title('Calculadora POO')
root.resizable(0,0)
root.geometry("330x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=20, padx=1, pady=1)

#Funciones

def mostrarPantalla(texto):
    pantalla.insert(END,texto)

def operar():
    ecuacion = pantalla.get()
    for e in ecuacion:
        if e == "+":
            antes=ecuacion.split(e)[0]
            despues = ecuacion.split(e)[1]
            resultado = sumar(antes,despues)
        elif e == "-":
            antes=ecuacion.split(e)[0]
            if antes != None:
                resultado = eval(ecuacion)
            else:
                continue
        elif e == "*":
            antes=ecuacion.split(e)[0]
            despues = ecuacion.split(e)[1]
            resultado = multiplicar(antes,despues)
        elif e == "/":
            antes=ecuacion.split(e)[0]
            despues = ecuacion.split(e)[1]
            resultado = dividir(antes,despues)
    pantalla.delete(0,END)
    pantalla.insert(0,resultado)

def sumar(x,y):
    return float(x)+float(y)

def multiplicar(x,y):
    return float(x)*float(y)

def dividir(x,y):
    return float(x)/float(y)

# Configuración botones
boton_1 = Button(root, text="1", command= lambda: mostrarPantalla(1),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command= lambda:mostrarPantalla(2),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command= lambda:mostrarPantalla(3),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", command= lambda:mostrarPantalla(4),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", command= lambda:mostrarPantalla(5),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", command= lambda:mostrarPantalla(6),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", command= lambda:mostrarPantalla(7),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", command= lambda:mostrarPantalla(8),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", command= lambda:mostrarPantalla(9),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", command= operar,width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)  #duda con ese columnspan
boton_punto = Button(root, text=".", command= lambda:mostrarPantalla("."),width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", command= lambda:mostrarPantalla("+"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", command= lambda:mostrarPantalla("-"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", command= lambda:mostrarPantalla("*"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", command= lambda:mostrarPantalla("/"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()