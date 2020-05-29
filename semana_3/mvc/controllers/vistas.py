import web
from datetime import date
from datetime import time
from datetime import datetime
class Visitas:
    def GET(self, nombre):
      try:
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
        fecha=datetime.date()
        web.setcookie("fecha",str(fecha),expires="",domain=None)
        t = datetime.time(datetime.now())
        print(t)

        return "visitas:" + str(visitas)+"   Nombre:"+nombre
      except Exception as e:
        return 'Error'+ str(e.args)