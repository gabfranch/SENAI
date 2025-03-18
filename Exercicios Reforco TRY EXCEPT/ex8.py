def contar_caracteres(texto, caractere):
    return texto.count(caractere)

texto = 12366

while True:
    caractere = input('Digite um caractere para contar: ')

    try:
        resultado = contar_caracteres(texto, caractere)

    except:
        print('Valor inválido! Digite um texto.')
        texto = input('Digite um texto: ')

    else:
        print(resultado)
        break