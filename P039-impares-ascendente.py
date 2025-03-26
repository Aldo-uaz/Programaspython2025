# Se impirira los numeros inpares de forma ascendente desde el 1 hasta el n

import os; os.system('Clear')

while(True):
    n= int(input('Hasata que numero quieres ? '))
    c = 0
    if c <= n:
        i = 1
        suma = 0
        print (f'Los numeros impares hasta {n} :')
        while i <= n:
            print(i, end =' ')
            suma += i
            i += 2
        print(f'\nLa suma de los numeros impares es: ', suma)
    if input('Deseas continuar (S/N) ?').upper() == 'N' : break
print('Proceso terminado')