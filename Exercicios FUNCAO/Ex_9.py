def vogais(palavra):
    vogais = 'aeiou'
    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1

    return contador

print(f'Há {vogais('Banana')} vogal(is)')