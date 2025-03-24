# tabla de conversion de peso a dolar en un rano de valores

import os; os.system('clear')

while(True):
    tc =20.50 ; tl=25.97
    print('Tabla de conversion de peso a dolar \n')
    pi=float(input('Valor inicial:  '))
    pf=float(input('Valor final:  '))
    c= pi
    print('\n Peso \t Dolar \tLibra')
    print('-'*15)
    while c <= pf:
        print(f'{c} \t{c/tc:.2f} \t{c/tl:.2f}')
        c += 1
    if input('Deseas contunial (S/N)').upper()== 'N': break
print('Proceso Terminado')
