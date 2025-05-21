# sumar los digitos individualmente de un numero

import os

def sumadigitos(n):
    s = 0
    while n!= 0:
        dig = n % 10
        s = s + dig
        n = n // 10
    return s
os.system('cls')
n = int(input('Introduce un numero: '))
# se invoca la funcion con un parametro
s = sumadigitos(n)
print(f'La suma de los digitos invididuales de {n} es: {s}')