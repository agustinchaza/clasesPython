class animal:
    def __init__(self, nombre, edad, ojos ):
        self.nombre = nombre
        self.edad = edad
        self.ojos = ojos
        self.energia=100
        
    def comer(self, comida):
        self.energia+= comida.energia
        cemida.__del__()
