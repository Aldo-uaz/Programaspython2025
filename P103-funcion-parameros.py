# Ejemplificar el uso de una funcion que recibe mas de un parametro
import os
def saluda(apaterno,nombre, edad):
    print(f"Hola {nombre} {apaterno}, tienes una edad de {edad} años")

os.system('cls')
print('Invocando la funcion con mas de un parametro')
# Invocando la funcion con 3 parametros
saluda('Castañeda','Carlos', 25)
# saluda('Soto') # # Error, no se le pasaron los 3 parametros
# saluda('Soto','Rocio',34,35) # Error, se pasaron 4 parametros
saluda('Bernal','Teresa', 45)