# Ejemplificar el uso de parametros en funciones

import os
def saludo(nombre):
    print(f"Hola {nombre}, bienvenido a las funcines en Python, tu nombre tiene {len(nombre)} letras")

os.system('cls')
print('mandado saludos desde la funcion')
saludo('Caarlos Castañeda')
saludo('Rocio Soto')
saludo('Teresa Bernal')
print('---')
for s in range(5):
    saludo(str(s)*5)
print('---')
nombres =['Hugo','Paco','Luis','Carlos','Rocio','Teresa']
for nombre in nombres:
    saludo(nombre)