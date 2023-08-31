from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
h1 = hypot(co, ca)
print(f'A hipotenusa vai medir: {h1 :.2f}')