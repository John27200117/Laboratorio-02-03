# 8.Implemente un programa recursivo que calcule la potencia de un nu mero elevado a otro.
print('-------------------------------------')
print('------------Pregunta N°8-------------')
print('-------------------------------------')


def potencia(base, exp):
    if exp == 0:
        resultado = 1
    else:
        resultado = base*potencia(base, exp-1)
    return resultado


base = int(input('Ingrese la base: '))
exp = int(input('Ingrese el exponente: '))
print(potencia(base, exp))
