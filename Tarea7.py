'''
Dadas dos listas, debes generar una tercera con todos los 
elementos que se repitan en ellas, pero no debe repetise ningún 
elemento en la nueva lista:'''
lista1={3,8,'Jose',3,'Hola',3,5,5,3,2,9,9}
print(lista1)
lista2={5,3,'Carlos',7,'Adios',9,7,8,4}
print(lista2)
lista3 = {}
lista3=lista1.union(lista2)
print(lista3)