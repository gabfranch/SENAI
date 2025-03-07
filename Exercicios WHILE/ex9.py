num = int(input('Digite um número: '))
pares = 0

while num != -1:
    if num % 2 == 0:
        pares += 1
    num = int(input('Digite um número: '))

print(f'O total de números pares foi: {pares}')