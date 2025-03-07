num_secreto = 7
tentativa = int(input('Digite o número secreto: '))

while tentativa != num_secreto:
    print('Número inválido!')
    tentativa = int(input('Digite o número secreto: '))

print('Número correto!')