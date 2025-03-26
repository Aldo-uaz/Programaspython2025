# Calculando el numero mayo de una serie de numeros intoducidos por el teclado
import os ; os.system('cls')
c = m = 0
while(True):
    num = int(input('Dame un numero:  '))
    if num == 0:
        break
    else: 
        c += 1
    if num < m:
        m == num

             
print(f'se introdujeron {c} numeros')
print(f'El numero mayor es:  {m}')


print('Gracias por usar este programa')