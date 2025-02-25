##Ejercicios del día 3

##Ejercicio 1
edad= int(input("Introduce tu edad: ")) #Se pide la edad

##Ejercicio 2
estatura= float(input("Introduce tu estatura: ")) #Se pide la estatura

##Ejercicio 3
numeroComplejo= complex(input("Introduce un número complejo: ")) #Se pide un número complejo

##Ejercicio 4
##Area de un triángulo
base= float(input("Introduce la base del triángulo: ")) #Se pide la base
altura= float(input("Introduce la altura del triángulo: ")) #Se pide la altura
area= (base*altura)/2 #Se calcula el área
print("El área del triángulo es: ", area) #Se imprime el resultado

##Ejercicio 5
##Perimetro de un triángulo

lado1= float(input("Introduce el lado 1 del triángulo: ")) #Se pide el lado 1
lado2= float(input("Introduce el lado 2 del triángulo: ")) #Se pide el lado 2
lado3= float(input("Introduce el lado 3 del triángulo: ")) #Se pide el lado 3
perimetro= lado1+lado2+lado3 #Se calcula el perímetro
print("El perímetro del triángulo es: ", perimetro) #Se imprime el resultado

##Ejercicio 6
##Area y perímetro de un cuadrado
lardo= float(input("Introduce el largo del cuadrado: ")) #Se pide el largo
ancho= float(input("Introduce el ancho del cuadrado: ")) #Se pide el ancho
area= lardo*ancho #Se calcula el área
perimetro= 2*lardo+2*ancho #Se calcula el perímetro
print("El área del cuadrado es: ", area) #Se imprime el área

##Ejercicio 7
##Area y perímetro de un circulo
pi= 3.1416 #Se define el valor de pi
radio= float(input("Introduce el radio del círculo: ")) #Se pide el radio
area= pi*radio**2 #Se calcula el área
perimetro= 2*pi*radio #Se calcula el perímetro
print("El área del círculo es: ", area) #Se imprime el área

##Ejercicio 8
##Pendiente de la recta "y=2x-2"
pendiente1= 2 #Se define la pendiente
intersecciónY= -2 #Se define la intersección con el eje Y
intersecciónX= intersecciónY/pendiente1 #Se calcula la intersección con el eje X
print("La pendiente de la recta es:\n", pendiente1, "\nLa intersección con el eje X es:\n", intersecciónX, "\nLa intersección con el eje Y es:\n", intersecciónY)

##Ejercicio 9
##Pendiente dos puntos
punto1= (2,2) #Se define el punto 1
punto2= (6,10) #Se define el punto 2
x1= punto1[0] #Se obtiene la coordenada x del punto 1
y1= punto1[1] #Se obtiene la coordenada y del punto 1
x2= punto2[0] #Se obtiene la coordenada x del punto 2
y2= punto2[1] #Se obtiene la coordenada y del punto 2
pendiente2= (y2-y1)/(x2-x1) #Se calcula la pendiente
distancia= ((x2-x1)**2+(y2-y1)**2)**0.5 #Se calcula la distancia entre los dos puntos
print("La pendiente de los puntos es:", pendiente2, "\nLa distancia entre los puntos es:", distancia)

##Ejercicio 10
##Comparar pendientes
pendiente1<pendiente2 #Se compara si la pendiente 1 es menor que la pendiente 2
if True:
    print("La pendiente 1 es menor que la pendiente 2")
else:
    print("La pendiente 1 no es menor que la pendiente 2")

##Ejercicio 11
x=int(input("Introduce un número: ")) 
y=x**2+6*x+9 
    ## "y" es igual a cero cunaod x es igual a -3

##Ejercicio 12
##Comparar longitudes de palabras
palabra1= "python" #Se define la palabra 1
palabra2= "dragon" #Se define la palabra 2
longitud1= len(palabra1) #Se obtiene la longitud de la palabra 1
longitud2= len(palabra2) #Se obtiene la longitud de la palabra 2
longitud1<longitud2 #Se compara si la longitud de la palabra 1 es menor que la longitud de la palabra 2
if True:
    print("La longitud de la palabra 1 es menor que la longitud de la palabra 2")
else:
    print("La longitud de la palabra 1 no es menor que la longitud de la palabra 2")

##Ejercicio 13 (PENDIENTE)
##Esta en?
print("on" in "python" and "on" in "dragon") #Se imprime si "on" está en "python" y en "dragon"
if True:
    print("on está en python y en dragon")  #Se imprime si "on" está en "python" y en "dragon"
else:
    print("on no está en python y en dragon")  #Se imprime si "on" no está en "python" y en "dragon"


##Ejercicio 14
##Esta en?2
print("jargon" in "I hope this course is not full of jargon") #Se imprime si "jargon" está en la frase
if True:
    print("jargon está en la frase")  #Se imprime si "jargon" está en la frase
else:
    print("jargon no está en la frase")

##Ejercicio 15
print("on" not in "python" and "on" not in "dragon") #Se imprime si "on" no está en "python" y en "dragon"
if True:
    print("on no está en python y en dragon")  #Se imprime si "on" no está en "python" y en "dragon"
else:
    print("on está en python y en dragon")  #Se imprime si "on" está en "python" y en "dragon"


##Ejercicio 16
##Converciones
palabra="python" #Se define la palabra
longitud= len(palabra) #Se obtiene la longitud de la palabra
float(longitud) #Se convierte la longitud a entero
str(longitud) #Se convierte la longitud a string

##Ejercicio 17
##Pares
n=int(input("Introduce un número: "))
n%2==0 #Se verifica si el número es par
if True:
    print("El número es par") #Se imprime si el número es par
else:
    print("El número no es par")

##Ejercicio 18
##floor division
floorDivision=7//3 #Se calcula la división entera de 7 entre 3
n=int(2.7) #Se convierte 2.7 a entero
floorDivision==n #Se compara si la división entera de 7 entre 3 es igual a 2.7 convertido a entero
if True:
    print("La división entera de 7 entre 3 es igual a 2.7 convertido a entero") #Se imprime si la división entera de 7 entre 3 es igual a 2.7 convertido a entero
else:
    print("La división entera de 7 entre 3 no es igual a 2.7 convertido a entero")

##Ejercicio 19
## ¿"10" es igual a 10?
print("10"==10) #Se compara si "10" es igual a 10  (False)

##Ejercicio 20
##¿int(9.8) es igual a 10?
print(int(9.8)==10) #Se compara si int(9.8) es igual a 10 (True)
##Los decimales se redondean al entero más cercano

##Ejercicio 21
##Salario
horasTrabajadas= int(input("Introduce las horas trabajadas: ")) #Se piden las horas trabajadas
tarifaPorHora= float(input("Introduce la tarifa por hora: ")) #Se pide la tarifa por hora
diasTrabajadosSemanales= int(input("Introduce los días trabajados a la semana: ")) #Se piden los días trabajados a la semana
salarioSemanal= horasTrabajadas*tarifaPorHora*diasTrabajadosSemanales #Se calcula el salario semanal
print("El salario semanal es: ", salarioSemanal) #Se imprime el salario semanal


##Ejercicio 22
##Años vividos, segundos vividos
edad= int(input("Introduce tu edad: ")) #Se pide la edad
diasVividos= edad*365 #Se calculan los días vividos
segundosVividos= diasVividos*24*60*60 #Se calculan los segundos vividos
print("Has vivido ", diasVividos, " días y ", segundosVividos, " segundos") #Se imprime los días y segundos vividos

##Ejercicio 23
##tabla de exponentes
a=1
print(a, a**0, a**1, a**2, a**3)
a+=1
print(a, a**0, a**1, a**2, a**3)
a+=1
print(a, a**0, a**1, a**2, a**3)
a+=1
print(a, a**0, a**1, a**2, a**3)
a+=1
print(a, a**0, a**1, a**2, a**3)
