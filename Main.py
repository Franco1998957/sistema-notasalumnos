#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.withdraw()
root.overrideredirect(1)
root.configure(bg='white')
root.geometry('+400+350')
window = Toplevel()
window.geometry('800x600')
window.title('Caso de estudio: ')
window.resizable(False, False)
window.configure(bg='white')
window.protocol("WM_DELETE_WINDOW", root.destroy)

but = Button(window, text='deiconify')
but['command'] = root.deiconify
but.pack()


triples = [[40, 1, 4.5], [80, 2, 3.7], [120, 3, 1.5], [160, 4, 3.6], [200, 5, 5.0], [240, 6, 4.8], [280, 7, 0.8],
           [320, 8, 4.3], [360, 9, 4.1], [400, 10, 2.5], [440, 11, 4.6], [480, 12, 4.0]]

antecedente = 0
Estudiante_x_boton_ = [""]
for i in range (len(triples)+1):
    Estudiante_x_boton_.append(0)

####################################################################################################################

# Funciones

def Cal_promedio():
    global triples
    promedio = 0
    for i in range(len(triples)):
        promedio += triples[i][2]
    promedio = round(promedio / len(triples), 2)
    return promedio


def promedio_():
    promedio = Cal_promedio()
    root.deiconify()
    Label_promedio = Label(root, text="El promedio de notas es: {0}".format(promedio))
    Label_promedio.pack()

    def Ok():
        Label_promedio.destroy()
        Button_Aceptar.destroy()
        root.withdraw()

    Button_Aceptar = Button(root, text="Ok", command=Ok, font=('Arial', 11))
    Button_Aceptar.pack()


def Mayor_al_Promedio():
    global triples
    promedio=Cal_promedio()
    lista_estudiantes = list()
    for i in range(len(triples)):
        if triples[i][2]>promedio:
            lista_estudiantes.append(i+1)
    root.deiconify()
    Label_promedio= Label(root, text="El promedio de notas es de: {0}".format(promedio), fg='black',bg='white', font=('Arial',11))
    Label_promedio.pack()
    label_ = []
    for i in range(len(lista_estudiantes)):
        label = Label(root, text="El estudiante {0} está por encima del promedio".format(lista_estudiantes[i]), fg='black',bg='white', font=('Arial',11))
        label_.append(label)
        label.pack()
    def Ok():
        Label_promedio.destroy()
        for i in range(len(label_)):
            label_[i].destroy()
        Button_Aceptar.destroy()
        root.withdraw()
    Button_Aceptar= Button(root, text="Ok.",command=Ok, fg='black', font=('Arial',11))
    Button_Aceptar.pack()

def crear_label(Y, numero_estudiante, nota_estudiante):
    Estudiante_x_Label = Label(frame_notas, text="", fg='black', bg='white', font=('Arial', 11))
    Estudiante_x_Label.configure(text="Estudiante {0}:".format(numero_estudiante))
    Estudiante_x_Label.place(x=0, y=Y)
    Nota_estudiante_Label = Label(frame_notas, text=nota_estudiante, fg='blue', bg='white', font=('Arial', 11))
    Nota_estudiante_Label.place(x=150, y=Y)

    def Cambiar():
        global antecedente, Estudiante_x_boton_
        Estudiante_x_boton.destroy()
        if antecedente==1 and Estudiante_x_boton_[numero_estudiante]!=0:
            Estudiante_x_boton_[numero_estudiante].destroy()
        Nota = StringVar(frame_notas,nota_estudiante)
        Nota_estudiante_Label.place(x=-5000, y=-5000)
        Nota_estudiante_Entry = Entry(frame_notas, textvariable=Nota)
        Nota_estudiante_Entry.place(x=150, y=Y, width=20)

        def Aceptar():
            global triples, antecedente, Estudiante_x_boton
            try:
                if float(Nota.get())>=0 and float(Nota.get())<=5.0:
                    antecedente=1
                    triples[numero_estudiante-1][2]=float(Nota.get())
                    Nota_estudiante_Label.configure(text=float(Nota.get()))
                    Nota_estudiante_Label.place(x=150,y=Y)
                    Nota_estudiante_Entry.destroy()
                    Button_Aceptar.destroy()
                    Estudiante_x_boton_[numero_estudiante] = Button(frame_notas, text='Cambiar',command=Cambiar, fg='white',bg='pink', font=('Arial',10),width=10)
                    Estudiante_x_boton_[numero_estudiante].place(x=245,y=Y-3)
                elif float(Nota.get())<0 and float(Nota.get())>5.0:
                    messagebox.showinfo('Ocurrió un error','Debe ingresar un valor entre 0 y 5')
            except ValueError:
                messagebox.showinfo('Ocurrió un error','Debe ingresar un valor decimal o entero')
        Button_Aceptar= Button(frame_notas, text="Aceptar",command=Aceptar, fg='white',bg='pink', font=('Arial',10))
        Button_Aceptar.place(x=260,y=Y-3)
    Estudiante_x_boton = Button(frame_notas, text='Cambiar', command=Cambiar, fg='white', bg='pink',font=('Arial', 10), width=10)
    Estudiante_x_boton.place(x=245, y=Y - 3)

####################################################################################################################

# Interfaz:

# frame imagen:
frame_imagen = Frame(window, width=470, height=520, relief=RAISED)
frame_imagen.place(x=0, y=0)
img = ImageTk.PhotoImage(Image.open(r'C:\Users\brian\Downloads\Clase.png'))
panel = Label(frame_imagen, image=img, relief=SUNKEN)
panel.place(x=0, y=0)
panel.image = img

# Frame Notas:

frame_notas = Frame(window, width=350, height=515, bg='white', relief=RAISED, bd=5)
frame_notas.place(x=451, y=0)
Notas_Label = Label(frame_notas, text='Notas', bg='white', fg='black', font=('Arial', 15), relief=RAISED)
Notas_Label.place(x=135, y=0)
for triple in triples:
    crear_label(triple[0], triple[1], triple[2])

# Frame Adicionales:

frame_Adicionales = Frame(window, width=800, height=90, bg='white', relief=RAISED, bd=5)
frame_Adicionales.place(x=1, y=510)
Adicionales_Label = Label(window, text='Adicionales', bg='white', fg='black', font=('Arial', 15), relief=RAISED)
Adicionales_Label.place(x=4, y=513)
frame_botones = Frame(frame_Adicionales, width=600, height=50, relief=RAISED, bd=5)
frame_botones.place(x=150, y=20)
Boton_promedio = Button(frame_botones, command=promedio_, text='Promedio', fg='black', bg='white', font=('Arial', 12), width=30)
Boton_promedio.pack(side=LEFT)
Boton_Mayor_al_promedio = Button(frame_botones, command=Mayor_al_Promedio, text='Mayor al promedio', fg='black',bg='white', font=('Arial', 12), width=30)
Boton_Mayor_al_promedio.pack(side=LEFT)

root.mainloop()


# In[2]:


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


# In[ ]:




