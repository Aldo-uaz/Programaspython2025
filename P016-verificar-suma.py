# Verificar si la suma de dos numeros enteros es igual a un tercero

import os; os.system('clear')
print('Verificar si la suma de dos numero enteros es igual a un tercero')

print('Dame 3 numeros enteros separados por <enter> ')
n1, n2, n3 = int(input()),int(input()),int(input())

if n1 + n2 == n3:
    print('\n La suma de los dos primeros numero es igual al tercero \n')
else:
    print('\n La suma de los dos primeros numeros es diferente al tercer numero \n')

print('\n Gracias por ultilizar este programa')