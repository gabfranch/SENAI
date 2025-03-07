def calculadora(num1, num2, operacao):
    operacoes = '+-*/'
    if operacao not in operacoes:
        raise ValueError('Tipo de dado inválido!')
    
    match operacao:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
operacao = input('Digite a operação: ')

try:
    print(calculadora(int(num1), int(num2), operacao))
except ZeroDivisionError:
    print('Divisão por zero!')
except ValueError:
    print('Tipo de dado inválido!')