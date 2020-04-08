from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('Notas Estudiantiles')
window.geometry('570x385')
window.resizable(0,0)

lst_notas = list()
for i in range(12):
    lst_notas.append(0.0)

def promedio():
    total = 0.0
    for una_nota in lst_notas:
        total += una_nota
    prom = total / len(lst_notas)
    messagebox.showinfo("Promedio del curso",str(prom))

def estudianteMayorProm():
    cont=0
    total = 0.0
    for una_nota in lst_notas:
        total += una_nota
    prom = total / len(lst_notas)
    for una_nota in lst_notas:
        if una_nota>prom:
            cont+=1
    messagebox.showinfo("Estudiantes mayor al promedio","Cantidad de estudiantes mayor al promedio: "+str(cont))

def botonCambiar(id):
    def guardar():
        try:
            nuevaNota = float(et.get())
            if nuevaNota<=5.0 and nuevaNota>=0.0:
                lst_notas[id]=nuevaNota
                crearLista()
                window2.destroy()
            else:
                messagebox.showinfo("Alerta","La nota debe ser entre 0 y 5")
                window2.destroy()
        except:
            messagebox.showerror("ERROR","Verifique los campos y vuelva a intentarlo")
            window2.destroy()
    window2=Tk()
    window2.title('Notas Estudiantiles')
    window2.resizable(0,0)
    Label(window2,text="Nueva nota:",font=("Arial", 10)).grid(row=0,column=0)
    et = Entry(window2)
    et.grid(row=0,column=1)
    bt = Button(window2,text="Guardar",command=guardar)
    bt.grid(row=1,column=1)
    window2.mainloop()

def crearBotones():
    lst_botones =  list()
    row = 1
    for i in range(12):
        bt_notas = Button(frame1,text="Cambiar")
        bt_notas.grid(row=row,column=2)
        lst_botones.append(bt_notas)
        row = row+1
    return lst_botones

def crearLista():
    row = 1
    for i in range(12):
        nro = i+1
        nro = str(nro)
        Label(frame1,text="Estudiante "+nro+":",font=("Arial", 10)).grid(row=row,column=0)
        lbl_notas = Label(frame1,text=str(lst_notas[i]),font=("Arial", 10), fg="blue")
        lbl_notas.grid(row=row,column=1)
        row = row+1

#Frame Imagen
frame = Frame(window,relief="groove",bd=5)
frame.place(x=185,y=5)
imagen = PhotoImage(file="curso.gif")
Label(frame,image=imagen).pack()

#Frame Contenido
frame1 = Frame(window,relief="groove",bd=5)
frame1.place(x=0,y=0)
#Titulo Notas para el Frame
Label(frame1,text="Notas",font=("Arial black", 11)).grid(row=0,column=0)
#Creamos lista de botones con sus notas y botones
crearLista()
listaBotones = crearBotones()

#Frame Adicionales
frame2 = Frame(window,relief="groove",bd=5)
frame2.place(x=0,y=350)
#Creamos botones
Button(frame2,text="Promedio",command=promedio,width="25").grid(row=1,column=0)
Button(frame2,text="Estudiantes mayor al promedio",command=estudianteMayorProm).grid(row=1,column=1)

#Configurar comando de botones, ya que no me funciona colocando variables en un for
listaBotones[0].config(command=lambda: botonCambiar(0))
listaBotones[1].config(command=lambda: botonCambiar(1))
listaBotones[2].config(command=lambda: botonCambiar(2))
listaBotones[3].config(command=lambda: botonCambiar(3))
listaBotones[4].config(command=lambda: botonCambiar(4))
listaBotones[5].config(command=lambda: botonCambiar(5))
listaBotones[6].config(command=lambda: botonCambiar(6))
listaBotones[7].config(command=lambda: botonCambiar(7))
listaBotones[8].config(command=lambda: botonCambiar(8))
listaBotones[9].config(command=lambda: botonCambiar(9))
listaBotones[10].config(command=lambda: botonCambiar(10))
listaBotones[11].config(command=lambda: botonCambiar(11))
window.mainloop()
