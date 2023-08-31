# Perguntas e declaração de variáveis
salario = float(input('Bem-vindo ao simulador de compra de casa/apto. Por favor, digite seu salário: '))
anos = int(input('Em quantos anos você deseja pagar sua casa/apto? '))
valor_da_casa = float(input('Por favor, digite o valor da casa/apto: '))

# Cálculos
meses = anos * 12
prestacao = valor_da_casa / meses
porcentagem_do_salario = salario * 0.3

if prestacao > porcentagem_do_salario:
    print("Seu empréstimo foi negado, pois a prestação excede 30% do seu salário.")
else:
    print(f'Seu empréstimo foi aprovado, o valor da prestação mensal será: {prestacao:.2f}')
