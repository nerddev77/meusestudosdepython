print('Bem-Vindo ao sistema de viagens')
distancia = float(input('Por-favor, me informe quantos KM foram percorridos: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
    print('Parabéns! Você percorreu mais de 200KM e irá ganhar um desconto! (De 5 centavos a cada KM mas já é alguma coisa)')
print(f'O total a pagar é R${preco :.2f}')