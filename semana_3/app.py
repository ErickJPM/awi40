import web

urls = (
    '/(.*)', 'mvc.controllers.vistas.Visitas'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()