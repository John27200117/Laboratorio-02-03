# 5.Escriba un programa recursivo y otro no recursivo para calcular la sucesión de Fibonacci.
import time
# Recursividad
print('-----------------------------------------------')
print('----------Cuando usamos recursividad-----------')
print('-----------------------------------------------')
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

tiempo1 = time.perf_counter()
n = int(input('Ingrese un numero: '))
fibonacci(n)
tiempo2 = time.perf_counter()
tiempo = tiempo2-tiempo1
print(fibonacci(n))
print('Cuando es Recursivo demora en ejecutar:', tiempo)

# Sin Recursividad
print('-----------------------------------------------')
print('----------Cuando NO usamos recursividad--------')
print('-----------------------------------------------')
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

tiempo1 = time.perf_counter()
n = int(input('Ingrese un numero: '))
fibonacci(n)
tiempo2 = time.perf_counter()
tiempo = tiempo2-tiempo1
print(fibonacci(7))
print('Cuando es NO es Recursivo demora en ejecutar:', tiempo)
