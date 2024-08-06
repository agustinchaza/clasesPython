def suma_digitos(n):
    # Caso base: Si el número es 0, la suma de sus dígitos es 0
    if n == 0:
        return 0
    else:
        # Llamada recursiva: Sumamos el último dígito al resultado de la función con el número dividido por 10
        
        rta= n % 10 + suma_digitos(n // 10)
        return rta

# Ejemplo de uso
numero = 1234



resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}")
