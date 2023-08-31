número = int (input('Digite um número inteiro: '))
print('''Escolha uma das base para conversão:
      [01] BINÁRIO
      [02] OCTAL
      [03] HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{número} convertuido para BINÁRIO é igual a {bin(número)[2:]}')
elif opção == 2:
    print(f'{número} convertido para OCTAL é igual a {oct(número)[2:]}')
elif opção == 3:
    print(f'{número} convertido para HEXADECIMAL é igual a {hex(número)[2:]}')
else:
    print('VALOR NÃO ACEITO')