import web

urls = (
    '/(.*)', 'mvc.controllers.control.hello'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()