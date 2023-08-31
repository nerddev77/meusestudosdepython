num = int(input('Me diga um número qualquer: '))
res = num % 2

# Aqui vamos fazer uma conta com o resto da divisão de 2
# Todo número par dá resultado 0, e todo número ímpar dá resultado 1

if res == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')

