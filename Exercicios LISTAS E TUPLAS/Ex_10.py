decrescente = []
crescente = []

for loop in range(2):
    nums = [1, 50, 3, -5, 250920, 123, -589]

    for sub_loop in range(len(nums)):
        match loop:
            case 0:
                decrescente.append(max(nums))
                nums.remove(max(nums))

            case 1:
                crescente.append(min(nums))
                nums.remove(min(nums))


print(f'''Crescente: {crescente}
Decrescente: {decrescente}''')