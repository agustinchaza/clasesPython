usuario="Agus123"
contraseña=12345
contraseñaIngresada=None

while contraseñaIngresada != contraseña:
    contraseñaIngresada =   int(input("Ingrese la contraseña: "))


print("Contraseña correcta")


## EJERCICIO
## PEDIR AL USUARIO QUE INGRESE UN NUMERO PAR 
## Mientras no ingrese un número par, mostrar un mensaje de error y pedir
## nuevamente

NUMERO_INGRESADO = int(input("Ingrese un número par: "))


while (NUMERO_INGRESADO % 2)!= 0:
    print("el numero era impar, intente nuevamente")
    NUMERO_INGRESADO = int(input("Ingrese un número par: "))

print("El número ingresado es par")


## PEDIR AL USUARIO QUE INGRESE UN NUMERO MAYOR A 
## 1000 Y MENOR A 10000  (OR)


