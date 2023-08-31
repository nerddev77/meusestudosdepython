print('=== NERD INC ===')
preço = float (input("Digite o preço total: "))

opcao = int(input('''FORMAS DE PAGAMENTO
      [ 1 ] à vista no dinheiro/PIX
      [ 2 ] à vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão
      Digite o número da opção desejada
'''))

if opcao == 1:
    total = preço - (preço * 10/100)
    print('Parabéns você recebeu 10% de desconto!')
    print(f'O preço final vai ficar {total}')
elif opcao == 2:
    total = preço - (preço * 5/100)
    print('Parabéns você recebeu 5% de desconto!')
    print(f'O preço final vai ficar {total}')
elif opcao == 3:
    preço 
    print(f'O preço final vai ficar {preço}')
elif opcao == 4:
    total = preço + (preço * 20/100)
    print('A compra teve um acréscimo de 20%!')
    print(f'O preço final vai ficar {preço}')
else:
    print('Insira uma opção válida')
    opcao()