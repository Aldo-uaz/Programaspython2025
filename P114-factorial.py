# Calcula el factorial de un número entero positivo n.

import os

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

os.system('cls')
print('Dame un numero entero positivo')
n = int(input('n: '))
while n < 0:
    print('El numero debe ser positivo')
    n = int(input('n: '))
# se invoca la funcion con un parametro
f = factorial(n)
print(f'El factorial de {n} es: {f}')
# El factorial de un número n es el producto de todos los números enteros positivos desde 1 hasta n.
