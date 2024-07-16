





def areaCuadrado(lado):
    return lado**2


def areaTriangulo(base, altura):
    return (base * altura) / 2

#funcion sin retorno
def saludar(nombre):
    print("Hola, mi nombre es: ", nombre)


print("el area de un cuadrado de lado 5 es : ",areaCuadrado(5))

print("el area de un cuadrado de lado 10 es : ",areaCuadrado(10))

print("el area de un cuadrado de lado 20 es : ",areaCuadrado(20))

x=saludar("Juan")
print(x)

# Ejercicios de funciones
# funcion suma resta mutiplicacion y division

def suma(a,b):
    suma= a + b
    return suma

valor1=5
valor2=10

print("la suma de ", valor1, " y ", valor2, " es: ", suma(valor1,valor2))

