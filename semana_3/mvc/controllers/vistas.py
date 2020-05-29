import web

class Visitas:
    def GET(self, nombre):
      try:
        cookie= web.cookies()
        visitas=0
        if nombre:
          web.setcookie("nombre",nombre,expires="",domain=None)
        else:
          nombre="NA"
          web.setcookie("nombre",nombre,expires="",domain=None)

        print(cookie)
        if cookie.get("visitas"):
          visitas=int(cookie.get("visitas"))
          print("hay "+str(visitas))
          visitas+=1
          web.setcookie("visitas",str(visitas),expires="",domain=None)
          return "visitas"+str(visitas)
        else:
          web.setcookie("visitas",str(1),expires="",domain=None)
          visitas=1
        return "visitas:" + str(visitas)+"Nombre:"+nombre
      except Exception as e:
        return 'Error'+ str(e.args)