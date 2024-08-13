class Habitacion:
    def __init__ (self, numero, capacidad, tarifaPorNoche):
        self.numero=numero
        self.capacidad=capacidad
        self.tarifaPorNoche=tarifaPorNoche

        self.ocupada=False



    def getNumero(self):
        return self.numero

    def getCapacidad(self):
        return self.capacidad
    
    def getTarifaPorNoche(self):
        return self.tarifaPorNoche
    
    def estaOcupada(self):
        return self.ocupada


    
    def ocuparHabitacion(self):
        self.ocupada=True


    def desocuparHabitacion(self):
        self.ocupada=False



