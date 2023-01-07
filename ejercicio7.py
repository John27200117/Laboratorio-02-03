# 7.Un robot puede dar pasos de 1,2 o 3 metros. Escriba un programa para enumerar todas las maneras en que el robot camina n metros.
print('-------------------------------------')
print('------------Pregunta N°7-------------')
print('-------------------------------------')


def robot(n):
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return n+1
    return robot(n-1)+robot(n-2)+robot(n-3)


n = int(input('Cuantos pasos dara el robot: '))
print('El robot tiene', robot(n), 'manera de caminar')
