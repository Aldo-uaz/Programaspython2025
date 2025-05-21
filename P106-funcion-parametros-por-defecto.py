# Ejemplifica el uso de parámetros por defecto en una función

import os

def saluda(nombre='nadie', edad=0):
    print(f"Hola {nombre}, tienes una edad de {edad} años")

os.system('cls')
print('Invocando la funcion con n parametros')
# Invocando la funcion con 1 parametro
saluda('Carlos')
# Invocando la funcion sin pasarle ningun parametro
saluda()
# Invocando la funcion con 2 parametros 
saluda('Carlos', 25)

