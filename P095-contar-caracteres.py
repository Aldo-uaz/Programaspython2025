# Programa que cuenta la cantidad de apariciones de cada carácter en una cadena
import os; os.system('cls')
cadena = input("Introduce una cadena: ")
conteo = {}

for caracter in cadena:
    if caracter in conteo:
        conteo[caracter] += 1
    else:
        conteo[caracter] = 1

print("Conteo de caracteres:")
for caracter, cantidad in conteo.items():
    print(f"'{caracter}'-> {cantidad}")