lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiplos_3(lista):
    multiplos_3 = 0

    for num in lista:
        if num % 3 == 0:
            multiplos_3 += 1

    return multiplos_3

print(multiplos_3(lista))