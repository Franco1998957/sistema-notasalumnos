from tkinter import ttk, messagebox
from tkinter import *
from  tkinter import  ttk
#---------------ventana-----------------------#
window = Tk()
window.title("ESTUDIANTES")
window.resizable(0,0)
window.geometry("900x600")
#-----------------frame-------------------------------#
miFrame1 = Frame(window,width="450", height="520",bd="10",bg="black")
miFrame1.grid(row=0,column=0)
imagen=PhotoImage(file="estudiantes.gif")
fondo=Label(miFrame1,image=imagen,bg="black").place(x=0,y=0)
#------------------------------------------------------------------
miFrame2 = Frame(window,width="450", height="520",bd="10",relief="groove",bg="black")
miFrame2.grid(row=0,column=1)
#-----------------variables globales---------------------------
prom=[0.0]
listanotas=list()
for R in range(12):
    listanotas.append(0.0)
#-------------Requerimientos------------------
def calcularPromedio():
    totaldenotas=0.0
    for notaAlumno in listanotas:
        totaldenotas += notaAlumno
    promedioN = totaldenotas / len(listanotas)
    promedioN = round(promedioN, 2)
    messagebox.showinfo("la cantidad de estudiantes mayor al promedio es de :", str(promedioN))
    prom.append(float(promedioN))

def cal_cant_mayor_prom():
    cont=0
    promedio=prom[1]
    for notaAlummno in listanotas:
        if notaAlummno>promedio:
            cont+=1
    messagebox.showinfo("la cantidad de estudiantes mayor al promedio es de :", str(cont))

#-----------------crear botones y labels-------------------
def  crearBotones():
    b=30
    listButton=list()
    for B in range(12):
        btnCambiar = Button(miFrame2, width="14", height="1", text="CAMBIAR")
        btnCambiar.place(x=180, y=b)
        b += 30
        listButton.append(btnCambiar)
    return listButton
def crearLabel():
    y=30
    x=0
    r=30
    for  i in  range(12):
        if i==0:
            Label(miFrame2, text="Notas: ", font=("Arial black  ", 14), fg="white",relief="groove",bg="black").place(x=x, y=0)
        i+=1
        Label(miFrame2, text="estudiante {}:".format(i), font=("Arial  ", 11), fg="Red",bg="black").place(x=x, y=y)
        y+=30
    for  R in range(12):
        x = 110
        label = Label(miFrame2, text=listanotas[R], font=("Arial  ", 11), fg="white",bg="black")
        label.place(x=x, y=r)
        r += 30

#--------------modificar notas----------------------
def modificar(i):
        def aceptar():
            nota = float(nuevanota.get())
            if  nota<=5.00:
                nota = round(nota, 2)
                listanotas[i] = nota
                crearLabel()
            else:
                Label(window2, text="ingrese una nota entre 0 y 5", font=("Arial  ", 11), relief="groove",fg="red" ).place(x=10,  y=20)
        window2 = Tk()
        window2.geometry("200x150")
        Label(window2, text="ingrese el valor a cambiar", font=("Arial  ", 11), relief="groove", ).place(x=10, y=20)
        btnCambiar = Button(window2, width="14", height="1", text="Cambiar nota", command=aceptar)
        btnCambiar.place(x=50, y=90)
        nuevanota = Entry(window2,width="11")
        nuevanota.place(x=70, y=50)
        window2.title("cambiar nota")
        window2.resizable(0, 0)


#-----------------------_______BOTONES DE REQUERIMIENTOS------------------------------------------
btonPROM=Button(window, width="20", height="2", text="PROMEDIO",command=calcularPromedio)
btonPROM.place(x=350,y=550)
btonPROM=Button(window, width="20", height="2", text="Mayor al del promedio",command=cal_cant_mayor_prom)
btonPROM.place(x=500,y=550)
#---------------------------------------LISTAINTERFAZ-----------------------------------------
listacrearlbl=crearLabel()
listabotones=crearBotones()
#-----------------------esto se debe de hacer para interactuar con la nota de cada estudiante-------------------------------------------
listabotones[0].config(command=lambda:modificar(0) )
listabotones[1].config(command=lambda:modificar(1) )
listabotones[2].config(command=lambda:modificar(2) )
listabotones[3].config(command=lambda:modificar(3) )
listabotones[4].config(command=lambda:modificar(4) )
listabotones[5].config(command=lambda:modificar(5) )
listabotones[6].config(command=lambda:modificar(6) )
listabotones[7].config(command=lambda:modificar(7) )
listabotones[8].config(command=lambda:modificar(8) )
listabotones[9].config(command=lambda:modificar(9) )
listabotones[10].config(command=lambda:modificar(10) )
listabotones[11].config(command=lambda:modificar(11) )
window.mainloop()