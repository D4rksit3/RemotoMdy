import urllib.request as urllib
from datetime import date
from datetime import datetime
import urllib, sys, socket, time, os, subprocess 
import pymysql
import tkinter as tk
#from tkinter import *

#Fecha actual
now = datetime.now()

#ip publica
import sys
version = sys.version[0]

if version == '2':
  import urllib2 as urllib
else:
  import urllib.request as urllib

url1 = None
url2 = None
servidor1 = 'http://www.soporteweb.com'
servidor2 = 'http://www.ifconfig.me/ip'

consulta1 = urllib.build_opener()
consulta1.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')] 
consulta2=consulta1

try:
  url1 = consulta1.open(servidor1, timeout=17)
  respuesta1 = url1.read()
  if version == '3':
    try:
      respuesta1 = respuesta1.decode('UTF-8')
    except UnicodeDecodeError:
      respuesta1 = respuesta1.decode('ISO-8859-1')

  url1.close()
  #print('Servidor1:'+respuesta1)
  
except:
  #print('Falló la consulta ip a '+servidor1)
  pass


#Datos IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("iplocation.com", 80))

ip_publico = respuesta1

ip_equipo = s.getsockname()[0]

hostname = socket.gethostname()

#Base de datos
db = pymysql.connect('localhost','root','','ipcc')
cursor = db.cursor()

#cursor1 = conect.cursor()
def text(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)



def obtener_ip():
    ip_remoto = str(entrada1.get())
    sql = f"INSERT INTO datos_maquina(ip_equipo,ip_publico,ip_remoto,hostname,fecha) values('{ip_equipo}','{ip_publico}','{ip_remoto}','{hostname}','{now}')"
    cursor.execute(sql)
    db.commit()
    
    
    
    subprocess.run(f"sudo.exe ps\\PsExec.exe \\\\{ip_remoto} -u administrador -p @C0l0n14l# -s cmd")
    
    return var.set(ip_remoto)
def cerrar():
    ventana.destroy()
#Grafica
ventana = tk.Tk()
#ventana.iconbitmap("favicon.ico")
ventana.tk.call('wm','iconphoto', ventana._w, tk.PhotoImage(file='favicon.png'))
ventana.title("REPARADOR IPCC V3.0")
#Ancho por alto
ventana.geometry('400x250')
ventana.configure(background='dim gray')

var =tk.StringVar()
text = f"Conectado a {var}"

#Texto
etiqueta1=tk.Label(ventana, text=f"Ingrese IP: ",bg="black", fg="white")
etiqueta1.pack(padx=5,pady=4,ipady=5,fill=tk.X)

#Entrada
entrada1 = tk.Entry(ventana)
entrada1.pack(padx=5,pady=5,ipady=5,fill=tk.X)

#efecto


#Boton
boton = tk.Button(ventana,text="Conectar a IP",bg="black",fg="White",command=obtener_ip)
boton.pack(side=tk.LEFT,padx=30,pady=30,ipady=15)

boton_cerrar = tk.Button(ventana,text="Cerrar pestaña",bg="black",fg="White",command=cerrar)
boton_cerrar.pack(side=tk.RIGHT,padx=30,pady=30,ipady=15)



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