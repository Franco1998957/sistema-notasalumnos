from tkinter import *

def promedio():
    window1 = Tk()
    window1.resizable(0,0)
    window1.title("Promedio")
    window1.geometry("400x150")
    
    nota0 = float(txtNota0.get())
    nota1 = float(txtNota1.get())
    nota2 = float(txtNota2.get())
    nota3 = float(txtNota3.get())
    nota4 = float(txtNota4.get())
    nota5 = float(txtNota5.get())
    nota6 = float(txtNota6.get())
    nota7 = float(txtNota7.get())
    nota8 = float(txtNota8.get())
    nota9 = float(txtNota9.get())
    nota10 = float(txtNota10.get())
    nota11 = float(txtNota11.get())
    sum= nota0 + nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10 + nota11
    res= sum/12
    lbl = Label(window1, text= "Nota0" + "Nota1" +  "Nota2" + "Nota3" + "Nota4" + "Nota5" + "Nota6" + "Nota7" + "Nota8" + "Nota9" +  "Nota10" +  "Nota11" + " Suma " + str(sum) + " Promedio " + str(res), font=("Arial Black", 10), bg="seagreen1", fg="seagreen")
    lbl.place(x=0, y=0)
    lblnotasDelCurso.configure(text=" Promedio " + str(res))

    promedio= Label(window1, text="Promedio :" + res, font=("Arial", 11))
    promedio.place(x=5, y=45)

    window1.mainloop()
  
def Promedio():
    window1 = Tk()
    window1.resizable(0,0)
    window1.title("Promedio")
    window1.geometry("400x150")

    promedio= Label(window1, text="Promedio :", font=("Arial", 11))
    promedio.place(x=5, y=45)

    txtpromedio= Entry(window1,width=10)
    txtpromedio.place(x=80, y=50)

    promedio = Button(window1, text="Aceptar Promedio", font=("Arial", 10), width = 15, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2")
    promedio.place(x=150, y=45)

#        def aceptarPromedio():
    
    window1.mainloop()

def mayorAlPromedio():
    window2 = Tk()
    window2.resizable(0,0)
    window2.title("Mayor al Promedio")
    window2.geometry("400x150")

    promedioMayor= Label(window2, text="Promedio Mayor :", font=("Arial", 11))
    promedioMayor.place(x=5, y=45)

    txtpromedioMayor= Entry(window2,width=10)
    txtpromedioMayor.place(x=130, y=50)

    promedioMayor = Button(window2, text="Aceptar Promedio Mayor", font=("Arial", 10), width = 20, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2")
    promedioMayor.place(x=200, y=45)

#        def promedioMayor():

    window2.mainloop()

def opcion1():
    window3 = Tk()
    window3.resizable(0,0)
    window3.title("Opción 1")
    window3.geometry("400x150")

    opción= Label(window3, text="Opción :", font=("Arial", 11))
    opción.place(x=5, y=45)

    txtopción= Entry(window3,width=10)
    txtopción.place(x=70, y=50)

    opción = Button(window3, text="Aceptar Opción", font=("Arial", 10), width = 15, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2")
    opción.place(x=140, y=45)

##        def aceptarOpcion1():
    
    window3.mainloop()
    
def opcion2():
    window4 = Tk()
    window4.resizable(0,0)
    window4.title("Opción 2")
    window4.geometry("400x150")

    opción1= Label(window4, text="Opción :", font=("Arial", 11))
    opción1.place(x=5, y=45)

    txtopción1= Entry(window4,width=10)
    txtopción1.place(x=70, y=50)

    opción1 = Button(window4, text="Aceptar Opción", font=("Arial", 10), width = 15, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2")
    opción1.place(x=140, y=45)

##        def aceptarOpcion2():

    window4.mainloop()

def cambiarNota():
    
    window5 = Tk()
    window5.resizable(0,0)
    window5.title("Cambio de Nota")
    window5.geometry("400x150")

    nota= Label(window5, text="Nota :", font=("Arial", 11))
    nota.place(x=5, y=45)

    txtNota= Entry(window5,width=10)
    txtNota.place(x=50, y=50)

    cambiarNota = Button(window5, text="Aceptar Cambios", font=("Arial", 10), width = 15, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
    cambiarNota.place(x=140, y=45)

    window5.mainloop()

window = Tk()
window.resizable(0,0)
window.title("Notas del Curso")
window.geometry('775x543')

FoNdO =PhotoImage(file="FoNdO.gif")
lblFoNdO=Label(window, image=FoNdO).place(x=0, y=5)

#Cuadro Estético

cuadro_notas = Canvas(window, width=380, height=470, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=390, y=5)
cuadro_notas = Canvas(window, width=775, height=470, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=477)

# Estudiantes

estudiantes = Label(window, text="Estudiantes", font=("Arial"))
estudiantes.place(x=390, y=0)
notas = Label(window, text="Notas", font=("Arial"))
notas.place(x=570, y=0)
Estudiante1 = Label(window, text="Estudiante1 :", font=("Arial", 11))
Estudiante1.place(x=400, y=25)
Estudiante2 = Label(window, text="Estudiante2 :", font=("Arial", 11))
Estudiante2.place(x=400, y=55)
Estudiante3 = Label(window, text="Estudiante3 :", font=("Arial", 11))
Estudiante3.place(x=400, y=95)
Estudiante4 = Label(window, text="Estudiante4 :", font=("Arial", 11))
Estudiante4.place(x=400, y=135)
Estudiante5 = Label(window, text="Estudiante5 :", font=("Arial", 11))
Estudiante5.place(x=400, y=175)
Estudiante6= Label(window, text="Estudiante6 :", font=("Arial", 11))
Estudiante6.place(x=400, y=215)
Estudiante7 = Label(window, text="Estudiante7 :", font=("Arial", 11))
Estudiante7.place(x=400, y=255)
Estudiante8 = Label(window, text="Estudiante8 :", font=("Arial", 11))
Estudiante8.place(x=400, y=295)
Estudiante9 = Label(window, text="Estudiante9 :", font=("Arial", 11))
Estudiante9.place(x=400, y=335)
Estudiante10 = Label(window, text="Estudiante10 :", font=("Arial", 11))
Estudiante10.place(x=400, y=375)
Estudiante11 = Label(window, text="Estudiante11 :", font=("Arial", 11))
Estudiante11.place(x=400, y=410)
Estudiante12 = Label(window, text="Estudiante12 :", font=("Arial", 11))
Estudiante12.place(x=400, y=445)

#Cuadros

txtNota0= Label(window, text="0.0" ,width=5)
txtNota0.place(x=570, y=25)
txtNota1= Label(window, text=("0.0") ,width=5)
txtNota1.place(x=570, y=55)
txtNota2= Label(window, text=("0.0") ,width=5)
txtNota2.place(x=570, y=95)
txtNota3= Label(window, text=("0.0") ,width=5)
txtNota3.place(x=570, y=135)
txtNota4= Label(window, text=("0.0") , width=5)
txtNota4.place(x=570, y=175)
txtNota5= Label(window, text=("0.0") , width=5)
txtNota5.place(x=570, y=215)
txtNota6= Label(window, text=("0.0") ,width=5)
txtNota6.place(x=570, y=255)
txtNota7= Label(window, text=("0.0") ,width=5)
txtNota7.place(x=570, y=295)
txtNota8= Label(window, text=("0.0") ,width=5)
txtNota8.place(x=570, y=335)
txtNota9= Label(window, text=("0.0") ,width=5)
txtNota9.place(x=570, y=375)
txtNota10= Label(window, text=("0.0") ,width=5)
txtNota10.place(x=570, y=415)
txtNota11= Label(window, text=("0.0") , width=5)
txtNota11.place(x=570, y=445)

# Botones de Cambiar Nota

cambiar1 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar1.place(x=650, y=25)
cambiar2 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar2.place(x=650, y=55)
cambiar3 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar3.place(x=650, y=95)
cambiar4 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar4.place(x=650, y=135)
cambiar5 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar5.place(x=650, y=175)
cambiar6 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar6.place(x=650, y=215)
cambiar7 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar7.place(x=650, y=255)
cambiar8 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar8.place(x=650, y=295)
cambiar9 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar9.place(x=650, y=335)
cambiar10 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar10.place(x=650, y=375)
cambiar11 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar11.place(x=650, y=415)
cambiar12 = Button(window, text="Cambiar", font=("Arial", 10), width = 8, borderwidth=1, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiarNota)
cambiar12.place(x=650, y=445)

#Adiciones

adicionales = Label(window, text="Adicionales", font="Arial").place(x=350, y=480)
Promedio = Button(window, text="Promedio", font=("Arial", 10), width = 15, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=promedio)
Promedio.place(x=80, y=510)
MayorAlPromedio = Button(window, text="Estudiantes mayor al promedio", font=("Arial", 10), width = 22 , borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=mayorAlPromedio)
MayorAlPromedio.place(x=220, y=510)
Opcion1 = Button(window, text="Opcion1", font=("Arial", 10), width = 15, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=opcion1)
Opcion1.place(x=420, y=510)
Opcion2 = Button(window, text="Opcion2", font=("Arial", 10), width = 15, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=opcion2)
Opcion2.place(x=560, y=510)

listaEstudiante()

window.mainloop()
