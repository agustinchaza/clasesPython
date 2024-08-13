from Habitacion import *
import os


class Hotel:
    def __init__(self, nombre, direccion, habitaciones, servicios):
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = habitaciones # Lista
        self.servicios = servicios

    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getHabitaciones(self):
        return self.habitaciones

    def getServicios(self):
        return self.servicios

    def setNombre (self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def setHabitaciones(self, habitaciones):
        self.habitaciones = habitaciones
    
    def setServicios(self, servicios):
        self.servicios = servicios


    def imporimirInformacion(self):
        print(f"Hotel: {self.nombre}, Dirección: {self.direccion}")
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.estaOcupada():
                pass
            else:
                print(f"Habitación {habitacion.getNumero()}, Capacidad: {habitacion.getCapacidad()}, Tarifa por noche: {habitacion.getTarifaPorNoche()}")

    def reservarHabitacion (self,nro):
        reservaExitosa=False 
        for habitacion in self.habitaciones:
            if habitacion.getNumero()==nro and not (habitacion.estaOcupada()):
                reservaExitosa=True
                habitacion.ocuparHabitacion()
                print(f"La habitación {nro} ha sido reservada.")
        if not reservaExitosa:
            print(f"La habitación {nro} no existe o está ocupada.")

    def liberarHabitacion(self, nro):
        liberacionExitosa=False
        for habitacion in habitaciones:
            if habitacion.getNumero()==nro and habitacion.estaOcupada():
                habitacion.desocuparHabitacion()
                liberacionExitosa=True  # Marca como liberada la habitación.
                print(f"La habitación {nro} ha sido liberada.")
        if not liberacionExitosa:
            print(f"La habitación {nro} no existe o no está ocupada.")


habitaciones=[
    Habitacion(101, 2, 100),
    Habitacion(102, 3, 150),
    Habitacion(103, 3, 150)  #, Habitacion(4, 5, 250) # Añadimos más habitaciones si es necesario.
]

Sanaez=Hotel("Sanaez", "Calle falsa 123", habitaciones, "Servicios: desayuno y cochera")


while True:
    print("\nMenú del hotel:")
    print("1. Imprimir información del hotel")
    print("2. Reservar habitación")
    print("3. Liberar habitación")
    print("4. Salir")

    opcion=int(input("ingrese el numero de la accion a realizar: "))


    os.system("clear")

    if opcion == 1:
        Sanaez.imporimirInformacion()


    if opcion == 2:
        habitacion=int(input("Ingerse el numero de habitacion a reservar: "))
        Sanaez.reservarHabitacion(habitacion)

    if opcion == 3:
        habitacion=int(input("Ingrese el numero de habitacion a liberar: "))
        Sanaez.liberarHabitacion(habitacion)

    if opcion == 4:
        break


