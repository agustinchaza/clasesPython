precios={
    "oreos": 500,
    "chocolates": 2000,
    "galletas": 1000,
    "pan": 500,
    "galletas de caramelo": 2000,
    "jamón y queso": 3000,
}

#iterar sobre clave y valor y del diccionario para imprimir los precios
"""for elemento, precio in precios.items()  :
    print(f"el {elemento} vale: ${precio}")
"""
#iterar solo sobre clave:

for elemento in precios :
    print(f"el {elemento} vale: ${precios[elemento]}")

