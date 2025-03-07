palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunda palavra: ')

def anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)
        
print(anagrama(palavra1, palavra2))