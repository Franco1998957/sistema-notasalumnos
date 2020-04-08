from tkinter import ttk
from tkinter import *
from  tkinter import  ttk
#---------------ventana-----------------------#
window = Tk()
window.title("ESTUDIANTES")
window.resizable(0,0)
window.geometry("900x600")
#------------------------------------------------#
miFrame1 = Frame(window,width="450", height="520",bd="10",bg="black")
miFrame1.grid(row=0,column=0)
imagen=PhotoImage(file="estudiantes.gif")
fondo=Label(miFrame1,image=imagen,bg="black").place(x=0,y=0)
#------------------------------------------------------------------
miFrame2 = Frame(window,width="450", height="520",bd="10",relief="groove",bg="black")
miFrame2.grid(row=0,column=1)
#-------------------------------------------------------------------
def  crearBotones():
    b=30
    listButton=list()
    for B in range(12):
        btnCambiar = Button(miFrame2, width="14", height="1", text="CAMBIAR",command=lambda :modificar())
        btnCambiar.place(x=180, y=b)
        b += 30
        listButton.append(btnCambiar)

def crearLabel():
    listalabels=list()
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
        listalabels.append(0.0)
        x = 110
        label = Label(miFrame2, text=listalabels[R], font=("Arial  ", 11), fg="white",relief="groove",bg="black")
        label.place(x=x, y=r)
        r += 30
    return listalabels

def modificar(i):
        def aceptar():
            cambiarnot.get()

        window2 = Tk()
        window2.geometry("200x200")
        btnCambiar = Button(window2, width="14", height="1", text="Aceptar", command=aceptar)
        btnCambiar.place(x=20, y=30)
        cambiarnot = Entry(window2)
        cambiarnot.configure(width="11")
        cambiarnot.place(x=40, y=30)

        window2.title("ESTUDIANTES")
        window2.resizable(0, 0)


#-----------------------BOTON OPCIONES----------------------------------------------------------------------------------------------
btonPROM=Button(window, width="20", height="2", text="PROMEDIO")
btonPROM.place(x=350,y=550)
btonPROM=Button(window, width="20", height="2", text="Mayor al del promedio")
btonPROM.place(x=500,y=550)
#---------------------------------------LISTAINTERFAZ----------------------------------------------------------------------------
listacrearlbl=crearLabel()
listabotones=crearBotones()
#---------------------------------------------------------------------------------------------------------------------


window.mainloop()