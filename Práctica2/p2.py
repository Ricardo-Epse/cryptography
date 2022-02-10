from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from PIL import Image
import numpy as np
import io



def obtenerModo(m):
	"""Función cuyo parámetro es la cadena de texto del modo y devuelve el modo en formato AES.MODE_XXX"""
	if m == "ECB": return AES.MODE_ECB
	elif m == "CBC": return AES.MODE_CBC
	elif m == "CFB": return AES.MODE_CFB
	elif m == "OFB": return AES.MODE_OFB
	else: return None


def cifrarECB(ubicacion, key, mode="",nonce=b"1234567890123456"):
	"""Función de descifrado requiere de la ubicación del archivo, la clave de 16 bytes, el modo de cifrado y el vector de inicialización (nonce, opcional para ECB)"""
	"""El vector de inicialización es 1234567890123456 por default si no se incluye en la llamada a la función"""
	# Abrir la imagen a cifrar, convertir para su cifrado y obteer su tamaño
	img = Image.open(ubicacion)
	imagen = np.array(img)
	size = img.size

	#Creación del cifrador según el modo
	if mode=="ECB":
		cipher = AES.new(key, obtenerModo(mode))
	elif mode=="CBC" or mode=="CFB" or mode=="OFB":
		cipher = AES.new(key, obtenerModo(mode), nonce)

	imgC = cipher.encrypt(pad(imagen.tobytes(),16))

	# Escribir nueva imagen cifrada
	cipherimage = Image.frombuffer("RGB", size, np.frombuffer(imgC))
	# Guardado del archivo cifrado con nuevo nombre
	cipherimage.save(ubicacion[:-4]+"_e"+mode+".bmp")


def descifrarECB(ubicacion, key, mode="", nonce=b"1234567890123456"):
	"""Función de descifrado requiere de la ubicación del archivo, la clave de 16 bytes, el modo de cifrado y el vector de inicialización (nonce, opcional para ECB)"""
	"""El vector de inicialización es 1234567890123456 por default si no se incluye en la llamada a la función"""
	# Abrir la imagen a cifrar, convertir para su descifrado y obtener su tamaño
	img = Image.open(ubicacion)
	imagen = np.array(img)
	size = img.size

	# Creación del cifrador según el modo
	if mode=="ECB":
		cipher = AES.new(key, obtenerModo(mode))
	elif mode=="CBC" or mode=="CFB" or mode=="OFB":
		cipher = AES.new(key, obtenerModo(mode), nonce)

	imgD = cipher.decrypt(imagen.tobytes())

	# Escribir nueva imagen descifrada
	plainimage = Image.frombuffer("RGB", size, np.frombuffer(imgD))
	# Guardado del archivo descrifrado con nuevo nombre
	plainimage.save(ubicacion[:-4]+"_d"+mode+".bmp")

def abrirArchivo():

	def ventana():
		global ubicacion
		ubicacion = filedialog.askopenfilename(title = "Abrir")
		lbl1 = Label(raiz, text = "Arhivo seleccionado:\n"+ubicacion)
		lbl1.grid(row=19,column=4)
	btn1 = Button(raiz, text="Abrir archivo", command = ventana, width=30)
	btn1.grid(row=18,column=4)

def cuadroCifrado():
	root = Tk()
	root.title("Archivo cifrado")
	root.geometry("300x100")
	lbl = Label(root, text = "Archivo cifrado :)")
	lbl.place(x=100, y=15)
	btn = Button(root, text="Aceptar", command=root.destroy)
	btn.place(x=125,y=50)
	root.mainloop()

def cuadroDescifrado():
	root = Tk()
	root.title("Archivo descifrado")
	root.geometry("300x100")
	lbl = Label(root, text = "Archivo descifrado :)")
	lbl.place(x=100, y=15)
	btn = Button(root, text="Aceptar", command=root.destroy)
	btn.place(x=125,y=50)
	root.mainloop()

def operaciones():
	if seleccion.get()==1:
		return "ECB"
	if seleccion.get()==2:
		return "CBC"
	if seleccion.get()==3:
		return "CFB"
	if seleccion.get()==4:
		return "OFB"

raiz = Tk()
raiz.title("Practica 2 - Cifrador por bloques")
raiz.geometry("265x600")
raiz.config(bg="white")
#Datos
label1= Label(raiz,text="\nC R Y P T O G R A P H Y\n")
label1.grid(row=3,column=4)
label1.config(bg="#800040",fg="white",font=("Verdana",10))

label2= Label(raiz,text="\nPRÁCTICA 2\n                  Cifrador por bloques                 ")
label2.grid(row=4,column=4)
label2.config(bg="white",font=("Verdana",8))

label3= Label(raiz,text="\nBello Muñoz Edgar Alejandro\nOrtiz Salazar Manuel Eduardo\nPérez Sereno Ricardo Erick")
label3.grid(row=5,column=4)
label3.config(bg="white",font=("Verdana",8))

label3= Label(raiz,text="\n 3CM17")
label3.grid(row=6,column=4)
label3.config(bg="white",font=("Verdana",9))


label3= Label(raiz,text="\n Elige el modo de operación")
label3.grid(row=9,column=4)
label3.config(bg="white",font=("Verdana",9))

seleccion = IntVar()
r3=Radiobutton(raiz,text="ECB",variable=seleccion,value=1)
r3.grid(row=10,column=4)
r4=Radiobutton(raiz,text="CBC",variable=seleccion,value=2)
r4.grid(row=11,column=4)
r5=Radiobutton(raiz,text="CFB",variable=seleccion,value=3)
r5.grid(row=12,column=4)
r6=Radiobutton(raiz,text="OFB",variable=seleccion,value=4)
r6.grid(row=13,column=4)

operaciones()



b1 = Button(raiz,text="Seleccionar Imagen",command=abrirArchivo)
b1.grid(row=18,column=4)
b1.config(bg="black",fg="white")

label6= Label(raiz,text="Key")
label6.grid(row=14,column=4)
label6.config(bg="white",fg="black")

key = Entry(raiz,text="key")
key.grid(row = 15, column = 4)
key.config(justify="center")

label7= Label(raiz,text="Vector de inicialización")
label7.grid(row=16,column=4)
label7.config(bg="white",fg="black")
vector = Entry(raiz, text = "vector")
vector.grid(row = 17, column = 4)
vector.config(justify="center")

# # Llamadas a las funciones (solo ejemplo, hacer desde la interfaz con la clave y vector del usuario)
# cifrarECB("Imagen1.bmp", b"sixteen byte key","ECB")
# descifrarECB("Imagen1_eECB.bmp", b"sixteen byte key", "ECB")

b1 = Button(raiz,text="Cifrar",command=lambda:[cifrarECB(ubicacion, bytes(key.get(), 'utf-8'),operaciones(),bytes(vector.get(), 'utf-8')),cuadroCifrado()])
b1.grid(row=22,column=4)
b1.config(bg="black",fg="white")

b2 = Button(raiz,text="Descifrar",command=lambda:[descifrarECB(ubicacion, bytes(key.get(), 'utf-8'),operaciones(),bytes(vector.get(), 'utf-8')),cuadroDescifrado()])
b2.grid(row=23,column=4)
b2.config(bg="black",fg="white")
raiz.mainloop()


#sixteen byte key
#1234567890123456