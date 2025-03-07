gumball, finn, steven, mordecai, nulo, branco = 0, 0, 0, 0, 0, 0

while True:
    voto = int(input('''CANDIDATOS:
    
    (1) Gumball
    (2) Finn
    (3) Steven
    (4) Mordecai
    (5) Nulo
    (6) Branco
                     
Para votar, digite o número do candidato: '''))

    match voto:
        case 0:
            break
        case 1:
            gumball += 1
        case 2:
            finn += 1
        case 3:
            steven += 1
        case 4:
            mordecai += 1
        case 5:
            nulo += 1
        case 6:
            branco += 1
        case _:
            print('\nDigite um número válido! \n')
            continue

total = gumball + finn + steven + mordecai + nulo + branco

print(f'TOTAL DE VOTOS:\n\n Gumball: {gumball}\n Finn: {finn}\n Steven: {steven}\n Mordecai: {mordecai}\n Nulo: {nulo / total * 100:.2f}%\n Branco: {branco / total * 100:.2f}%')