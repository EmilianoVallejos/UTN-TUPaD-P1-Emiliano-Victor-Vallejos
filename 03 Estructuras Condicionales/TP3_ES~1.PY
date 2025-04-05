###1

edad= int(input ("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
    
###2

nota= float(input("Ingrese su califificación: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

###3

num= int(input("Ingrese un número: "))
if (num % 2 ==0):
    print("número par")
else:
    print("número impar")

###4

edad= int(input("Ingrese edad: "))
if edad >= 18:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto")
elif edad >= 12:
    print("Adolescente")
else:
    print("Niño")

###5

password= (input("Ingrese contraseña entre 8 a 14 caracteres:"))

if (len(password))<8:
    print("Su contraseña debe superar los ocho caracteres")
elif (len(password))>14:
    print("Su contraseña no debe superar los catorce caracteres")
else:
    print("Contraseña adecuada")

###6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(mean(numeros_aleatorios))
print(median(numeros_aleatorios))
print(mode(numeros_aleatorios))

moda= (mode(numeros_aleatorios))
media= (mean(numeros_aleatorios))
mediana= (median(numeros_aleatorios))

if (media > mediana > moda):
    print("Sesgo positivo o a la derecha")
elif (media < mediana < moda):
    print("Sesgo negativo o a la izquierda")
else: ##(media == mediana == moda)
    print("Sin sesgo")

###7

palabra_frase= [list(input("Ingrese palabra o frase: "))]

if palabra_frase[-1] == ("a" or "A" or "e" or "E" or "i" or "I" or "o" or "O" or "u" or "U"):
    print(palabra_frase + "!")
else:
    pass


###8

nombre= input("Ingrese palabra o frase: ")
numero= input("Ingrese número:")

if (numero == 1):
    nombre_mayuscula = nombre.upper()
    print(nombre_mayuscula)
elif (numero ==2):
    nombre_minuscula = nombre.lower()
    print(nombre_minuscula)
else: 
    nombre_primeramay = nombre.title()
    print(nombre_primeramay)


###9
magnitud= float(input("Ingrese la magnitud del terremoto, según escala Richter: "))

if (magnitud<3):
    print("Muy leve -imperceptible-")
elif magnitud>=3 and <4:
    print("Leve - Ligeramente perceptible")
elif magnitud>=4 and <5:
    print("Moderado")
elif magnitud>=5 and <6:
    print("Fuerte")
elif magnitud>=6 and <7:
    print("Muy fuerte")
else:
    print("Extremo")

###10