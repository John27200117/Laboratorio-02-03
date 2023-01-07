# 9.Implemente un programa recursivo que sume ds números a + b. Considera que la suma a+b=a+1+1+...+1 (b veces)
print('-------------------------------------')
print('------------Pregunta N°9-------------')
print('-------------------------------------')


def suma_recursiva(a, b):
    if b == 0:
        return a
    else:
        return suma_recursiva(a, b-1)+1


a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
print(suma_recursiva(a, b))
