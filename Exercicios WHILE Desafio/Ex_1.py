num = int(input('Digite um número: '))
sequencia = [0, 1]
loop = 0

while True:

    if sequencia[-1] > num:
        sequencia.remove(sequencia[-1])
        break

    else:
        sequencia.append(sequencia[loop] + sequencia[loop + 1])
        loop += 1

print(*sequencia)