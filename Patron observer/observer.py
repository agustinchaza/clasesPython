class Observado:
    def __init__(self):
        self.subscriptores = []

    def agregarSuscriptor(self,subscriptor):
        self.subscriptores.append(subscriptor)

    def eliminarSuscriptor(self, subscriptor):
        self.subscriptores.remove(subscriptor)



    def notificarSuscriptores(self, informacion):
        for suscriptor in self.subscriptores:
            suscriptor.recibirNotificacion(informacion)

    

class Suscriptor:
    def __init__(self):
        pass

    def recibirNotificacion(self, informacion):
        print(f"Recibí el evento: {informacion}")




