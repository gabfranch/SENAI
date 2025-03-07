five_nums = []

for num in range(1, 6):
    nums = int(input(f'Digite o {num}º número: '))

    five_nums.append(nums)

print(max(five_nums))