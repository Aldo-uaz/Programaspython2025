# Verificar la suma de tres numeros enteros si el resultado es igual a alguno de los otros

import os; os.system('celar')

print('Dame 3 numeros enteros separados por <enter> ')
n1, n2, n3 = int(input()),int(input()),int(input())

if n1 + n2 == n3:
    print('{n1} + {n2} = {n3}')
elif n1 + n3 == n2:
    print('{n1} + {n3} = {n2}')
elif n2 + n3 == n1:
    print('{n2} + {n3} = {n1}')
else:
    print('Problablemente son iguales')