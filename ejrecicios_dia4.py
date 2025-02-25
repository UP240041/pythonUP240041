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

##Ejercicio 14
##Separar2
texto="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(texto.split(","))

##Ejercicio 15
##Index
CFA="Coding For All"
print(CFA[0])

##Ejercicio 16
##Rindex
print(CFA.rindex("l"))

##Ejercicio 17
##Imprimir index
CFA="Coding For All"
print(CFA[10])

##Ejercicio 18
##Acronimo1
PFE="Python For Everyone"
primero=PFE.index("P")
segundo=PFE.index("F")
tercero=PFE.index("E")
acronimo=PFE[primero]+PFE[segundo]+PFE[tercero]
print(acronimo)

##Ejercicio 19
##Acronimo2
CFA="Coding For All"
primero=CFA.index("C")
segundo=CFA.index("F")
tercero=CFA.index("A")
acronimo=CFA[primero]+CFA[segundo]+CFA[tercero]
print(acronimo)

##Ejercicio 20
##index
CFA="Coding For All"
print(CFA.index("C")) 

##Ejercicio 21
##index2
CFA="Coding For All"
print(CFA.index("F"))

##Ejercicio 22
##rfind
texto="Coding For All People"
print(texto.rfind("l"))

##Ejercicio 23
##Oración index
texto="You cannot end a sentence with because because because is a conjunction"
print(texto.index("because"))

##Ejercicio 24
##Oración rindex
texto="You cannot end a sentence with because because because is a conjunction"
print(texto.rindex("because"))

##Ejercicio 25
##Oración Cortar
texto="You cannot end a sentence with because because because is a conjunction"
fin=texto.index("because")-1
inicio=texto.rindex("e")+1
textoCortado=texto[0:fin]+texto[inicio:]
print(textoCortado)

##Ejercicio 26
##Oración index2
texto="You cannot end a sentence with because because because is a conjunction"
print(texto.index("because"))

##Ejercicio 27
##Oración Cortar2
texto="You cannot end a sentence with because because because is a conjunction"
fin=texto.index("because")-1
inicio=texto.rindex("e")+1
textoCortado=texto[0:fin]+texto[inicio:]
print(textoCortado)

##Ejercicio 28
##satrtswith
CFA="Coding For All"
inicio="Coding"
print(CFA.startswith(inicio))

##Ejercicio 29
##endswith
CFA="Coding For All"
fin="coding"
print(CFA.endswith(fin))

##Ejercicio 30
##Quitar espacios
texto='   Coding For All      '
inicio=texto.index("C")
fin=texto.rindex("l")+1
textosinespacios=texto[inicio:fin]	
print(textosinespacios)

##Ejercicio 31
##isidentifier
texto1="30DaysOfPython"
texto2="thirty_days_of_python"
print(texto1.isidentifier())
