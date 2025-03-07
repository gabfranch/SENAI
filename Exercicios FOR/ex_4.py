soma = 0

for loop in range(1,6):
    nums = int(input(f'Digite o {loop}º número: '))
    soma += nums

media = soma / 5

print(f'A soma é {soma} e a média é {media}')