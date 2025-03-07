pares = 0
impares = 0

for loop in range(1, 11):
    num = int(input('Digite um número: '))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')