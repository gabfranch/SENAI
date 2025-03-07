nome_pais = input('Escreva o nome de um país: ')

paises = ['Suécia', 'Suíça', 'Serra Leoa', 'Suriname', 'Suécia', 'Síria']
contador = 0

for pais in paises:
    if nome_pais == pais:
        contador += 1

print(f'{nome_pais} aparece {contador} vezes!')