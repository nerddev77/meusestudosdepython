nome = input('Digite o nome do aluno(a)')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
notafinal = (n1 + n2 + n3 + n4) / 4
print(f'A nota de {nome} é {notafinal:.2f}')