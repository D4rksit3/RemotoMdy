import subprocess 
import os
from datetime import date
from datetime import datetime
import urllib, sys, socket
import pymysql

#Fecha actual
now = datetime.now()


#Datos IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("iplocation.com", 80))

ip_equipo = s.getsockname()[0]
nombre_equipo = socket.gethostname()

#Base de datos
db = pymysql.connect('localhost','root','','ipcc')
cursor = db.cursor()

#cursor1 = conect.cursor()
sql = f"INSERT INTO datos_maquina(ip,hostname,fecha) values ('{ip_equipo}','{nombre_equipo}','{now}')"
cursor.execute(sql)
db.commit()









ruta = 'ps'



#ip = input("Ingresar ip a remotear: ")
#ip = "192.168.1.39"
#user = "Administrador"
#password = "@C0l0n14l#"
#tarea = "taklist"
#kill = os.kill("notepad.exe")
#subprocess.run(["ls", "-l"])

subprocess.run("sudo.exe ps\\PsExec.exe \\\\192.168.1.39 -u administrador -p @C0l0n14l# -s cmd")
#os.system("ps\\PsExec.exe \\\\192.168.1.39 -u administrador -p @C0l0n14l# -s cmd tasklist")
#os.system("ps\\PsExec.exe \\\\192.168.1.39 -u administrador -p @C0l0n14l# tasklist")