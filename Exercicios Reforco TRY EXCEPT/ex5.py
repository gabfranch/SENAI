def soma_lista(lista):
    return sum(lista)

while True:
    lista = input('Digite uma lista de números (separe-os por espaço): ').split(sep=' ')
    
    try:
        lista = list(map(int, lista))

        soma = soma_lista(lista)

    except ValueError:
        print('Valor(es) inválido(s)! Digite somente números inteiros.')

    else:
        print(soma)
        break