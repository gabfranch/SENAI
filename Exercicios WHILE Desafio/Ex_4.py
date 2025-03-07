num = int(input('Digite um número: '))
soma = 0

for nums in range(1, num):
    if num % nums == 0:
        soma += nums
        print(nums)
    else:
        continue

match soma == num:
    case True:
        print(f'{num} é um número perfeito!')
    case False:
        print('Não é um número perfeito')
