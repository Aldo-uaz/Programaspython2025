# Solicitar al usuario que introduzca la cantidad de horas

print('Calcualndo los dias, minutos y segundos de las horas dadas por el usuario')

horas = int(input("Introduce la cantidad de horas como un numero entero: "))

dias = horas // 24
minutos = horas * 60
segundos = minutos * 60


print(f"Equivalente de las horas {horas} son:")
print(f"Equivalente en días: {dias} días")
print(f"Equivalente en minutos: {minutos} minutos")
print(f"Equivalente en segundos: {segundos} segundos")
