class persona:
    def __init__ (self, nombre, edad, genero, nacionalidad, ContraseñaBancaria):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.nacionalidad=nacionalidad
        self.mayorDeEdad=edad>18
        self.__ContraseñaBancaria=ContraseñaBancaria

    def saludar(self):
        print("Hola, mi nombre es: ",self.nombre)
    # ejercio 1: funcion cumplir años
    def cumple (self):
        self.edad +=1

    def __str__(self):
        return f"objeto tipo persona: nombre = {self.nombre}, edad = {self.edad}, genero = {self.genero}, nacionalidad = {self.nacionalidad}"
    
    def __del__(self):
        print(f"{self.nombre} is dead")

class alumno(persona):
    def __init__(self, nombre, edad, genero, nacionalidad, carrera):
        super().__init__(nombre,edad,genero,nacionalidad,000)
        self.carrera=carrera

    




persona1=persona("pepito",21,"Masculino","Argentino", 123)

alumno1=alumno("roberta", 22, "Femenino", "Brasil", "pasteleria")

alumno1.saludar()

print(persona1.__ContraseñaBancaria)





