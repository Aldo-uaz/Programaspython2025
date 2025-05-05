# Procesar cleintes y pruductos en un diccionario
# Calcualr el subtotal de casa cliente en otro diccionario

import os; os.system('cls')

compras = [
    {'Cliente':'Juan','Producto':'pinzas','Cantidad':3,'Precio':250.55},
    {'Cliente':'Juan','Producto':'martillo','Cantidad':3,'Precio':95.32},
    {'Cliente':'Pedro','Producto':'pinzas','Cantidad':6,'Precio':250.55},
]
n = int(input('Cuantas compras mas deseas agregar: '))
for c in range(1, n+1):
    print(f'\nCompra {n}')
    compra={
        'Cliente': input('Nombre: '),
        'Producto': input('Producto: '),
        'Cantidad': int(input('Cantidad: ')),
        'Precio' :float(input('Precio: '))
    }
    compras.append(compra)
#calculo subtotales por cada cliente
clientes = {}
for compra in compras:
    cliente = compra['Cliente']
    if cliente not in clientes:
        clientes[cliente]= {'Cantidad':0,'subtotal':0}
    clientes[cliente]['Cantidad'] += compra['Cantidad']
    clientes[cliente]['subtotal'] += compra['Cantidad'] * compra['Precio']
# imprime los subtotales de cada cliente
print(f'Clientes: {clientes} - {len(clientes)}')
for cliente, datos in clientes.items():
    print('Cliente: ',cliente)
    print(f'Cantidad: {datos['Cantidad']:.2f}')
    print(f'subtotal: {datos['subtotal']:.2f}')
