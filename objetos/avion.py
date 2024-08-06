"""objeto avion

atributos
- destino
- origen
- fecha de salida
- lista de asientos ocupados con su respectivo pasajero
- capacidad máxima de pasajeros


metodos
- alta_pasajero(nombre)
- baja_pasajero(nombre)"""
class Avion:
    def __init__(self, destino, origen, fecha_salida, capacidad_maxima):
        self.destino = destino
        self.origen = origen
        self.fecha_salida = fecha_salida
        self.capacidad_maxima = capacidad_maxima
        self.listaPasajeros =[]


    def alta_pasajero(self, nombre):
        if len(self.listaPasajeros)== self.capacidad_maxima:
            return "No queda espacio en el avion"
        else:
            self.listaPasajeros.append(nombre)
            return "se cargo el pasaje con exito"
    
    def baja_pasajero(self, nombre):
        self.listaPasajeros.remove(nombre)



# Prueba
avion=Avion("Bs As", "cordoba", "mañana", 3)

avion.alta_pasajero("Lautaro")
avion.alta_pasajero("Fernando")
avion.alta_pasajero("Paula")
avion.alta_pasajero("Ana")

avion.baja_pasajero("Paula")



print(avion.listaPasajeros)



