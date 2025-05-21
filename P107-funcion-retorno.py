# Ejemplificando el uso de valores de retorno en una funcion
import os

def suma(n1, n2):
    s=n1 + n2
    return s

os.system('cls')
print('Invocando la funcion con 2 parametros y un valor de retorno')
# Invocando la funcion con 2 parametros
resultado = suma(10, 20) # Guardamos el resultado de la suma en una variable
print(f'El resultado de la suma es: {resultado}')

resultado = suma(1000, 2000) # Guardamos el resultado de la suma en una variable
print(f'El resultado de la suma es: {resultado}')

# el usuario ingresa los valores
print('Dame dos numeros enteros y te calculo la suma')
a,b= int(input()), int(input()) # leo los valores en variables que se llaman diferente a los parametros
print(f'La suma de {a} + {b} es: {suma(a,b)}') # no se guarda el resultado, solo se imprime
