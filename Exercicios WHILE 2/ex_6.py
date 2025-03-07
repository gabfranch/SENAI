nota = int(input('Digite uma nota entre 0 e 10: '))

while True:

    if nota >= 0 and nota <= 10:
        break
    
    else:
        print('Nota inválida!')
        nota = int(input('Digite uma nota entre 0 e 10: '))