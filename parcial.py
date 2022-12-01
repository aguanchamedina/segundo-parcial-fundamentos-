from tkinter import *
import numpy as np
from tkinter import messagebox


# FUNCIONES 
def limpiar():
    Funcion_Problema.set("")
    Funcion_Problema1.set("")
    
def matriz(): 
    filas=int(Funcion_Problema.get()) 
    columnas=int(Funcion_Problema1.get())
    matriz=[]

    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor=int(input("fila{},columna{}:".format(i+1,j+1)))
            matriz[i].append(valor)
    print()
    for fila in matriz:
        print("[",end=" ")
        for elemento in fila:
            print("{}".format(elemento),end=" ")
            print("]")
    print()
    
    for ma in matriz:
        for m in ma:
            print(m)
        diction = []
        diction.append(m)
       
        maxInt = max(diction)
        counter = [0] * (maxInt+1)
        for i in diction:
            counter[i] += 1
        
        result = {}
        for i in range(maxInt):
            if(counter[i]>1):
                result[i] = i * counter [i]
    solucion_matriz.set(result)
    return result

# FUNCIONES MENU 
def manual_usuario():
    messagebox.showinfo("Manual de usuario", "En construcción...")
def acerca_de():
    messagebox.showinfo("Acerca de...", "Versión 1.0")
    
def salir():
    root.destroy()
  

# VENTANA TK
root=Tk()
root.title("MATRICES")
root.geometry("800x500")
root.config(bg="white")
barra_menus = Menu()
root.config(menu=barra_menus)
menu_edicion = Menu(tearoff=0)

# PANELES
panel2=Frame()
panel3=Frame()
panel2.config(width="800",height="470",bg="blue")
panel2.place(x=0,y=120)
panel3.config(width="800",height="470",bg="red")
panel3.place(x=0,y=190)

Funcion_Problema=StringVar()
Funcion3=Entry(root,textvariable=Funcion_Problema).place(x=320,y=240)
Funcion_Problema1=StringVar()
Funcion3=Entry(root,textvariable=Funcion_Problema1).place(x=320,y=284)
solucion_matriz=StringVar()
Funcion3=Entry(root,textvariable=solucion_matriz).place(x=320,y=414)

# BOTONES 
boton1=Button(root,text="Solucionar",width=10,height=1,bg="LightBlue1",relief="groove",command=matriz)
boton1.place(x=460, y=204)

boton2=Button(root,text="Revisar numero que se repite",width=10,height=1,bg="LightBlue1",relief="groove",command=limpiar)
boton2.place(x=660, y=254)

# TITULOS 
titulo2=Label(root,text="Matrices",bg="dark slate gray",font=('Georgia',16,),fg="white")
titulo2.place(x=830,y=284)

titulo5=Label(root,text="Numero_de_columnas",bg="dark slate gray",font=('Times New Roman',16,),fg="white")
titulo5.place(x=0,y=240)

titulo6=Label(root,text="Numero_de_fiilas",bg="dark slate gray",font=('Times New Roman',16,),fg="white")
titulo6.place(x=0,y=284)

titulo7=Label(root,text="numero que se repite",bg="dark slate gray",font=('Times New Roman',16,),fg="white")
titulo7.place(x=0,y=414)

# BARRA DE MENU 
menu_archivo = Menu(tearoff=0)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", compound="left", command=salir)
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)
menu_edicion.add_command(label="En proceso ", command=manual_usuario)
barra_menus.add_cascade(label="Edición", menu=menu_edicion)
menu_ayuda = Menu(tearoff=0)
menu_ayuda.add_command(label="Términos y Condiciones", command=manual_usuario)
menu_ayuda.add_command(label="Versión del programa", command=acerca_de)
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

# FIN DEL PROGRAMAA 
root.mainloop()
