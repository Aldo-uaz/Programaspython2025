# Ejemplificando el uso de una funcion que recibe n parametros
import os

def saludatodos(*todos):
    print(f'Saluda para {todos}')
    print(f'\nTu eres un cliente especial: {todos[0]}')
    print(f'\nSaludos a todos los clientes de la tienda {' / '.join(todos)}')
    for nombre in todos:
        print(f'\n{nombre} es un placer contar con tu preferencia en esta tienda')
os.system('cls')
print('Invocando la funcion con n parametros')
saludatodos('Juan','Pedro','Luis','Gonzalo')