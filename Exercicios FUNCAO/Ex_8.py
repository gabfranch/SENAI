def media_das_notas(notas):
    return sum(notas) / len(notas)

print(f'A média das suas notas é {media_das_notas([10, 0, 8, 6, 3, 2, 1, 7]):.1f}')