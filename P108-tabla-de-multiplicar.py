# Ejemplificar el uso de una funcion para con 2 parametros
import os
def tabla(t, n):
    for i in range(1, n + 1):
        print(f'{t} x {i} = {t * i}')
os.system('cls')
print('Imprimiendo la tabla de multiplicar que tu deseas')
t = int(input('que tabla: '))
n = int(input('hasta que numero: '))
# Invocando la funcion con 2 parametros
tabla(t, n)
