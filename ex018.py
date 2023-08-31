from math import radians, sin, cos, tan
an = float(input("Digite o ângulo: "))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print(f'O ângulo de {an}° tem o seno de {seno :.2f}')
print(f'O cosseno de {cosseno :.2f}')
print(f'E o tangente de {tangente :.2f}')