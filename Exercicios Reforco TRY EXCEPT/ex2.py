def ler_inteiro(num):
    return int(num)

num = input('Digite um número: ')

while True:
    try:
        ler_inteiro(num)
    except ValueError:
        print('Valor inválido! Digite um número inteiro.')
        num = input('Digite um número: ')
    else:
        break