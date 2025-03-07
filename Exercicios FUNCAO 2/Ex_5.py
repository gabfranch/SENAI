nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

def negativo_para_zero(lista):
    for num in nums:
        if num < 0:
            nums[nums.index(num)] = 0

    return nums

print(negativo_para_zero(nums))
