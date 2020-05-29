import web
import time
from datetime import date
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
        today = date.today()
        #Fecha actual
        now = datetime.now())
        print(today)
        print(now)
        if cookie.get("visitas"):
          visitas=int(cookie.get("visitas"))
          print("hay "+str(visitas))
          visitas+=1
          web.setcookie("visitas",str(visitas),expires="",domain=None)
        else:
          web.setcookie("visitas",str(1),expires="",domain=None)
          visitas=1

        return "visitas:" + str(visitas)+"   Nombre:"+nombre
      except Exception as e:
        return 'Error'+ str(e.args)