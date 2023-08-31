from random import randint
from time import sleep

numaleatorio = randint(0,5) # Sorteia um número

print('-=-' * 10)
print ('Vou pensar em um número entre 0 e 5')
print('-=-' * 10)

print ('PENSANDO...')
sleep(1)
print ('Pronto, tente adivinhar em que número eu pensei!')

player = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
if player == numaleatorio:
    print('Você é BRABO, parabéns!')
else:
    print(f'Não foi dessa vez, eu pensei no número {numaleatorio} e não no {player}')



