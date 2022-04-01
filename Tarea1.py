'''1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta.'''

print('Calculadora')
print('')
a=int(input('Ingrese el primer valor: '))
b=int(input('Ingrese el segundo valor: '))
print('')
print('Escoja la operacion que desee realizar')
print('1) Suma')
print('2) Resta')
print('3) Multiplicacion')
print('4) Division')
print('5) Salir')
print('')

c=int(input('Escoja una opcion del 1 al 5: '))
if c==1:
    print('La suma de ',a,' + ',b,' = ', a+b)
elif c==2:
    print('La suma de ',a,' - ',b,' = ', a-b)
elif c==3:
    print('La suma de ',a,' * ',b,' = ', a*b)
elif c==4:
    print('La suma de ',a,' / ',b,' = ', a/b)
else:
    c==5
    print('Salio con exito')

        
