# Dados unos numeros calcualr y mostrar las difrentes operaciones de conjuntos
A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}
print('Conjunto A:', A)
print('Conjunto B:', B)
print('Conjunto C:', C)
print('Union de los conjuntos A y B')
print('A U B:', A.union(B))
print('Union de los conjuntos B y C')
print('B U C:', B.union(C))
print('Diferencia de los conjuntos A y C')
print('A - C:', A.difference(C))
print('Diferencia simetrica de los conjuntos B y C')
print('B ^ C:', B.symmetric_difference(C))
print('Interseccion de los conjuntos B y C')
print('B n C:', B.intersection(C))
print('A es subconjunto de B:', A.issubset(B))
print('C es superconjunto de A:', C.issuperset(A))
print('Verificando si 100 esta en A:', 100 in A)
print('Verificando si 60 esta en A, B y C:', 60 in A, B, C)
print('Verificando si 900 no esta en C:', 200 not in C)