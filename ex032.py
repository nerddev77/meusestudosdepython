from calendar import isleap

print('Bem-vindo ao Verificador de Ano Bissexto 3000')
ano = int(input('Digite o ano desejado: '))
if isleap(ano) == True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} NÃO é bissexto')
