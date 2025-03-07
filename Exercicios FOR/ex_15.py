desconto = 0

for valor_da_compra in range(500, 2901, 100):
    desconto += 0.01
    print(f'Valor da Compra: {valor_da_compra} - Desconto: {desconto * 100:.0f}% - Valor Final: {valor_da_compra - (valor_da_compra * desconto):.2f}')