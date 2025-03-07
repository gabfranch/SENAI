num = int(input('Digite um número: '))
num_anterior = 0
nums_inseridos = 0

while True:
    nums_inseridos += 1
    num = int(input('Digite outro número: '))

    if num == num_anterior:
        break

    num_anterior = num

print(nums_inseridos)