# Se imprime la secuencia de numeros mostrados el numero de renglones que el usuario desee

import os 
while(True):
    os.system('cls')
    n=int(input('Dame un numero: '))
    cn = ' '
    for i in range(1,n+1):
        for j in range(1,i + 1):
            print(j, end = ' ')
        print()
    if input('\nDeseas otra secuencia S/N? ').upper()=='N':break

print('\nHemos llegado al final..')
