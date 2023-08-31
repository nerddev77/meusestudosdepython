produto = float(input('Qual é o preço do produto?'))
desconto = int(input('Qual é o desconto desejado?'))
calc = produto*desconto/100
final = produto - calc
print(f'O preço antigo era {produto}, mas com o desconto de {desconto}%, o produto vai sair {final}R$')