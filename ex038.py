a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a > b:
    print(f'{a} é maior que {b}')
elif b > a:
    print(f'{b} é maior que {a}')
else:
    print(f'{a} e {b} são iguais.')