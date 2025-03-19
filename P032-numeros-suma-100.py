# Suma numeros hasta dar 100

import os; os.system('clear')
s = 0 
c = 0
while c < 200:
    c += 1
    s += c
    print(c, end=' ')
    if s >= 15000:
        print("\n")
        break
else:
    print('\n Llegamos a la meta')

print(f'Suma {s}, numero sumados para alcanzar la meta {c}')