def divisao_segura(a, b):
    return a / b

while True:
    try:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        if num2 != 0:
            print(divisao_segura(num1, num2))
            break
        else:
            print(divisao_segura(num1, num2))
    except:
        print('Erro: Divisão por zero não permitida!')