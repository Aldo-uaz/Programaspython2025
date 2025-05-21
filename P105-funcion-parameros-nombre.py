# Ejemplificando el uso de nombres en los parametros esto permite invocar a la funcion 
# con los para metros en orden deseado

import os

def saluda(apaterno, amaterno, nombre):
    print(f"Hola {apaterno} {amaterno} {nombre}, bienvenido a esta universidad")

os.system('cls')
print('Invocando la funcion con n parametros')
saluda('Castañeda', 'Ramirez', 'Carlos')
saluda('Carlos', 'Ramirez', 'Castañeda') # los parameros llegan en un orden incorrecto
# Invocando la funcion con los nombres de los parametros
saluda(nombre='Carlos', apaterno='Castañeda', amaterno='Ramirez')
