'''Realiza un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética:'''
a=int(input('Cuantos números desea ingresar?: '))
suma=0
for i in range(a):
    b= int(input('Ingrese un número '))
    suma+=b/a
print('El valor de la media aritmetica es: ',suma)

