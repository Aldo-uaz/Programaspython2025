# Suma el rango de numeros enteros consecutivos con una funcion

import os

def suma_rango(inicio, fin):
    s = 0
    for i in range(inicio, fin + 1):
        s = s + i
    return s
os.system('cls')
print('Dame el rango de numeros enteros consecutivos y te retorno la suma')
inicio = int(input('Inicio: '))
fin = int(input('Fin: '))
print('La suma del rango es: ', suma_rango(inicio, fin))
