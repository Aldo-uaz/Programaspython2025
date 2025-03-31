# imprimir numero de 1 a n o de n a 1
import os;

while(True):
    os.system('cls')
    print('Imprimir numeros usando ciclo for')
    print('[1] Imprimir numeros del 1 al n')
    print('[2] Imprimir numeros del n al 1')
    print('[3] Salir')
    op = int(input('Que opcion eliges: '))

    if op==1:
        print(f'Imprimir numeros del 1 al n')
        n = int(input('Hasta donde: '))
        for x in range(1, n+1, 1): print(x, end=' ')
    if op==2:
        print(f'Imprimir numeros del n al 1')
        n = int(input('Desde donde: '))
        for x in range(n, 0, -1): print(x, end=' ')
    if op==3:
        print(f'Te vamos a extrañar'); break
    else:
        print(f'OPCION NO VALIDA')

    if(input('Deseas continuar? (S/N) ')).upper()=='N':break

print('\nHemos llegado al final..')