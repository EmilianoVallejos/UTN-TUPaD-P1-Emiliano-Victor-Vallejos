#### Trabajo Práctico: Funciones.

#### Alumno: Emiliano Víctor Vallejos.

#########################################################################
#EJERCICIO 1


def hola_mundo (saludo):
    return saludo


saludar = hola_mundo (print("Hola mundo!"))


#########################################################################
#EJERCICIO 2


def saludar_usuario(nombre):
    return f"Hola! {nombre}"


nombre = input("Por favor, ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)


#########################################################################
#EJERCICIO 3


def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}"

nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
residencia= input("Ingrese su lugar de residencia: ")

informacion = informacion_personal(nombre, apellido, edad, residencia)
print(informacion)


#########################################################################
#EJERCICIO 4


def  calcular_area_circulo(radio):
    return 3.14159*(radio*radio)

def calcular_perimetro_circulo(radio):
    return 2*3.14159*radio


radio=(float(input("Ingrese el valor del radio: ")))

areacirculo= calcular_area_circulo(radio)
perimetrocirculo= calcular_perimetro_circulo(radio)

print(f"El area del círculo es: {areacirculo}. El perímetro del círculo es: {perimetrocirculo}")


#########################################################################
#EJERCICIO 5


def segundos_a_horas(segundos):
    return segundos/3600


segundos=float(input("Ingrese cantidad de segundos: "))
conversor=segundos_a_horas(segundos)
print(f"Los {segundos} segundos ingresados representa {conversor} horas")


#########################################################################
#EJERCICIO 6


def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i}= {numero*i}")
    
numero=int(input("Ingrese un número: "))
tabla_multiplicar(numero)


#########################################################################
#EJERCICIO 7

def operaciones_basicas(a, b):
    suma= a+b
    resta= a-b
    multiplicacion= a*b
    division= a/b if b != 0 else "División por 0 es inexistente"
    return(suma, resta, multiplicacion, division)


a=int(input("Ingrese un primer número: "))
b=int(input("Ingrese un segundo número: "))

resultado= operaciones_basicas(a, b)

print(f"El resultado de sumarlos: {resultado[0]}. El resultado de restarlos: {resultado[1]}. El resultado de multiplicarlos: {resultado[2]}. El resultado de dividirlos: {resultado[3]}")


#########################################################################
#EJERCICIO 8


def calcular_imc(peso, altura):
    return peso/altura**2

peso=float(input("Ingrese su peso en kilogramos: "))
altura=float(input("Ingrese su estatura en metros: "))

imc= calcular_imc(peso, altura)

print(f"El índice de masa corporal conforme a sus valores ingresados es: {imc:.2f}")


#########################################################################
#EJERCICIO 9


def celsius_a_fahrenheit(celsius):
    fahrenheit= (celsius*1.8)+32
    return fahrenheit


celsius=float(input("Ingrese la temperatura en grados Celsius: "))    
fahrenheit=celsius_a_fahrenheit(celsius)

print(f"El equivalente de los {celsius}° celsius a fahrenheit es: {fahrenheit}")


#########################################################################
#EJERCICIO 10


def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    return promedio


a=float(input("Ingrese un primer número:"))
b=float(input("Ingrese un segundo número:"))
c=float(input("Ingrese un tercer número:"))

promedio= calcular_promedio(a, b, c)

print(f"El promedio de los numeros {a}, {b} y {c} es: {promedio}")