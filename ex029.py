velocidade = float(input('Qual é a velocidade atual do carro?'))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Continue dirigindo com segurança!')
else:
    print('MULTADO! Você excedeu o limite de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa}')