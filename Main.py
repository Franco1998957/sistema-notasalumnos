from tkinter import *
from PIL import ImageTk, Image

#Creacion de Tk y Toplevel
root = Tk()
root.withdraw()
root.overrideredirect(1)
root.configure(bg='black')
root.geometry('+400+350')

window = Toplevel()
window.geometry('800x600+250+50')
window.resizable(False,False)
window.configure(bg='black')
window.protocol("WM_DELETE_WINDOW", root.destroy)

#Quit Button
but = Button(window, text='deiconify')
but['command'] = root.deiconify
but.pack()

#Variables globales
"""""
La confeccion de la lista esta hecha de esta manera: triples es una lista con tantas listas adentro como estudiantes haya.
Los elemenetos de cada lista dentro de triples estan compuestos por la altura a la que van el label y el botón del estudiante.
El segundo elemento es el numero del estudiante y el tercero es la nota que le corresponde.
Esta lista existe con el fin de no llamar a la funcion "crear_label" un numero incierto de veces.
"""""
triples=[[40,1, 4.5],[80, 2, 3.7],[120, 3, 1.5],[160, 4, 3.6],[200, 5, 5.0],[240, 6, 4.8],[280, 7, 0.8],[320, 8, 4.3],[360, 9, 4.1],[400, 10, 2.5],[440, 11, 4.6],[480, 12, 4.0]]
"""""
En el codigo se crea una instancia con un boton Cambiar.
Cuando se apreta el boton 'Cambiar' por primera vez se destruye la instancia en donde fue creado el boton, y al apretar
el boton 'Aceptar' se vuelve a crear la misma instancia, pero anteriormente en el codigo ya se habia creado esta instancia,
por lo que quedan dos botones con el mismo nombre y al apretar el boton 'Cambiar' de nuevo, este solo destruye una instancia,
es por eso que se crean las variables globales 'antecedente' y 'Estudiante_x_Button', la primera sirve de condicion para 
verificar que ya se ha apretado por primera vez el boton 'Cambiar' cuando valga '1',y la segunda es una lista que sirve 
para guardar la segunda instancia del boton 'Cambiar' que se crea, para cada estudiante, es decir cada indice corresponde
al boton de un estudiante, y asi poder eliminar ambas instancias una vez se apreta el boton 'Cambiar', para cada estudiante.
"""""
antecedente=0
Estudiante_x_Button_= [0]
for i in range(len(triples)):
    Estudiante_x_Button_.append(0)
#Funciones
def calculo_promedio():
    global triples
    promedio=0
    for i in range(len(triples)):
        promedio+=triples[i][2]
    promedio=round(promedio/len(triples),2)
    return promedio
def promedio_():
    promedio=calculo_promedio()
    root.deiconify()
    Label_promedio= Label(root, text="El promedio de notas es: {0}".format(promedio), fg='purple',bg='black', font=('Open Sans',11))
    Label_promedio.pack()
    def Ok():
        Label_promedio.destroy()
        Button_Aceptar.destroy()
        root.withdraw()
    Button_Aceptar= Button(root, text="Ok.",command=Ok, fg='purple',bg='black', font=('Open Sans',11))
    Button_Aceptar.pack()
def Mayor_al_Promedio():
    global triples
    promedio=calculo_promedio()
    lista_estudiantes = list()
    for i in range(len(triples)):
        if triples[i][2]>promedio:
            lista_estudiantes.append(i+1)
    root.deiconify()
    Label_promedio= Label(root, text="El promedio de notas es de: {0}".format(promedio), fg='purple',bg='black', font=('Open Sans',11))
    Label_promedio.pack()
    label_ = []
    for i in range(len(lista_estudiantes)):
        label = Label(root, text="El estudiante {0} está por encima del promedio".format(lista_estudiantes[i]), fg='purple',bg='black', font=('Open Sans',11))
        label_.append(label)
        label.pack()
    def Ok():
        Label_promedio.destroy()
        for i in range(len(label_)):
            label_[i].destroy()
        Button_Aceptar.destroy()
        root.withdraw()
    Button_Aceptar= Button(root, text="Ok.",command=Ok, fg='white',bg='black', font=('Open Sans',11))
    Button_Aceptar.pack()
def crear_label(Y, numero_estudiante, nota_estudiante):
    Estudiante_x_Label = Label(frame_notas, text="", fg='white',bg='black', font=('Open Sans',11))
    Estudiante_x_Label.configure(text="Estudiante {0}:".format(numero_estudiante))
    Estudiante_x_Label.place(x=0,y=Y)
    Nota_estudiante_Label= Label(frame_notas, text=nota_estudiante, fg='purple',bg='black', font=('Open Sans',11))
    Nota_estudiante_Label.place(x=150,y=Y)
    def Cambiar():
        global antecedente, Estudiante_x_Button_
        Estudiante_x_Button.destroy()
        if antecedente==1 and Estudiante_x_Button_[numero_estudiante]!=0:
            Estudiante_x_Button_[numero_estudiante].destroy()
        Nota=IntVar(frame_notas,nota_estudiante)
        Nota_estudiante_Label.place(x=-5000,y=-5000)
        Nota_estudiante_Entry = Entry(frame_notas,textvariable=Nota)
        Nota_estudiante_Entry.place(x=150,y=Y,width=20)
        def Aceptar():
            global triples, antecedente, Estudiante_x_Button_
            antecedente=1
            triples[numero_estudiante][2]=Nota.get()
            Nota_estudiante_Label.configure(text=Nota.get())
            Nota_estudiante_Label.place(x=150,y=Y)
            Nota_estudiante_Entry.destroy()
            Button_Aceptar.destroy()
            Estudiante_x_Button_[numero_estudiante] = Button(frame_notas, text='Cambiar',command=Cambiar, fg='white',bg='black', font=('Open Sans',10),width=10)
            Estudiante_x_Button_[numero_estudiante].place(x=245,y=Y-3)
        Button_Aceptar= Button(frame_notas, text="Aceptar",command=Aceptar, fg='white',bg='black', font=('Open Sans',11))
        Button_Aceptar.place(x=260,y=Y-3)
    Estudiante_x_Button = Button(frame_notas, text='Cambiar',command=Cambiar, fg='white',bg='black', font=('Open Sans',10),width=10)
    Estudiante_x_Button.place(x=245,y=Y-3)
#GUI
    #frame imagen
frame_imagen= Frame(window, width=450, height=510,relief=RAISED)
frame_imagen.place(x=0,y=0)
img = ImageTk.PhotoImage(Image.open(r'C:\Users\Agus\Downloads\curso.jpg'))
panel = Label(frame_imagen, image = img, relief=SUNKEN)
panel.place(x=0,y=0)
panel.image = img
    #frame_Notas
frame_notas = Frame(window, width=350, height=515,bg='black',relief=RAISED,bd=5)
frame_notas.place(x=451,y=0)
Notas_Label = Label(frame_notas, text='Notas',bg='black',fg='purple', font=('Open Sans',15),relief=RAISED)
Notas_Label.place(x=135,y=0)
for triple in triples:
        crear_label(triple[0],triple[1],triple[2])  
    #frame_Adicionales
frame_Adicionales = Frame(window, width=800, height=90,bg='black',relief=RAISED,bd=5)
frame_Adicionales.place(x=1,y=510)
Adicionales_Label = Label(window, text='Adicionales',bg='black',fg='purple', font=('Open Sans',15),relief=RAISED)
Adicionales_Label.place(x=4,y=513)
frame_botones = Frame(frame_Adicionales, width=600,height=50,relief=RAISED,bd=5)
frame_botones.place(x=150,y=20)
Boton_promedio = Button(frame_botones, command=promedio_, text='Promedio', fg='white',bg='black', font=('Open Sans',12),width=30)
Boton_promedio.pack(side=LEFT)
Boton_Mayor_al_promedio = Button(frame_botones, command=Mayor_al_Promedio, text='# Mayor al promedio', fg='white',bg='black', font=('Open Sans',12),width=30)
Boton_Mayor_al_promedio.pack(side=LEFT)            

root.mainloop()

