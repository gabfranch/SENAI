num = int(input('Digite um número: '))
maior = 0

while True:
    num = int(input('Digite novamento um número (Digite um número negativo para cancelar): '))

    if num > maior:
        maior = num

    elif num < 0:
        break

print(maior)
    

