def pegar_elemento(lista, indice):
    return lista[indice]

while True:
    lista = input('Digite uma lista de palavras (separe-os por espaço): ').split(sep=' ')
    
    try:
        indice = int(input('Digite o índice: '))

        elemento = pegar_elemento(lista, indice)

    except ValueError:
        print('Valor inválido! Digite um número inteiro (..., -2, -1, 0, 1, 2, ...).')
    
    except:
        print('O índice não existe!')
    
    else:
        print(elemento)
        break