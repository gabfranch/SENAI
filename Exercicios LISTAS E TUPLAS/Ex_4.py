num = int(input('Digite um número para verificar se está presente na lista: '))

nums = [1, 2, 3, 4, 5]

if num in nums:
    print(f'O número está presente na lista!')
else:
    print(f'O número não está presente na lista!')