candidato1 = 0
candidato2 = 0
candidato3 = 0

eleitores = int(input('Número de eleitores: '))

for eleitor in range(eleitores + 1):
    voto = int(input('Vote em um candidato (1, 2 ou 3): '))

    match voto:
        case 1:
            candidato1 += 1
        case 2:
            candidato2 += 1
        case 3:
            candidato3 += 1

print(f'Candidato 1: {candidato1} votos')
print(f'Candidato 2: {candidato2} votos')
print(f'Candidato 3: {candidato3} votos')