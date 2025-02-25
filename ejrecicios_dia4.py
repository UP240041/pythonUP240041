##Ejercicios dia 4

##Ejercicio 1
##Concatenar1
plabra1="Thirty"
palabra2="Days"
palabra3="Of"
palabra4="Python"
espacio=" "
concatenar=plabra1+espacio+palabra2+espacio+palabra3+espacio+palabra4
print(concatenar)

##Ejercicio 2
##Concatenar2
palabra1="Coding"
palabra2="For"
palabra3="All"
espacio=" "
concatenar=palabra1+espacio+palabra2+espacio+palabra3
print(concatenar)

##Ejercicio 3
##Decalración de variable
company="Coding For All"

##Ejercicio 4
##Imprimir la variable company
print(company)

##Ejercicio 5
##Imprimir el tamaño de la variable company
print(len(company))

##Ejercicio 6
##Todas las letras en mayusculas
print(company.upper())

##Ejercicio 7
##Todas las letras en minusculas
print(company.lower())

##Ejercicio 8
##Dar formato a un string
CFA="coding for all"
print(CFA.capitalize())
print(CFA.title())
print(CFA.swapcase())

##Ejercicio 9
##Cortar
CFA="Coding For All"
inicio=CFA.find("Coding")
fin=CFA.find("All")
print(CFA[inicio:fin])

##Ejercicio 10
##Buscar "Coding"
buscar="Coding"
CFA="Coding For All"
print(CFA.index(buscar))

##Ejercicio 11
##Reemplazar1
CFA="Coding For All"
print(CFA.replace("Coding","Python"))

##Ejercicio 12
##Reemplazar2
EP="Everyone to Python"
print(EP.replace("Python","All"))

##Ejercicio 13
##Separar
CFA="Coding For All"
print(CFA.split(" "))



