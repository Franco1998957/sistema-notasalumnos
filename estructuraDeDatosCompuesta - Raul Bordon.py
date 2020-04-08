from tkinter import Tk
from tkinter import messagebox
from tkinter import *

#variables
tot=round(float(0),2)
listaNotas=[round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2),round(float(0),2)]

#ventana
ventana=Tk()
ventana.title("Las Notas de un Curso")
ventana.geometry("800x540")

#canvas
tit=Canvas(ventana,width=800,height=70, borderwidth=2,relief="raised")
tit.create_rectangle(0,0,900,900)
tit.place(x=0,y=0)

ima=Canvas(ventana,width=500,height=380, borderwidth=2,relief="raised")
ima.create_rectangle(0,0,800,600)
ima.place(x=0,y=76)

notaC=Canvas(ventana,width=293,height=380, borderwidth=2,relief="raised")
notaC.create_rectangle(0,0,800,600)
notaC.place(x=507,y=76)

est=Canvas(ventana,width=800,height=60, borderwidth=2,relief="raised")
est.create_rectangle(0,0,900,900)
est.place(x=0,y=464)

titulo=Label(ventana, text="Notas de los Alumnos", font=("Times New Roman",36,"bold"),fg="black")
titulo.place(x=190,y=3)

#imagen
imageAlu=PhotoImage(file="scholarship (2).png")
Label(ventana,image=imageAlu).place(x=180,y=220)

#funciones
def cambiar1():
    def guardar():
        global listaNotas
        listaNotas[0]=round(float(cambiarNotaTxt.get()),2)
        not1.configure(text=listaNotas[0])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar2():
    def guardar():
        global listaNotas
        listaNotas[1]=round(float(cambiarNotaTxt.get()),2)
        not2.configure(text=listaNotas[1])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar3():
    def guardar():
        global listaNotas
        listaNotas[2]=round(float(cambiarNotaTxt.get()),2)
        not3.configure(text=listaNotas[2])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar4():
    def guardar():
        global listaNotas
        listaNotas[3]=round(float(cambiarNotaTxt.get()),2)
        not4.configure(text=listaNotas[3])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar5():
    def guardar():
        global listaNotas
        listaNotas[4]=round(float(cambiarNotaTxt.get()),2)
        not5.configure(text=listaNotas[4])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar6():
    def guardar():
        global listaNotas
        listaNotas[5]=round(float(cambiarNotaTxt.get()),2)
        not6.configure(text=listaNotas[5])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar7():
    def guardar():
        global listaNotas
        listaNotas[6]=round(float(cambiarNotaTxt.get()),2)
        not7.configure(text=listaNotas[6])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar8():
    def guardar():
        global listaNotas
        listaNotas[7]=round(float(cambiarNotaTxt.get()),2)
        not8.configure(text=listaNotas[7])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar9():
    def guardar():
        global listaNotas
        listaNotas[8]=round(float(cambiarNotaTxt.get()),2)
        not9.configure(text=listaNotas[8])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar10():
    def guardar():
        global listaNotas
        listaNotas[9]=round(float(cambiarNotaTxt.get()),2)
        not10.configure(text=listaNotas[9])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar11():
    def guardar():
        global listaNotas
        listaNotas[10]=round(float(cambiarNotaTxt.get()),2)
        not11.configure(text=listaNotas[10])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

def cambiar12():
    def guardar():
        global listaNotas
        listaNotas[11]=round(float(cambiarNotaTxt.get()),2)
        not12.configure(text=listaNotas[11])
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
        ventanaCambiar.destroy()
    ventanaCambiar=Tk()
    ventanaCambiar.title("Cambiar Nota")
    ventanaCambiar.geometry("400x90")
        
    cambiarNota=Label(ventanaCambiar, text="Nueva Nota:", font=("Arial",12), fg="black")
    cambiarNota.place(x=0,y=10)
    cambiarNotaTxt=Entry(ventanaCambiar,width=21)
    cambiarNotaTxt.place(x=200,y=11)
    botoncambiarNota=Button(ventanaCambiar,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
    botoncambiarNota.place(x=0,y=40)
        
    ventanaCambiar.mainloop()

#funciones promedio y cantidad mayor
def promedioCalc():
    global tot
    sumNum=float(0)
    cant=float(0)
    for num in listaNotas:
        sumNum+=num
        cant+=1
    tot=round(sumNum/cant,2)
    messagebox.showinfo(title="Promedio",message=(f"El promedio de nota en el curso es de {tot}"))

def numMaxProm():
    global tot
    x=0
    for num in listaNotas:
        if num>tot:
            x+=1
    messagebox.showinfo(title="Advertencia",message=(f"El numero de alumnos con notas mayores al promedio son {x}"))

#label estudiantes y notass
est1=Label(ventana, text="Estudiante 1:", font=("Arial",12), fg="black")
est1.place(x=520,y=90)
est2=Label(ventana, text="Estudiante 2:", font=("Arial",12), fg="black")
est2.place(x=520,y=120)
est3=Label(ventana, text="Estudiante 3:", font=("Arial",12), fg="black")
est3.place(x=520,y=150)
est4=Label(ventana, text="Estudiante 4:", font=("Arial",12), fg="black")
est4.place(x=520,y=180)
est5=Label(ventana, text="Estudiante 5:", font=("Arial",12), fg="black")
est5.place(x=520,y=210)
est6=Label(ventana, text="Estudiante 6:", font=("Arial",12), fg="black")
est6.place(x=520,y=240)
est7=Label(ventana, text="Estudiante 7:", font=("Arial",12), fg="black")
est7.place(x=520,y=270)
est8=Label(ventana, text="Estudiante 8:", font=("Arial",12), fg="black")
est8.place(x=520,y=300)
est9=Label(ventana, text="Estudiante 9:", font=("Arial",12), fg="black")
est9.place(x=520,y=330)
est10=Label(ventana, text="Estudiante 10:", font=("Arial",12), fg="black")
est10.place(x=520,y=360)
est11=Label(ventana, text="Estudiante 11:", font=("Arial",12), fg="black")
est11.place(x=520,y=390)
est12=Label(ventana, text="Estudiante 12:", font=("Arial",12), fg="black")
est12.place(x=520,y=420)

not1=Label(ventana, text=listaNotas[0], font=("Arial",12), fg="black")
not1.place(x=650,y=90)
not2=Label(ventana, text=listaNotas[1], font=("Arial",12), fg="black")
not2.place(x=650,y=120)
not3=Label(ventana, text=listaNotas[2], font=("Arial",12), fg="black")
not3.place(x=650,y=150)
not4=Label(ventana, text=listaNotas[3], font=("Arial",12), fg="black")
not4.place(x=650,y=180)
not5=Label(ventana, text=listaNotas[4], font=("Arial",12), fg="black")
not5.place(x=650,y=210)
not6=Label(ventana, text=listaNotas[5], font=("Arial",12), fg="black")
not6.place(x=650,y=240)
not7=Label(ventana, text=listaNotas[6], font=("Arial",12), fg="black")
not7.place(x=650,y=270)
not8=Label(ventana, text=listaNotas[7], font=("Arial",12), fg="black")
not8.place(x=650,y=300)
not9=Label(ventana, text=listaNotas[8], font=("Arial",12), fg="black")
not9.place(x=650,y=330)
not10=Label(ventana, text=listaNotas[9], font=("Arial",12), fg="black")
not10.place(x=650,y=360)
not11=Label(ventana, text=listaNotas[10], font=("Arial",12), fg="black")
not11.place(x=650,y=390)
not12=Label(ventana, text=listaNotas[11], font=("Arial",12), fg="black")
not12.place(x=650,y=420)

#botones cambiar
cambiarNota1=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar1)
cambiarNota1.place(x=700,y=85)
cambiarNota2=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar2)
cambiarNota2.place(x=700,y=115)
cambiarNota3=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar3)
cambiarNota3.place(x=700,y=145)
cambiarNota4=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar4)
cambiarNota4.place(x=700,y=175)
cambiarNota5=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar5)
cambiarNota5.place(x=700,y=205)
cambiarNota6=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar6)
cambiarNota6.place(x=700,y=235)
cambiarNota7=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar7)
cambiarNota7.place(x=700,y=265)
cambiarNota8=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar8)
cambiarNota8.place(x=700,y=295)
cambiarNota9=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar9)
cambiarNota9.place(x=700,y=325)
cambiarNota10=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar10)
cambiarNota10.place(x=700,y=355)
cambiarNota11=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar11)
cambiarNota11.place(x=700,y=385)
cambiarNota12=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=10,height=1, command=cambiar12)
cambiarNota12.place(x=700,y=415)

#botones promedio y cantidad mayor
promedio=Button(ventana,text="Promedio", font=("Times New Roman",12),width=40,height=1, command=promedioCalc)
promedio.place(x=10,y=480)
numMayorProm=Button(ventana,text="Numero Mayor al Promedio", font=("Times New Roman",12),width=40,height=1, command=numMaxProm)
numMayorProm.place(x=425,y=480)

ventana.mainloop()
