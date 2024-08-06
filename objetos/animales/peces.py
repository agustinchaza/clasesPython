from animal import *


class pez(animal):
    def __init__(self, nombre, edad, ojos, color, cantidadAletas):
        super().__init__(nombre, edad, ojos)
        self.color = color
        self.cantidadAletas = cantidadAletas

    def nadar(self):
        print(f"{self.nombre} esta nadando")
    
    