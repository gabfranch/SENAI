valor_total = 0

while True:
        
    codigo_prod = int(input('PRODUTOS:\n\n #1 Pão (1kg) - R$ 10\n #2 Presunto - R$ 50\n #3 Queijo - R$ 7\n #4 Arroz - R$ 5\n #5 Carne (1kg) - R$ 30\n #6 Frango (1kg) - R$ 20\n #7 Sorvete - R$ 23\n\nDigite o código do produto: '))
    
    if codigo_prod == 0:
        break
    elif codigo_prod > 7 or codigo_prod < 0:
        print('\nDigite um código válido!\n')
        continue

    quantidade_prod = int(input('Digite a quantidade: '))

    match codigo_prod:
        case 1:
            valor_total += 10 * quantidade_prod
        case 2:
            valor_total += 50 * quantidade_prod
        case 3:
            valor_total += 7 * quantidade_prod
        case 4:
            valor_total += 5 * quantidade_prod
        case 5:
            valor_total += 30 * quantidade_prod
        case 6:
            valor_total += 20 * quantidade_prod
        case 7:
            valor_total += 23 * quantidade_prod

    print(f'Valor total: {valor_total}\n')

print(f'\nValor total: {valor_total}')