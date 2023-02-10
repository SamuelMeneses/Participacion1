# Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.

textodelusuario = str(input("Ingrese una frase: "))

if (textodelusuario) == (textodelusuario)[::-1]:
    print("Si es un palindromo")

else:
    print("No es un palindromo")