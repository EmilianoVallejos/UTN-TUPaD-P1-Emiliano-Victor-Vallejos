#TRABAJO PRÁCTICO PROGRAMACIÓN 1: LISTAS - Emiliano Víctor Vallejos


#1 EJERCICIO:

lista_1a100_4 = []
acumulado= 0
for lista_1a100_4 in range(0, 104, 4):
    lista_1a100_4 += acumulado
    print(lista_1a100_4)


#2 EJERCICIO:

lista_5_elementos=["Emiliano Vallejos", 2025, "UTN", "Programación 1", 9.8]
penultimo_lista= lista_5_elementos[-2]
print(penultimo_lista)


#3 EJERCICIO:

lista_vacia = []
lista_vacia.append("UTN")
print(lista_vacia)                                                                                                              


#4 EJERCICIO: 

animales = ["perro", "gato", "conejo", "pez" ]
animales[2]="loro"
animales[3]= "oso"
print(animales)


#5 EJERCICIO:
#En el siguiente ejercicio la función lista.remove(max(lista)) se ocupa de remover el elemento de mayor valor dentro de una lista predeterminada. 

numeros = [8, 15, 3, 22,  7]
numeros.remove(max(numeros))
print(numeros)


#6 EJERCICIO:

lista_10_30= list(range(10,31,5))
primeros_dos= lista_10_30[0: 2]
print(primeros_dos)


#7 EJERCICIO:

autos = ["sedan", "polo", "suran", "gol"]

autos[1]="golf"
autos[2]="vento"
print(autos)


#8 EJERCICIO:

dobles=[]

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


#9 EJERCICIO:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

    #a) Agregar "jugo" a la lista del tercer cliente usando append
agrega_jugo = compras[2]
agrega_jugo.append("jugo")

    #b)Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]= "tallarines"

    #c)Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

    #d)Imprimir la lista resultante por pantalla.
print(compras)


#10 EJERCICIO:

lista_anidada= [15, True,[25.5, 57.9, 30.6], False]
print(lista_anidada)