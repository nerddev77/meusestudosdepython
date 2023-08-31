#Fazer um software que passe o aluno caso ele tire uma nota maior que 5 uau

print('Bem-Vindo ao Passador/Lasca Aluno')
aluno = str(input('Digite o nome do(a) lascado(a)'))

#notas
nota1 = float(input('Digite a nota de Português: '))
nota2 = float(input('Digite a nota de Matemática: '))
nota3 = float(input('Digite a nota de História: '))
nota4 = float(input('Digite a nota de Geografia: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if 7 > media >=5 :
    print(f'RECUPERAÇÃO {aluno} pois tirou {media :1f}')
elif media < 5:
    print(f'Você está reprovado {aluno}, pois tirou {media :1f} de média.')
elif media >= 7:
    print(f'Parabéns {aluno}! Você está aprovado!')