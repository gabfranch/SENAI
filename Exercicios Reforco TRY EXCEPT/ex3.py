def calcular_media(lista):
    return sum(lista) / len(lista)

lista = map(int, input('Digite uma lista de números (separe-os por espaço): ').split(sep=' '))

while True:
    try:
        calcular_media(list(lista))
    except:
        print('Lista vazia!')
        lista = map(int, input('Digite uma lista de números (separe-os por espaço): ').split(sep=' '))
    else:
        break

