class dispositivo:
    nombre =''
    estado =False
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado
    def incender(self, estado):
        if self.estado == False:
            estado = True
    def apagar(self, estado):
        if self.estado == True:
            estado = False