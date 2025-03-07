lista = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

def positivo(lista):
    positivos = 0

    for num in lista:
        if num >= 0:
            positivos +=1
    
    return positivos

print(positivo(lista))