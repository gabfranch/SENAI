def multiplicar(num1, num2):
    return num1 * num2

while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))

        produto = multiplicar(num1, num2)

    except ValueError:
        print('Valor inválido! Digite somente números inteiros (..., -2, -1, 0, 1, 2, ...).')

    else:
        print(produto)
        break