import web
from datetime import date
from datetime import time
from datetime import datetime
class Visitas:
  def GET(self, nombre):
    cookie= web.cookies()
    visitas=0
    if nombre:
      web.setcookie("nombre",nombre,expires="",domain=None)
    else:
      nombre="anonimo"
      web.setcookie("nombre",nombre,expires="",domain=None)
    print(cookie)
    if cookie.get("visitas"):
      visitas=int(cookie.get("visitas"))
      visitas+=1
      web.setcookie("visitas",str(visitas),expires="",domain=None)
    else:
      web.setcookie("visitas",str(1),expires="",domain=None)
      visitas=1
    now = datetime.now()
    fecha=now.date()
    print(fecha)
    web.setcookie("fecha",str(fecha),expires="",domain=None)
    hora = datetime.time(datetime.now())
    print(hora)
    web.setcookie("hora",str(hora),expires="",domain=None)

    return "visitas:" + str(visitas)+"   Nombre:"+nombre+"\nFecha: "+str(fecha)+"    Hora: "+ str(hora)
