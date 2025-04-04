# Imprime la secuencia de numeros atomicos

import os; os.system('cls')

print('Imprime secuencia de numeros armonicos y su suma')

n = int(input('Cuantos terinos ? '))

s = 0
c = " "

for x in range(1, n + 1):
    f = 1 / x  
    s += f
    c += f'1/{x}!'
    if x < n:
            c = c + ' + '
print(f'{c} , suma: {s}')