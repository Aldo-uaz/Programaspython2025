# Convertir temperatura de farenheit a centigrados y viceversa

import os; os.system('clear')
print('Convertir temperatura de farenheit a centigrados y viceversa')
print('De Centigrados a farenheit .......[1]')
print('De farenheit a Centigrados.......[2]')
op = int(input('elige ?'))
if op==1:
    print('Convitiendo de centigrados a farenheit .......')
    temp = float(input('Grados centigrados ? '))
    res= (temp * 9/5) + 32
    print(f'{temp} grados centigrados, equivale a {res} grados farenheit ')
else: 
    print('Convitiendo de farenheit a centigrados .......')
    temp = float(input('Grados farenheit ? '))
    res= (temp - 32) * 5/9
    print(f'{temp} grados farenheit, equivale a {res} grados centigrados ')