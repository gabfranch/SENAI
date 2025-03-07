palavras = ['Cachecol', 'Sorvete', 'Pato', 'Esfigmomanômetro', 'Carlos']

def maior_palavra(palavras):
    return max(palavras, key=len)

print(maior_palavra(palavras))

