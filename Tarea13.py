'''Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

Por ejemplo:

pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]
Nota: Para ordenar una lista automáticamente puedes usar el método .sort().

In [7]:'''
lista = [-12, 84, 13, 20, -33, 101, 9]
pares=[]
impares=[]
def separar():
    for i in lista:
        if i%2==0:
            pares.append(i)
            pares.sort()

        elif i%2==1:
            impares.append(i)
            impares.sort()
    print('la lista es: ',lista)
    print('Pares: ',pares)
    print('Impares: ',impares)
separar()

