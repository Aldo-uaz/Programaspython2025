# Imprimir un cuadro de caracteres

import os 
while(True):
    os.system('cls')
    n=int(input('Cuantos renglones: '))
    c=input('Que caracter deseas: ')
    for i in range(1,n+1):
        for j in range(1,i + 1):
            print(c, end = ' ')
        print()
    if input('\nDeseas otra figura S/N? ').upper()=='N':break

print('\nHemos llegado al final..')