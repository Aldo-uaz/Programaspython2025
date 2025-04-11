# Dado el numero del mes, se mostrara el mes y los dias que tiene ese mes

import os ; os.system('cls')

mes = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
pos = 0
print('Dado el numero del mes, se mostrara el mes y los dias que tiene ese mes')

while(True):
    n = int(input('Dame un numero del 0 al 11: '))
    if n > 0 and n <= 11:
        print(f'Elegiste el mes: {n}')
        print(f'El mes es: {mes[n]}, los dias totales del mes son: {dias[n]}')
    else: print('>(')

    if(input('\nDeseas continuar? (S/N) ')).upper()=='N':break

print('\nHemos llegado al final..')