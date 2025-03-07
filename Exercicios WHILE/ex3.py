numero = int(input('Digite um número: '))
soma = 0

while numero != 0:
    soma += numero
    numero = int(input('Digite um número: '))

print(f'Soma: {soma}')