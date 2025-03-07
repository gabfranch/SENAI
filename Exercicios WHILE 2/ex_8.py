total = 0

while True:
    
    while True:
        
        valor_produtos = float(input('Olá! Insira o valor dos produtos: '))
        total += valor_produtos

        if valor_produtos == 0:
            break


    while True:

        print(f'Valor total da compra: R$ {total:.2f}')

        valor_pago = float(input('Digite o valor a ser pago: '))

        if valor_pago > total:
            print(f'Compra realizada! O troco será de R$ {valor_pago - total:.2f}')
            
            total = 0
            break

        elif valor_pago < total:
            print(f'Valor insuficiente!')
            continue

        else:
            print('Compra realizada!')

            total = 0
            break