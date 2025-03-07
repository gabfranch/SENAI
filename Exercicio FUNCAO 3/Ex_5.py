def soma_lista(lista):
    return sum(lista)

while True:
    try:
        nums = list(map(int, input('Digite uma sequência de números separados por espaço: ').split(sep=' ')))
        print(soma_lista(nums))
        break
    
    except ValueError:
        print('Valor(es) inválido(s)! Digite uma sequência de números separados por espaço')