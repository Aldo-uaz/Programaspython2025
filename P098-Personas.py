# Reapaso de los conjuntos

import  os; os.system('cls')
A = {'Juan','Maria','Pedro','Jose','Rocio'}
B = {'Pedro','Juan','Pablo','Mateo','Esther'}
print(f'Conjunto de Personas A: {A} - {len(A)}  ')
print(f'Conjunto de Personas B: {B} - {len(B)}  ')

print('Union de los conjuntos')
print(f'A U B: {A.union(B)}')

print('Interseccion de los conjuntos')
print(f'A & B: {A.intersection(B)}')

print('Diferencia de los conjuntos')
print(f'A - B: {A.difference(B)}')

print('Diferencia simetrica entre los conjuntos')
print(f'A ^ B: {A.symmetric_difference(B)}')

print('si el conjunto de nombres Pablo, Mateo, es subconjunto de B:', {'Pablo','Mateo'}.issubset(B))

print('si el conjunto A, es superconjunto del conjunto de nombres: Reynaldo, Angelica:', A.issuperset({'Reynaldo','Angelica'}))
print('Verificando si Pedro esta en A')
print(f'Pedro en A: {'Pedro' in A}')
print('Verificando si Lilia no esta en B')
print(f'Lilia en B: {'Lilia' in B}')



