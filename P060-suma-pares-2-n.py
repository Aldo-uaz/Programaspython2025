#suma pares de 2 en 2 hasta n

import os;

while(True):
    os.system('cls')
    print('Imprimir la suma de pares e impares en un rango de 1 a n')
    n = int(input('Dame el valor final: '))

    sp =  0
    cp = " "
    for i in range(1,n+1):
        if i % 2 == 0: #es par
            cp = cp + " " + str(i)
            sp= sp+i
    print(f'\nLos Pares : {cp}, La suma es = {sp}')




    if(input('\nDeseas continuar? (S/N) ')).upper()=='N':break

print('\nHemos llegado al final..')