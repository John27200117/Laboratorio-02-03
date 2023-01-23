# 1.Implemente el siguiente algoritmo como un programa para desordenar.
import random

print('------------Pregunta N°1-------------')



def desordena(lista, largoL, contador):
    if contador < largoL:
        numeroR = random.randint(contador, largoL-1)
        lista[contador], lista[numeroR] = lista[numeroR], lista[contador]
        desordena(lista, largoL, contador+1)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
desordena(A, len(A), 0)
print("Asi se veria desordenado =", A)
