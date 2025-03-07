for loop in range(1, 10000):
    nota = int(input('Dê uma nota de 0 a 10: '))

    if nota < 0 or nota > 10:
        print('Valor inválido!')

    else:
        print('Valor válido!')
        break