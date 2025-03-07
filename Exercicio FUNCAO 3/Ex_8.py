def contar_caracteres(texto, caractere):
    return texto.count(caractere)

while True:
    try:
        texto = input('Digite um texto: ')
        caractere = input('Digite um caractere: ')
        
        if str(texto):
            print(contar_caracteres(texto, caractere))
            break
        else:
            print(contar_caracteres(texto, caractere))

    except:
        print('O texto não é do tipo string!')