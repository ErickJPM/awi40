class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hola, ' + name + '!'