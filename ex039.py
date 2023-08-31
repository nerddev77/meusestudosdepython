print('Bem-Vindo ao Alistamento Militar')
anodenascimento = int(input('Digite a data do seu nascimento: '))
idade = 2023 - anodenascimento
minimodeidade = 18 - idade
divida = idade - 18

if anodenascimento > 2005:
    print(f'Você ainda não precisa se alistar, pois tem {idade} e ainda falta(m) {minimodeidade} ano(s).')
elif anodenascimento == 2005:
    print(f'Parabéns pelos 18 anos! Agora você precisa se alistar para o exército!')
elif anodenascimento < 2005:
    print(f'Você precisa se alistar para o Serviço Militar, pois tem {idade} e já faz(em) {divida} ano(s) que você está em dívida.')