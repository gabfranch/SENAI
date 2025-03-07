def ler_inteiro(num):
    return num
    
num = input('Digite um número inteiro: ')

while True:
    try:
        print(ler_inteiro(int(num)))
        if int(num):
            break 
        
    except ValueError:
        print('Valor inválido! Digite um número inteiro!')
        num = input('Digite um número inteiro: ')