# 2.Corra el algoritmo anterior "desordena"(del ejercicio 1) muchas veces para la misma sucesión de entrada.¿Como puede analizarse para determinar si es verdaderamente "aleatorio"?
import random
print('-------------------------------------')
print('------------Pregunta N°2-------------')
print('-------------------------------------')


def desordenar(lista, largoL, contador):
    if contador < largoL:
        numeroR = random.randint(contador, largoL-1)
        lista[contador], lista[numeroR] = lista[numeroR], lista[contador]
        desordenar(lista, largoL, contador+1)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
desordenar(A, len(A), 0)
print(A)

# RESPUESTA:Nos damos cuenta que, cada vez que se ejecute el programa
# nos saldra una diferente lista
