# numeroes del 1 al 100 usando ciclo for

import os ; os.system('cls')

x= int(input('Hasta donde: '))
i= int(input('incremento: '))

for n in range(0,x + 1,i):
    print(n, end= ' ')
print('\nLlegamos al final')