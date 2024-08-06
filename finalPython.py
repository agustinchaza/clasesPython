class genero:
    # EJERCICIO 1 - (2 Pto.)
    # complete el constructor de la clase cancion
    def __init__(self, nombre, descripcion):
        # ----------- Comienza aqui --------------#
        
        pass
        
        # ----------- Termina aqui ---------------#
       
# EJERCICIO 2 - (1 Pto.)
# Modifique la siguiente clase para que subgenero tambien sea un genero
# (HEREDE de genero)   

# ----------- Comienza aqui --------------#
class subgenero:          
# ----------- Termina aqui ---------------#                    
    def setGeneroPadre(self, generoPadre):
        self.generoPadre=generoPadre
        
    def getGeneroPadre(self):
        return self.generoPadre    
    
    
class cancion:
    
    def __init__(self, nombre, artista, duracion, genero):
       self.nombre=nombre
       self.artista=artista
       self.duracion=duracion
       self.genero=genero    

    def getDuracion(self):
        return self.nombre
    
    def setDuracion(self, nombre):
        self.nombre = nombre


    # EJERCICIO 3 - (2 Pto.)
    # construya getter y setter para el atributo artista
       
       
    # ----------- Comienza aqui --------------#
        
        
        
    # ----------- Termina aqui ---------------#
    
    
class album:
    def __init__(self, artista, nombre, canciones):
        self.artista=artista
        self.nombre=nombre
        self.canciones=canciones # LISTA de canciones
        
    def duracionAlbum(self):
        # EJERCICIO 4 - (2.5 Pto.)
        # esta funcion DEVUELVE la suma de las duraciones 
        # de las canciones que componen el album
        
        # ----------- Comienza aqui --------------#
        
        pass
    
        # ----------- Termina aqui ---------------#
    
    def nroCanciones(self): 
        # EJERCICIO 5 - (1 Pto.)
        # esta funcion DEVUELVE la cantidad de
        # canciones que compone el album
        # SUGERENCIA: usar una de las funciones las listas vistas en clase
        
        # ----------- Comienza aqui --------------#
        
        pass
    
        # ----------- Termina aqui ---------------#
        



# Crear instancia de Genero para "rock"
rock = genero("Rock", "Género musical caracterizado por el uso de instrumentos eléctricos y una fuerte presencia rítmica.")

# Crear instancia de Subgenero para "indie rock"
indie_rock =None

#indie_rock = subgenero("Indie Rock", "Subgénero del rock que se caracteriza por su enfoque independiente y DIY.")
#indie_rock.generoPadre(rock)


# Lista para almacenar las canciones del álbum "AM" de Arctic Monkeys
canciones_AM = [
    #cancion("Nombre de la cancion", "nombre del artista", duracion, genero)
    
    cancion("Do I Wanna Know?", "Arctic Monkeys",    4.32, indie_rock),
    cancion("R U Mine?", "Arctic Monkeys",           3.21, indie_rock),
    cancion("One for the Road", "Arctic Monkeys",    3.26, indie_rock),
    cancion("Arabella", "Arctic Monkeys",            3.27, indie_rock),
    cancion("I Want It All", "Arctic Monkeys",       3.05, indie_rock),
    cancion("No. 1 Party Anthem", "Arctic Monkeys",  4.03, indie_rock),
    cancion("Mad Sounds", "Arctic Monkeys",          3.35, indie_rock),
    cancion("Fireside", "Arctic Monkeys",            3.01, indie_rock),
    cancion("Why'd You Only Call Me When You're High?", "Arctic Monkeys", 2.41, indie_rock),
    cancion("Snap Out of It", "Arctic Monkeys",      3.12, indie_rock),
    cancion("Knee Socks", "Arctic Monkeys",          4.17, indie_rock),
    cancion("I Wanna Be Yours", "Arctic Monkeys",    3.04, indie_rock)
]



# EJERCICIO 6 - (1.5 Pto.)
#construya el objeto album con los siguientes atributos:
#artista: "arctic monkeys"
# nombre: "AM"
#canciones: use la lista de canciones de arriba
 

# ----------- Comienza aqui --------------#
Album_AM= None
# ----------- Termina aqui ---------------#

#print(Album_AM.duracionAlbum())
#print(Album_AM.nroCanciones() )