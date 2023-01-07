# 6.Un robot puede dar pasos de 1 o 2 metros. Escriba un programa para numerar todas las maneras en que el robot camina n metros
print('-------------------------------------')
print('-------------------------------------')
print('------------Pregunta N°6-------------')
print('-------------------------------------')


def robot(n):
    if n == 1 or n == 2:
        return n
    return robot(n-1)+robot(n-2)


n = int(input('Cuantos pasos dara el robot: '))
print('El robot tiene', robot(n), 'manera de caminar')
