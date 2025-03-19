def ler_inteiro(num):
    return int(num)

while True:
    num = input('Digite um número: ')
    
    try:
        ler_inteiro(num)
    except ValueError:
        print('Valor inválido! Digite um número inteiro.')
    else:
        break