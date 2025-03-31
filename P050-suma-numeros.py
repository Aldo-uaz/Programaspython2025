#Suma de n numeros, introducidos por el usuario usando ciclo for

import os

while(True):
    os.system('cls')
    cuantos = int(input('Cuantas calificaciones deseas procesar: '))
    suma = 0
    cadnum = " "

    for i in range(1,cuantos+1):
        n= int(input(f'Calificacion [{i}] = '))
        suma +=n
        cadnum += str(n) + ' '

    print(f'Los numeros que introdujeron fueron: {cadnum}')
    print(f'La suma es: {suma}, el promedio es: {suma/cuantos}')


    if(input('\nDeseas continuar? (S/N) ')).upper()=='N':break

print('\nHemos llegado al final..')