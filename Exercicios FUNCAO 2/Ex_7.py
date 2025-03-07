nums = [1, 20, 3, 40, 5, 60, 7, 80, 9, 100]

def soma_par(lista):
    soma = 0

    for num in lista:
        if num % 2 == 0:
            soma += num
    
    return soma

print(soma_par(nums))
