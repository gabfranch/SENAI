def calculadora(num1, num2, operacao):
    match operacao:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        
num1 = input('Digite um número: ')
operacao = input('Digite a operação: ')
num2 = input('Digite outro numero: ')

try:
    resultado = calculadora(int(num1), int(num2), operacao)

except ValueError:
    print('Valor inválido! Digite um número.')

except ZeroDivisionError:
    print('Divisão por zero! Digite outro número diferente de zero.')

else:
    print(resultado)