##Ejercicios del día 3

##Ejercicio 1
edad= int(input("Introduce tu edad: ")) #Se pide la edad
estatura= float(input("Introduce tu estatura: ")) #Se pide la estatura
numeroComplejo= complex(input("Introduce un número complejo: ")) #Se pide un número complejo

##Ejercicio 2
##Area de un triángulo
base= float(input("Introduce la base del triángulo: ")) #Se pide la base
altura= float(input("Introduce la altura del triángulo: ")) #Se pide la altura
area= (base*altura)/2 #Se calcula el área
print("El área del triángulo es: ", area) #Se imprime el resultado

##Ejercicio 3
##Perimetro de un triángulo

lado1= float(input("Introduce el lado 1 del triángulo: ")) #Se pide el lado 1
lado2= float(input("Introduce el lado 2 del triángulo: ")) #Se pide el lado 2
lado3= float(input("Introduce el lado 3 del triángulo: ")) #Se pide el lado 3
perimetro= lado1+lado2+lado3 #Se calcula el perímetro
print("El perímetro del triángulo es: ", perimetro) #Se imprime el resultado

##Ejercicio 4
##Area y perímetro de un cuadrado
lardo= float(input("Introduce el largo del cuadrado: ")) #Se pide el largo
ancho= float(input("Introduce el ancho del cuadrado: ")) #Se pide el ancho
area= lardo*ancho #Se calcula el área
perimetro= 2*lardo+2*ancho #Se calcula el perímetro
print("El área del cuadrado es: ", area) #Se imprime el área

##Ejercicio 5
##Area y perímetro de un circulo
pi= 3.1416 #Se define el valor de pi
radio= float(input("Introduce el radio del círculo: ")) #Se pide el radio
area= pi*radio**2 #Se calcula el área
perimetro= 2*pi*radio #Se calcula el perímetro
print("El área del círculo es: ", area) #Se imprime el área

##Ejercicio 6
##Pendiente de la recta "y=2x-2"
pendiente1= 2 #Se define la pendiente
intersecciónY= -2 #Se define la intersección con el eje Y
intersecciónX= intersecciónY/pendiente1 #Se calcula la intersección con el eje X
print("La pendiente de la recta es:\n", pendiente1, "\nLa intersección con el eje X es:\n", intersecciónX, "\nLa intersección con el eje Y es:\n", intersecciónY)

##Ejercicio 7
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

##Ejercicio 8
##Comparar pendientes
pendiente1<pendiente2 #Se compara si la pendiente 1 es menor que la pendiente 2
if True:
    print("La pendiente 1 es menor que la pendiente 2")
else:
    print("La pendiente 1 no es menor que la pendiente 2")

##Ejercicio 9
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

##Ejercicio 10
##Esta en?









##Ejercicio 
##Converciones
palabra="python" #Se define la palabra
longitud= len(palabra) #Se obtiene la longitud de la palabra
pirnt("on" in "python" and "on" in "dragon") #Se imprime si "on" está en "python" y en "dragon"

