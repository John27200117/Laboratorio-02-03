# 3. Implemente la selección por orden como un programa: EL algoritmo de seleccion por orden acomodada la sucesión S1,...,Sn en orden no decreciente,
#    para ello encuentra primero el elemento más pequeño, po ejemplo si, y lo colocara en el primer lugar intercambiando S1 y Si. Despues encuentra el
#    algoritmo más pequeño en S2,...,Sn; de nuevo digmos Si, y lo coloco en el segundo lugar intercambiando S2 y S1. Continuamos hasta que la sucesión esté ordenada.
print('-------------------------------------')
print('------------Pregunta N°3-------------')
print('-------------------------------------')


def seleccion_orden(lista, largo_lista, contador):
    if contador < largo_lista:
        pequeño = lista[contador]
        posicion = contador
        for i in range(contador+1, largo_lista):
            if lista[i] < pequeño:
                pequeño = lista[i]
                posicion = i
        lista[contador], lista[posicion] = lista[posicion], lista[contador]
        seleccion_orden(lista, largo_lista, contador+1)


A = [7, 2, 5, 3, 1, 4, 9, 6]
seleccion_orden(A, len(A), 0)
print(A)
