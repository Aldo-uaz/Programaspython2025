# Se desea calcualr la suma de los numeros introducidos por el usuario hasta que la suma sea >=200, luego mostrar cuantos numeros
#fueron introducidos y la suma de estos

import os; os.system('cls')
while(True):
    f=200
    c = s = 0
    while s <= f:
        num = int(input('Dame un numero:  '))
        c += 1
        s += num
    print(f'se introdujeron {c} numeros')
    print(f'La suma es:  {s}')
    if input('Deseas iniciar de nuevo (S/N)').upper()=='N': break
print('Proceso terminado')