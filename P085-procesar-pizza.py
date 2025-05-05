# Procesar el pedido de una pizza con diferentes ingredientes

import os; os.system('cls')

ingredientes ={
    'T' : 1.50,
    'P' : 3.50,
    'C' : 3.74,
    'A' : 0.40
}

base = 15
subtotal = 0
total = 0
descuento = 0
pedido = input('Ingredientes (T)Tomate, (P)Peperoni,(C)Champiñones,(A)Aguacate: ').upper

for ingrediente in pedido:
    if ingrediente in ingredientes:
        subtotal = subtotal + ingredientes[ingrediente]
subtotal = subtotal + base
total = subtotal

if subtotal >= 20:
    descuento = subtotal*0.05

    total = subtotal - descuento
print(f'Los ingredientes que elegistes fueron:{pedido}')
print(f'El subtotal a pagar sin descuento es: {subtotal}')
print(f'El importe del descuento es:{descuento}')
print(f'Total a pagar es: {total}')