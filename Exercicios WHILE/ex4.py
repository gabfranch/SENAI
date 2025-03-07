senha = '1234'
tentativa = input('Digite a senha: ')

while tentativa != senha:
    print('Senha errada!')
    tentativa = input('Digite a senha: ')

print('Senha correta!')