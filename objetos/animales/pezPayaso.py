from peces import *

class pezPayaso(pez):
    def __init__(self, nombre, edad):
        super().__init__( nombre, edad, 2, "Naranja", 2)
    


Nemo=pezPayaso("Nemo", 1)

print(Nemo.nombre)
print(Nemo.edad)
print(Nemo.ojos)
print(Nemo.color)
print(Nemo.cantidadAletas)

Nemo.nadar()