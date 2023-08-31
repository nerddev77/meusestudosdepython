print('-='*20)
print('Bem-Vindo a Calculadora de IMC')
print('-='*20)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f}, você está no quadro de MAGREZA')
elif imc >= 18.6 and imc <= 24.9:
    print(f'Seu IMC é {imc:.2f}, você está no quadro NORMAL')
elif imc >= 25.0 and imc <= 29.9:
    print(f'Seu IMC é {imc:.2f}, você está no SOBREPESO')
elif imc >= 30.0 and imc <= 39.9:
    print(f'Seu IMC é {imc:.2f}, você está no quadro de OBESIDADE')
else:
    print(f'Seu IMC é {imc:.2f}, você está no quadro de OBESIDADE GRAVE')