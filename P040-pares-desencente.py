# Imprime los numerso pares desde 100 hasta n, tambien suma los numeros, el proceso termina hasta que el usuario desea terminar


while(True):
    import os ; os.system('cls')
    print('Imprime los numeros del 100 al numero que quieres que termine el conteo')
    n=int(input('Dame un numero menor a 100:  '))
    i=100
    c=100
    while i>=n:
        print(i ,end = ' ')
        i-=2   
        c+=i
    print(i ,end = ' ')
    print(f'\nLa suma es igual a: {c}' )
    if input('Deseas continuar (S/N)').upper()=='N':break
print('Proceso terminado')
      