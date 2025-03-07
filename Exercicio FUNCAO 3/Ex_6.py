def multiplicar(a, b):
    return a * b

while True:
    try:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        
        print(multiplicar(num1, num2))
        break

    except ValueError:
        print('Valor(es) inválido(s)! Digite número inteiro.')