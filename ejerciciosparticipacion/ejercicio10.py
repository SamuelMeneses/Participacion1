# Escribir una función que calcule el factorial de un número dado

def factorial_de_num(numero):
    if numero < 0:
        print("Factorial de un numero negativo no existe")

    elif numero == 0:
        return 1

    else:
        factorial = 1
        while (numero > 1):
            factorial *= numero
            numero -= 1
        return factorial

numero = int(input("escriba su numero"))

print("el factorial de", numero, "es", factorial_de_num(numero))