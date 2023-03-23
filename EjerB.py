from tkinter import*
import tkinter as tk
import tkinter
from PIL import ImageTk,Image
from debugpy import configure

#Crear pa vantana principal
root= Tk()
contra= StringVar()
confir= StringVar()


def sesion():
    if contra.get()==confir.get():
        print("SESION INICIADA")
        ventana.configure(bg="green")
    else:
        print("CONTRASEÑA INCORRECTA")

#Frame principal
ventana= Frame(root,bg="#a0a0a0",width=580,height=580)
ventana.pack()
#Poner imagen
img = Image.open("ElBicho.JPG")
imagen = img.resize((198,286))
imagenP = ImageTk.PhotoImage(imagen)
Ponerimagen = Label(ventana, image=imagenP).grid(row=2,column=2)

#titlogin= Label(ventana,text="LOG IN",font=("Roboto",10)).grid(row=7,column=1)

#Crear Etiqueta del nombre y la entrada
nombre= Label(ventana,text="NOMBRE:",font=("Roboto",10)).grid(row=10,column=2)
nombreEN= Entry(ventana,font=("Roboto",10)).grid(row=11,column=2,padx=1,pady=5)
#Crear etiqueta d contraseña y la entrada
contr= Label(ventana,text="CONTRASEÑA:",font=("Roboto",10)).grid(row=13,column=2)
contrEN= Entry(ventana,textvariable=contra,show="*").grid(row=14,column=2,padx=1,pady=5)
#Confirmacion de contraseña
confirma= Label(ventana,text="CONFIRMA CONTRASEÑA:",font=("Roboto",10)).grid(row=16,column=2)
confirEN= Entry(ventana,textvariable=confir,show="*").grid(row=17,column=2,padx=8,pady=2)

esH= tk.Checkbutton(ventana,text='Masculino').grid(row=20,column=1,padx=1,pady=1)
esM= tk.Checkbutton(ventana,text='Femenino').grid(row=20,column=3,padx=1,pady=1)
acep= tk.Checkbutton(ventana, text="Acepto los términos y condiciones").grid(row=21,column=2)

boton1= Button(ventana,text="INICIAR",command=sesion).grid(row=24,column=2)

root.mainloop()