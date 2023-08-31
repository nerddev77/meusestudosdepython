from datetime import date
atual = date.today().year
nasc = int(input('Insira o Ano de Nascimento: '))
idade = atual - nasc
print(f'O atleta tem {idade}')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: MASTER')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else: 
    print('Classificação: MASTER')