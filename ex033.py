a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior

maior = a
if b > a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
