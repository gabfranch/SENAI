num = int(input('Digite um número acima de 2: '))
intervalo = 2

while True:
    intervalo += 2
    print(intervalo)

    if intervalo == num or intervalo == (num + 1) or intervalo == (num - 1):
        break