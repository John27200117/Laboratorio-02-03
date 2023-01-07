# 4. Escriba un programa recursivo y otro no recursivo para calcular n!. Compare los tiempos requeridos por los programas.
import time
# Programa recursivo
print('-------------------------------------')
print('-----Cuando usamos recursividad------')
print('-------------------------------------')


def factorial(n):
    if n == 1:
        return n
    return n*factorial(n-1)


tiempo1 = time.perf_counter()
n = int(input("Ingrese de que número desea su factorial: "))
x = factorial(n)
tiempo2 = time.perf_counter()
tiempo = tiempo2 - tiempo1
print('El factorial de', n, '!=', x)
print('El tiempo cuando usamos recursividad:', tiempo)

# Programa no recursivo
print('-------------------------------------')
print('-----Cuando no usamos recursividad---')
print('-------------------------------------')


def factorial(n):
    b = 1
    for i in range(n, 1, -1):
        b = b*i
    return b


tiempo1 = time.perf_counter()
n = int(input("Ingrese de que número desea su factorial: "))
fac = factorial(n)
tiempo2 = time.perf_counter()
tiempo = tiempo2-tiempo1
print('El factorial de', n, '!=', fac)
print('El tiempo cundo no usamos recursividad:', tiempo)
