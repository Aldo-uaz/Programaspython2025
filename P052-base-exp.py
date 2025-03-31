# Dado un numero entero como base y un numero como exponente, calcuar la base elevado al exponente

import os; os.system('cls')

b = int(input('Base: '))
e = int(input('Exponente: '))
r = 1

for _ in range(e):
    r = r * b
print(f'{b}^{e} = {r}')