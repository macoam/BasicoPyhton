#Esto es un comentario
#print ("Comentario")
print("Hola otra vez mundo") 
print("Adios mundo")

#Operadores aritméticos
5+1
print (4+6)
print (5-3)
print (4*4)
print (30/2)

#Precedecia de operadores
print (5+8*3+2)
print (5+8*(3+2))

#Tipos de datos
print (type(2))
print (type(8.62))
print (type("Texto"))
print (type('Texto'))
print (type("5"))

#Variables
mensaje = "Esto es un mensaje"
print(mensaje)
mensaje = "Este mensaje esta modificado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

mis3animales = "Son mios"
print(mis3animales)
#3animales = "Son mios" 
# #print(3animales)
# LAS VARIABLES NO PUEDEN COMENZAR CON NUMERO NI
# CARACTERES ESPECIALES

#Concatenación de textos

textoUno = "Mi texto"
textoDos = "Mi segundo texto"

print(textoUno + textoDos)

edad = "20"
print("La edad del usuario es: " + edad)

#edad = 20
#print("La edad del usuario es: " + edad) ASÍ NO

edad = 20
print("La edad del usuario es: " + str(edad))
print(type(edad))
print(str(type(edad)))
print("La edad del usuario es: " + str(type(edad)))


import math 

grados = 45
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("Seno de 45° es: " + str(seno))

def saludar(nombre):
    print("Holis " + nombre)
    print("¿Cómo estas?")
    print("De lejos, con susana distancia")

def despedir():
    print("Ya me voy pues")
    print("Genial, la peda pa' la otra")

def concatenar(parte1, parte2):
    return parte1 + parte2

print("Esto no es parte de la función")
saludar("Murdoc")
despedir()

frase = concatenar("Hola 2D", " - Hola Murdoc")
print(frase)

