##EJERCICIO 1

for i in range(101):
    print(i)


##EJERCICIO 2

entero=int(input("Ingrese un número:"))

if entero <= 9:
    print("El número ingresado contiene un dígito")
elif entero <= 99:
    print("El número ingresado contiene dos dígitos")
elif entero <= 999:
    print("El número ingresado contiene tres dígitos")
elif entero <= 9999:
    print("El número ingresado contiene cuatro dígitos")
elif entero <= 99999:
    print("El número ingresado contiene cinco dígitos")
elif entero <= 999999:
    print("El número ingresado contiene seis dígitos")
else:
    pass


##EJERCICIO 3

entero1=int(input("Ingrese un primer número: "))
entero2=int(input("Ingrese un segundo número: "))
acum = 0

if entero1 < entero2:
    for cont in range(entero1 + 1, entero2):
        acum += cont
else:
    for cont in range(entero2 + 1, entero1):
        acum += cont
print(f"La sumatoria de los números comprendidos entre {entero1} y {entero2} dados es: {acum}")


##EJERCICIO 4

acumul= 0

while True:
    nro1 = int(input("Ingrese un número para ser sumado -o 0 para finalizar-: "))
    if nro1 == 0:
        break
    acumul += nro1
    print(f"la suma acumulada es: {acumul}")


##EJERCICIO 5

import random
aleatorio = random.randint(0, 9)
nroadiv = int(input("Adivine el nro del 0 al 9: "))
contador = 1

while nroadiv != aleatorio:
    nroadiv = int(input("Ingrese otro nro del 0 al 9: "))
    contador = contador + 1    
else:
    print(f"El número {nroadiv} ha sido acertado!. {contador} intentos " )


##EJERCICIO 6 - 

for i in range(100,-2,-2):
    print(i)


##EJERCICIO 7

nroentero = int(input("Ingrese un número entero: "))
suma= 0
for i in range (0, nroentero + 1):
    suma+=i
print(f"El resultado de de la suma entre 0 y {nroentero} es: {suma}")


##EJERCICIO 8

cantidadlimite = 10

pares = 0
impares = 0
negativos = 0
positivos = 0

print (f"Ingrese {cantidadlimite} números enteros: ")

for i in range(cantidadlimite):
    numingresado = int(input(f"Número {i + 1}:"))
    if numingresado % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numingresado > 0:
        positivos += 1
    elif numingresado < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
    

##EJERCICIO 9
from statistics import mean

cantidadlimite = 10

print (f"Ingrese {cantidadlimite} números enteros: ")

numeros = []

for i in range(cantidadlimite):
    numingresado = int(input(f"Número {i + 1}:"))
    numeros.append(numingresado)
    
media = mean(numeros)
print(f"La media de los números ingresados es: {media}")


##EJERCICIO 10

nro = int(input("Ingrese un número entero: "))
nroinvertido = 0
digito = 0

while nro !=0:
    digito= nro % 10
    nroinvertido = nroinvertido*10 + digito
    nro = nro // 10
print(f"El número invertido es: {nroinvertido}")