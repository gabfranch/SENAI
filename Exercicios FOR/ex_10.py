faturamento = 0

for loop in range(1,6):
    cliente = float(input('Digite o valor da compra do {loop}º cliente: '))
    faturamento += cliente

if faturamento > 54000:
    print(f'O faturamento da loja A superou por R$ {faturamento - 54000:.2f}: a loja B')
else:
    print('O faturamento da loja A não superou a loja B')