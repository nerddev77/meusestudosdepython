frase = input(str('Digite uma frase: ')).strip().lower()
print(f'Sua frase tem {frase.count("a")} letra(s) A')
print(f'O primeiro A está na posição {frase.find("a")}')
print(f'O último A está na posição {frase.rfind("a")}')