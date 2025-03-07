def calcular_media(lista):
     return sum(lista) / len(lista)

while True:
    try:
        nums = list(map(int, input('Digite uma sequência de números (separe por espaços): ').split(sep=' ')))
        if len(nums) != 0:
            print(calcular_media(nums))
            break
    except:
        print('Nenhum número inserido. Digite uma sequência de números separando por espaços: ')