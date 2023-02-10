#Escribir un programa que determine si un número dado es par o impar.

n = int(input("Ingrese el numero: "))

num = n % 2

if (num == 0):
    print(f"El numero {n} es par.")
else:
    print(f"El numero {n} es inpar.")