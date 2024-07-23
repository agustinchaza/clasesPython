import tkinter as tk  
import random

class juego():
    def __init__(self):
        self.setNumero()
    
    def setNumero(self):
        self.numero = random.randint(0, 1000)
        
    def intentar(self):
        ingresado = int(intento.get())
        
        if ingresado == self.numero:
            respuesta.set("¡GANASTE!... intentalo de nuevo :)")
            self.setNumero()
        elif ingresado < self.numero:
            respuesta.set("El número buscado es mayor")
        elif ingresado > self.numero:
            respuesta.set("El número buscado es menor")

# Instancia de la clase 'juego'
juego1 = juego()

# Creación de la ventana principal
pantalla = tk.Tk()

# Estilo para la ventana
pantalla.title("Juego de Adivinar Número")
#pantalla.geometry("300x200")
pantalla.configure(bg="#222222")  # Fondo muy oscuro

# Variables de control para los widgets
intento = tk.StringVar()
respuesta = tk.StringVar()

# Crear un marco para organizar los widgets
marco = tk.Frame(pantalla, bg="#222222")  # Fondo muy oscuro
marco.pack()

# Etiqueta para las instrucciones
texto = tk.Label(marco, text="Intenta adivinar un número", bg="#222222", fg="white", font=("Comic Sans MS", 12))
texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Campo de entrada
campoEntrada = tk.Entry(marco, textvariable=intento, justify="center",bg="white", fg="black", font=("Comic Sans MS", 10))  # Contraste con el fondo oscuro
campoEntrada.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón
boton = tk.Button(marco, text="Ingresar número", command=juego1.intentar, bg="green", fg="white", font=("Comic Sans MS", 10, "bold"))
boton.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Campo de respuesta
campoRespuesta = tk.Entry(marco, textvariable=respuesta, justify="center",state="disabled", width=50, bg="#222222", fg="red", font=("Comic Sans MS", 10, "italic"))
campoRespuesta.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
pantalla.mainloop()