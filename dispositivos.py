class dispositivo:
    nombre =''
    lugar =''
    numero =''
    estado =False
    def __init__(self, nombre, lugar, numero, estado):
        self.nombre = nombre
        self.lugar = lugar
        self.numero = numero
        self.estado = estado
    def incender(self, estado):
        if self.estado == False:
            estado = True
    def apagar(self, estado):
        if self.estado == True:
            estado = False