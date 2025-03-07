num = int(input('Digite um número: '))
numeros = []

while num != 0:
    numeros.append(num)
    num = int(input('Digite um número: '))

print(f'O maior número que você digitou foi: {max(numeros)}')