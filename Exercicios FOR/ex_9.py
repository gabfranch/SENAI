num = int(input('Digite um número: '))
restos = []
zeros = 0

if num >= 2:
    for primo in range(1, num):
        resto = num % primo
        restos.append(resto)
        if resto == 0:
            zeros += 1

    print(zeros)

    if zeros < 3:
        print('Número é primo!')
    else:
        print('Número não é primo!')

else:
    print('Número não é primo!')