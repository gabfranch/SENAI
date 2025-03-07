senha_correta = 'opato123'
tentativa = input('Digite a senha: ')

while True:

    print('Senha inválida! Digite novamente.')
    tentativa = input('Digite a senha: ')

    if tentativa == senha_correta:
        print('Senha correta!')
        break
