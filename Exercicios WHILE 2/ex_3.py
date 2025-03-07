nota = int(input('Digite uma nota: '))
soma = 0
num_notas_inseridas = 0

while True:
    
    nota = int(input('Digite novamente uma nota (Digite -1 para cancelar): '))
    soma += nota
    num_notas_inseridas += 1

    if nota == -1:
        break

media = soma / num_notas_inseridas

print(f'A média é: {media:.2f}')