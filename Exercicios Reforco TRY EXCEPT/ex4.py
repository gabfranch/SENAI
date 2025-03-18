def divisao_segura(num1, num2):
    return num1 / num2

while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))

        resultado = divisao_segura(num1, num2)

    except ZeroDivisionError:
        print('Divisão por zero! Digite um valor maior que zero.')

    except ValueError:
        print('Valor invalido! Digite um número inteiro.')

    else:
        print(resultado)
        break