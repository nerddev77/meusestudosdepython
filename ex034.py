salário = float(input('Digite o salário do funcionário: '))
if salário > 1250.00:
    reajuste = salário + (salário * 10/100)
    print(f'O reajuste do funcionário será: {reajuste :.2f}')

if salário < 1250.00:
    reajuste = salário + (salário * 15/100)
    print(f'O reajuste do funcionário será: {reajuste :.2f}')