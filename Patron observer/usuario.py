from observer import *

class CanalYoutube(Observado):
    def __init__(self, nombre):
        super().__init__()
        self.nombre=nombre
        self.videos=[]

    def agregarVideo(self, video):
        self.videos.append(video)
        self.notificarSuscriptores(f"Se agregó un nuevo video: {video}")

        





class usuario(Suscriptor):
    def __init__(self, nombre, contraseña, edad):
        self.nombre=nombre
        self.__contraseña=contraseña
        self.edad=edad
        self.MayordeEdad=edad>18

    def clonar(self):
        return usuario(self.nombre, self.__contraseña, self.edad)

    def imprimirContraseña(self):
        print("Contraseña: ", self.__contraseña)




    #GETTER y SETTER

    def getEdad(self):
        return self.edad

    def getNombre(self):
        return self.nombre


    
    def setEdad(self, edad):
        self.edad=edad
        self.MayordeEdad=edad>18



Messi24=usuario("Messi24", 123456, 24)
# Esto no se puede hacer porque la contraseña es un campo privado
# clonFalso=usuario(usuario1.getNombre(), usuario1.__contraseña, usuario1.getEdad())

Rubius=CanalYoutube("El Rubius")

Rubius.agregarSuscriptor(Messi24)
Rubius.agregarVideo("El video de Messi en el canal")

