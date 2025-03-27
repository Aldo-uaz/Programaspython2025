#El usuario introducira los numeros y se sacara el promedio y la suma de los numeros, se termina de tomar numero cuando el
#usuario ponga 0

import os; os.system('cls')

c = s = 0
while(True):
    while(True):
        num = int(input('Dame un numero:  '))
        if num == 0:
            break
        else:
            c += 1
            s += num
            p = s/c
    print(f'se introdujeron {c} numeros')
    print(f'La suma es:  {s}')
    print(f'El promedio es: {p}')
    if input('Deseas continuar (S/N)').upper()=='N':break
print('Proceso terminado')