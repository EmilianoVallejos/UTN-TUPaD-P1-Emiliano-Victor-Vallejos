#####TRABAJO PRÁCTICO PROGRAMACIÓN I: RECURSIVIDAD
### Alumno: Emiliano Víctor Vallejos.



# EJERCICIO 1:


def factorial_numero(n):
    if n == 0:
        return 1
    else:
        return n * factorial_numero(n-1)
    
n=int(input("Ingrese un número para realizar su factorial:")) 

print(f"El factorial del número {n} ingresado por el usuario es: {factorial_numero(n)}")



# EJERCICIO 2:


def funcion_fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return funcion_fibonacci(n-1) + funcion_fibonacci(n-2)
        

n=int(input("Ingrese un número entero positivo:"))

if n < 0:
    print("ERROR. Debe ingresar un número positivo.")
else:
    print(f"La serie Fibonacci hasta la posición ingresada {n}: ")
    for i in range (n + 1):
        print(funcion_fibonacci(i), end=" - ")



# EJERCICIO 3:


def funcion_potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * funcion_potencia (n, m-1)

n= float(input("Ingresse un número para la base: "))
m= int(input("Ingrese un número entero positivo, como exponente: "))


if m < 0:
    print("ERROR. Únicamente permitido exponentes enteros no negativos")
else:
    resultado= funcion_potencia(n, m)
    print(f"{n} elevado a la {m} es igual a: {resultado}")



# EJERCICIO 4:


def funcion_decimal_a_binario(decimal):
    if decimal == 0:
        return ""
    else:
        print(f"Llamando a funcion_decimal_a_binario({decimal})")
        return funcion_decimal_a_binario(decimal//2)+str(decimal%2)

decimal=int(input("Ingrese un número entero decimal para su conversión a binario: "))

if decimal <0:
    print("ERROR. Debe ingresar un número positivo")
elif decimal == 0:
    print("El número 0 en binario es igual a 0")
else:
    binario = funcion_decimal_a_binario(decimal)
    print(f"El numero {decimal} a binario es: {binario}")



# EJERCICIO 5:


def es_palindromo(palabra):
    if len(palabra)<=1:
        return True
    
    if palabra [0]!= palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()

if es_palindromo(texto):
    print(f"La palabra ingresada: {texto}, es un palíndromo.")
else:
    print(f"La palabra ingresada: {texto}, NO es un palíndromo.")



# EJERCICIO 6:


def suma_digitos(n):
    if n == 0:
        return 0
    else:
        print(f"n: {n}, n % 10 = {n % 10}, n // 10 = {n // 10}")
        return (n%10) + suma_digitos(n//10)
    

n=int(input("Ingrese un número entero positivo: "))

if n < 0:
    print("ERROR: Debe ingresar un número positivo.")
else:
    resultado = suma_digitos(n)
    print(f"La suma de los dígitos de {n} es: {resultado}")



# EJERCICIO 7:


def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)
    
n=int(input("Ingrese un número entero positivo: "))

if n < 0:
    print("ERROR: Debe ingresar un número positivo.")
else:
    resultado = contar_bloques(n)
    print(f"La suma necesaria de bloques para construir la pirámide es: {resultado}")



# EJERCICIO 8:


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10

        if ultimo_digito == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
            

numero=int(input("Ingrese un número entero positivo: "))
digito=int(input("Ingrese un dígito (entre 0 y 9) para saber cuantas veces se encuentra en el número indicado: "))

resultado = contar_digito(numero, digito)

print(f"El dígito {digito} ingresado aparece {resultado} veces en el número")