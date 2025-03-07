ate15 = 0
ate30 = 0
ate45 = 0
ate60 = 0
acima61 = 0

for pessoa in range(1, 16):
    idade = int(input('Digite a sua idade: '))

    match idade < 16, idade < 31, idade < 46, idade < 61, idade > 60:
        case True, True, True, True, False:
            ate15 += 1
        case False, True, True, True, False:
            ate30 += 1
        case False, False, True, True, False:
            ate45 += 1
        case False, False, False, True, False:
            ate60 += 1
        case False, False, False, False, True:
            acima61 += 1

print(f'Até 15 anos: {ate15} pessoas, {ate15 / pessoa * 100:.2f}%')
print(f'De 16 a 30 anos: {ate30} pessoas, {ate30 / pessoa * 100:.2f}%')
print(f'De 31 a 45 anos: {ate45} pessoas, {ate45 / pessoa * 100:.2f}%')
print(f'De 46 a 60 anos: {ate60} pessoas, {ate60 / pessoa * 100:.2f}%')
print(f'Acima de 61 anos: {acima61} pessoas, {acima61 / pessoa * 100:.2f}%')

