def palindromo(palavra):
    if palavra[::-1] == palavra:
        return f'A palavra {palavra} é um palíndromo!'
    else:
        return f'A palavra {palavra} não é um palíndromo!'
    
print(palindromo('marcos'))