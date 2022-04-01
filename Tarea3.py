'''Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:'''
print('Suma del 0 al 100')
suma = 0
for i in range (0,101):
    if i%2==0:
        suma += i
print(suma)