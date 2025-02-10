# leer y mostrar datos.

print('leyendo datos del usuario, luego enviar un saludo :\n')

nombre = input('Dame tu nombre: ') # lee cadena
edad   = int(input('Dame tu edad: ')) # lee cadena y convierte a entero
peso   = float(input('Dame tu peso: ')) # lee una cadena y convierte un flotante
print('\n')

print(f'{nombre} Bienvenido al lenguaje Python, tu edad es {edad}, tu peso es {peso}')

print('\n')

print(type(nombre))
print(type(edad))
print(type(peso))
