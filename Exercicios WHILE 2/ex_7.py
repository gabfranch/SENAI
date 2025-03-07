paisA = 80000
paisB = 200000
taxa_paisA = 0.03
taxa_paisB = 0.015
anos = 0

while True:

    if paisA > paisB:
        print(f'O país A irá superar o B em: {anos} anos')
        break
    
    else:
        paisA *= (taxa_paisA + 1)
        paisB *= (taxa_paisB + 1)
        anos += 1