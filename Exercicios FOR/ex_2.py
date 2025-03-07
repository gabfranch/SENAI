num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    num1, num2 = num2, num1

for nums in range(num1+15, num2):
    print(nums)