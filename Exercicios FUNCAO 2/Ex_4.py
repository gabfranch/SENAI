palavras = ['Pablo ', 'comeu ', 'coxinha ', 'quente']

def juntar_palavras(palavras):
    frase = ''

    for palavra in palavras:
        frase += palavra

    return frase

print(juntar_palavras(palavras))
