##Ejercicios dia 5

##Ejercicio 1
##lista vacia
lista=[]

##Ejercicio 2
##lista con 5 elementos
lista=[0,1,2,3,4]

##Ejercicio 3
##cantidad de elementos de la lista
print(len(lista))

##Ejercicio 4
##Inicio, medio y final de la lista
##print(lista[0,2,4])
primero, segundo, tercero, cuarto, quinto = lista
print(primero, tercero, quinto)

##Ejercicio 5
##Lista de datos mixta
mixed_data_types=["Eduardo",18,1.85,"soltero","Mi casa"]

##Ejercicio 6
##Empresas IT
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

##Ejercicio 7
##Imprimir lista
print(it_companies)

##Ejercicio 8
##Cantidad de compañias
print("Cantidad de compañias IT",len(it_companies))

##Ejercicio 9
##Inicio, medio y final de la lista IT
inicio=it_companies[0]
medio=it_companies[3]
final=it_companies[6]
print(inicio,medio,final)

##Ejercicio 10
##Imprimir despues de modificar la lista
it_companies[1]="Meta"
print(it_companies)

##Ejercicio 11
##Agregar un elemento al final de la lista
it_companies.append("X")

##Ejercicio 12
##Agregar un elemento en medio de la lista
it_companies.insert(5, "Reditt")

##Ejercicio 13
##Editar un elemento de la lista
it_companies[0].upper()

##Ejercicio 14
##Join
print("#, ".join(it_companies))

##Ejercicio 15
##Existencia en la lista
existeGoogle="Google" in it_companies
print(existeGoogle)

##Ejercicio 16
##Ordenar la lista (Ascendente)
it_companies.sort()

##Ejercicio 17
##Ordenar la lista (Descendente)
it_companies.sort(reverse=True)

##Ejercicio 18
##Quitar los primeros tres elementos de la lista
print(it_companies[3:])

##Ejercicio 19
##Quitar los ultimos tres elementos de la lista
print(it_companies[0:-3])

##Ejercicio 20
##Quitar la empresa de en medio
empresas1=it_companies[0:4]
empresas2=it_companies[5:9]
empresasResultantes=empresas1+empresas2
print(empresasResultantes)

##Ejercicio 21
##Remover la primera empresa
del it_companies[0]

##Ejercicio 22
##Remover la empresa de enmedio
del it_companies[3,4]

##Ejercicio 23
##Remover la ultima empresa
it_companies.pop()

##Ejercicio 24
##Remover todas las empresas
it_companies.clear()

##Ejercicio 25
##Eliminar la lista
del it_companies

##Ejercicio 26
##Concatenar dos listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
listaCompleta= front_end + back_end
print(listaCompleta)

