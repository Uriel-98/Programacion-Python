
import tkinter
from turtle import back

lista_botones = [[1,2,3, "Borrar"],[4,5,6,"/"],
              [7,8,9,'*',],[".",0,"-","+"]] 
tipo_numero = 0

def suma(n1, n2):
    resultado = n1 + n2

    label_numeros.config(text=resultado)

def resta(n1, n2):
    resultado = n1 - n2

    label_numeros.config(text=resultado)

def division(n1, n2):
    resultado = n1 / n2

    label_numeros.config(text=resultado)

def multiplicacion(n1, n2):
    resultado = n1 * n2

    label_numeros.config(text=resultado)


def boton_tocado(tipo_boton = -1):
    global num_1
    global num_2
    global operacion
    global tipo_numero

    if tipo_boton == 0 or tipo_boton == 1 or tipo_boton == 2 or tipo_boton == 3 or tipo_boton == 4 or tipo_boton == 5 or tipo_boton == 6 or tipo_boton == 7 or tipo_boton == 8 or tipo_boton == 9:
        if label_numeros.cget("text") == "-" or label_numeros.cget("text") == "+" or label_numeros.cget("text") == "/" or label_numeros.cget("text") == "*":
            label_numeros.config(text=tipo_boton)
        else:
            label_numeros.config(text=f"{label_numeros.cget('text')}{tipo_boton}")

    elif tipo_boton == ".":
        tipo_numero = "float"
        label_numeros.config(text=f"{label_numeros.cget('text')}{tipo_boton}")

    elif tipo_boton == "+":
        operacion = "suma"
        if label_numeros.cget("text") == "-":
            pass
        else:
            if tipo_numero == "float":
                num_1= float(label_numeros.cget("text"))
            else:
                num_1= int(label_numeros.cget("text"))
            label_numeros.config(text="+")
            label_numeros.config(text=tipo_boton)
    
    elif tipo_boton == "-":
        operacion = "resta"
        if label_numeros.cget("text") == "-":
            pass
        else:
            if tipo_numero == "float":
                num_1= float(label_numeros.cget("text"))
            else:
                num_1= int(label_numeros.cget("text"))
            label_numeros.config(text="-")
            label_numeros.config(text=tipo_boton)
    
    elif tipo_boton == "/":
        operacion = "division"
        if label_numeros.cget("text") == "/":
            pass
        else:
            if tipo_numero == "float":
                num_1= float(label_numeros.cget("text"))
            else:
                num_1= int(label_numeros.cget("text"))
            label_numeros.config(text="/")
            label_numeros.config(text=tipo_boton)

    elif tipo_boton == "*":
        operacion = "multiplicacion"
        if label_numeros.cget("text") == "*":
            pass
        else:
            if tipo_numero == "float":
                num_1= float(label_numeros.cget("text"))
            else:
                num_1= int(label_numeros.cget("text"))
            label_numeros.config(text="*")
            label_numeros.config(text=tipo_boton)

    elif tipo_boton == "Borrar":
        label_numeros.config(text="-")
    elif tipo_boton == "=":
        if tipo_numero == "float":
            num_2 = float(label_numeros.cget("text"))
        else:
            num_2 = int(label_numeros.cget("text"))
        if operacion == "suma":
            suma(num_1, num_2)
        elif operacion == "resta":
            resta(num_1, num_2)
        elif operacion == "division":
            division(num_1, num_2)
        elif operacion == "multiplicacion":
            multiplicacion(num_1, num_2)
        tipo_numero = 0
        
        

def ventana_principal():
    global label_numeros

    ventana = tkinter.Tk()
    ventana.title("Calculadora")
    #ventana.geometry("")

    for fila_index, fila in enumerate(lista_botones):
        for columna_index, contenido_boton in enumerate(fila):
            boton = tkinter.Button(ventana, bg= "#add8e6", text=contenido_boton, width=5, command=lambda tipo_boton=contenido_boton :boton_tocado(tipo_boton))
            boton.grid(row=fila_index+1, column=columna_index)
    boton_igual = tkinter.Button(ventana, bg= "#90EE90", text="=", width=5, command=lambda tipo_boton="=" :boton_tocado(tipo_boton))
    boton_igual.grid(column=0, row=0)

    label_numeros = tkinter.Label(ventana, bg="#ECECEC", text=("-"), font= "Arial 20")
    label_numeros.grid(column=3, row=0)

    ventana.mainloop()

ventana_principal()