# se imprime numeros del 1 a n de 10 en 10

import os ; os.system('cls')

x= int(input('Dame un numero: '))
i= 10

for n in range(1,x + 1,i):
    print(n, end= ' ')
print('\nLlegamos al final')