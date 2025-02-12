# Ejemplifica las operaciones matematicas basicas

import os; os.system('clear')

#datos de prueba
x= float(input('valor de x: '))
y= float(input('valor de y: '))


suma = x + y
resta = x - y
mult = x * y
div = x / y
res = x % y
pot = x ** y
dive = x // y

print(f'Suma : {suma} \n Resta: {resta} \n Multiplicacion: {mult} \n Division: {div}')
print(f'Residuo : {res} \n Potencia: {pot} \n Divicion entera: {dive} ')
