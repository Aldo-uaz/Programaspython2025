# Calcular el factorial de m numero

import os;
os.system('cls')

print('Calcuala e imprime factorial de m numero')

m = int(input('Hasta que numero deseas el factorial: '))


for x in range(1, m + 1):

    f=1
    sec = ' '
    for i in range(1, x+1):
        f = f * i
        sec = sec + str(i)
        if i < x:
            sec = sec + ' * ' # ppara que no imprima el ultimo numero con * por eso se hace eso
    print(f'{x}! = {sec} = {f:,}')