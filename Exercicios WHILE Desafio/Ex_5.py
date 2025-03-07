from decimal import *

num = int(input('Digite um número: '))

while True:
    if Decimal((num ** (1/2))) * Decimal((num ** (1/2))) == num:
        print('Quadrado perfeito!')
        num = int(input('Digite um número: '))

    else:
        print('Não é um quadrado perfeito!')
        num = int(input('Digite um número: '))

    match num:
        case 0:
            break