r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Não forma um triângulo.')
elif r1 != r2 != r3:
    print('Forma um triângulo escaleno.')
elif (r1 == r2) and (r2 == r3):
    print('Forma um triângulo equilátero.')
elif (r1 == r2) or (r2 == r3) or (r3 == r1):
    print('Forma um triângulo isósceles.')