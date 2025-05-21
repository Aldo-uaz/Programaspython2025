# Ejemplificar el uso de una funcion que recibe varios parametros
import os
def cuadro(r,c,car): # renglones, columnas, caracter
    for i in range(1 + r+1): # renglones de 1 a r
        for j in range(1 + c+1): # columnas de 1 a c
            print(car, end=' ') # imprime el caracter
        print()
os.system('cls')
print('Imprimiendo un cuadro de r * c del caracter que tu deseas')
r = int(input('Renglones: '))
c = int(input('Columnas: '))
car = input('Caracter: ')
cuadro(r,c,car)