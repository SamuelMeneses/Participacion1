# Crear un programa que genere una lista de números pares entre 1 y 100.

listauno = []
listados = []
for r in range(0,101):
    listauno.append(r)

for par in listauno:
    if par % 2 == 0:
        listados.append(par)

print (listados)