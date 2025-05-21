# Ejemplificar el uso de una funcion que recibe 3 parametros numericos
# y devuelve el mayor de ellos
import os

def mayor(c1, c2, c3):
    may = 0
    if c1 > c2 and c1 > c3:
        may = c1
    elif c2 > c1 and c2 > c3:
        may = c2
    else:
        may = c3
    return may
os.system('cls')
print('Dame 3 calificaciones y te dire cual es la mayor')
a , b , c = float(input('calificacion 1: ')), float(input('calificacion 2: ')), float(input('calificacion 3: '))
m = mayor(a, b, c)
if m == 0:
    print('No se ha podido determinar la calificacion mayor')
else:
    print(f'La calificacion mayor es: {m}')