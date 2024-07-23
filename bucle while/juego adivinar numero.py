import random

numeroAleatorio = random.randint(0, 100)
numeroUsuario = None
vidas=5

while True:
    numeroUsuario = int(input("Ingrese un número: "))

    if numeroUsuario == numeroAleatorio:
        print("Felicidades, acertaste!")
    elif numeroUsuario < numeroAleatorio:
        print("El número ingresado es menor, intente nuevamente con un numero mas grande.")
    else:
        print("El número ingresado es mayor, intente nuevamente con un numero mas pequeño.")


