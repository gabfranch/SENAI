import math

pessoas = int(input('Digite o número de pessoas: '))
soma = 0
idades = []

for pessoa in range(1, pessoas+1):
    idade = int(input('Qual a sua idade? '))
    idades.append(idade)
    soma += idade

media = soma / pessoas


match media > 0, media > 25, media > 60:
    case True, False, False:
        print('A turma é jovem!')
    case True, True, False:
        print('A turma é adulta!')
    case True, True, True:
        print('A turma é velha!')
    case _:
        print('Média inválida!')