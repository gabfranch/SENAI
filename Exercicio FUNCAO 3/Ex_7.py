def pegar_elemento(lista, indice):
    return lista[indice]

while True:
    try:
        lista = input('Digite uma lista: ').split(sep=', ')
        indice = int(input('Digite o índice: '))

        print(pegar_elemento(lista, indice))
        break

    except:
        print('O índice não existe!')
