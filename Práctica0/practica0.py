from tkinter import*
from cryptography.fernet import Fernet 
from tkinter import filedialog

#Varibales Globales
global nom_archivo
global clave
global nom_archivo2

#Generamos la clave
def GenerarClave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)

#Función para cifrar
def Cifrar():
    #Seleccionamos el archivo y lo guaramos
    nom_archivo = filedialog.askopenfilename()
    #Cargamos la clave
    clave = open("clave.key","rb").read()
    f = Fernet(clave)
    #Abrimos el archivo
    with open(nom_archivo,"rb") as file:
        archivo = file.read()
    #Ciframos el archivo
    MensajeC = f.encrypt(archivo)
    #Generamos otro archivo
    with open(nom_archivo[:-4] + "_c.txt",'wb') as f1:
        f1.write(MensajeC)

#Funcion para descifrar
def Descifrar():
    #Seleccionamos el archivo
    nom_archivo2 = filedialog.askopenfilename()
    #cargamos la clave
    clave = open("clave.key","rb").read()
    f = Fernet(clave)
    #Abrimos el archivo
    with open(nom_archivo2,"rb") as file:
        archivoE = file.read()
    #Desciframos
    MensajeD = f.decrypt(archivoE)
    with open(nom_archivo2[:-4] + "_d.txt",'wb') as f2:
        f2.write(MensajeD)


#Interfaz
raiz = Tk()
raiz.title("Practica 0 - Cifrar y descifrar")
raiz.geometry("265x260")
raiz.config(bg="white")

#Datos
label1= Label(raiz,text="\nC R Y P T O G R A P H Y\n")
label1.grid(row=3,column=4)
label1.config(bg="#800040",fg="white",font=("Verdana",10))

label2= Label(raiz,text="\nPRÁCTICA 0")
label2.grid(row=4,column=4)
label2.config(bg="white",font=("Verdana",8))

label3= Label(raiz,text="\nPérez Sereno Ricardo Erick")
label3.grid(row=5,column=4)
label3.config(bg="white",font=("Verdana",8))

label3= Label(raiz,text="\n 3CM17\n")
label3.grid(row=6,column=4)
label3.config(bg="white",font=("Verdana",9))

#Boton generar Clave
b1 = Button(raiz,text="Generar Clave",command=GenerarClave)
b1.grid(row=7,column=4)
b1.config(bg="black",fg="white")

#Boton cifrar
b3 = Button(raiz,text="Cifrar",command=Cifrar)
b3.grid(row=8,column=3)
b3.config(bg="black",fg="white")

#Boton Descifrar
b4 = Button(raiz,text="Descifrar",command=Descifrar)
b4.grid(row=8,column=5)
b4.config(bg="black",fg="white")



raiz.mainloop()