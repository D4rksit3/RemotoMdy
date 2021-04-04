import subprocess 
import os
from datetime import date
from datetime import datetime
import urllib, sys, socket
import pymysql
import tkinter as tk
#from tkinter import *

#Fecha actual
now = datetime.now()


#Datos IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("iplocation.com", 80))

ip_equipo = s.getsockname()[0]
#nombre_equipo = os.system("wmic csproduct get name")
nombre_equipo = socket.gethostname()

#Base de datos
db = pymysql.connect('localhost','root','','ipcc')
cursor = db.cursor()

#cursor1 = conect.cursor()
sql = f"INSERT INTO datos_maquina(ip,hostname,fecha) values ('{ip_equipo}','{nombre_equipo}','{now}')"
cursor.execute(sql)
db.commit()

def obtener_ip():
    ip = str(entrada1.get())
    subprocess.run(f"sudo.exe ps\\PsExec.exe \\\\{ip} -u administrador -p @C0l0n14l# -s cmd")
    return var.set(ip)
def cerrar():
    ventana.destroy()
#Grafica
ventana = tk.Tk()
ventana.title("REPARADOR IPCC V3.0")
#Ancho por alto
ventana.geometry('400x250')
ventana.configure(background='dim gray')

var =tk.StringVar()
text = f"Conectado a {var}"

#Texto
etiqueta1=tk.Label(ventana, text="Ingrese IP:",bg="black", fg="white")
etiqueta1.pack(padx=5,pady=4,ipady=5,fill=tk.X)

#Entrada
entrada1 = tk.Entry(ventana)
entrada1.pack(padx=5,pady=5,ipady=5,fill=tk.X)

#efecto

#Boton
boton = tk.Button(ventana,text="Conectar",bg="black",fg="White",command=obtener_ip)
boton.pack(side=tk.TOP)



#efect = tk.Label(ventana,textvariable=var,padx="5",pady="5",width=50)
#efect.pack()


ventana.mainloop()

#ip = input("IP a conectarte: ")







#ip = input("Ingresar ip a remotear: ")
#ip = "192.168.1.39"
#user = "Administrador"
#password = "@C0l0n14l#"
#tarea = "taklist"
#kill = os.kill("notepad.exe")
#subprocess.run(["ls", "-l"])


#os.system("ps\\PsExec.exe \\\\192.168.1.39 -u administrador -p @C0l0n14l# -s cmd tasklist")
#os.system("ps\\PsExec.exe \\\\192.168.1.39 -u administrador -p @C0l0n14l# tasklist")