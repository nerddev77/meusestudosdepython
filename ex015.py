# O preço de cada km é R$ 0,15 centavos e a diária é R$ 60,00

dias = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos KM você rodou com o carro ao total?'))
total = km * 0.15 + 60 * dias
print(f'O total da viagem andando {km}, e com {dias} usando o carro, ficou R${total :.2f}')