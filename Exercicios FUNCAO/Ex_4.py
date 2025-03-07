def fatorial(num):
    for loop in range(1, num):
        num *= loop
    return num

print(f'Fatorial: {fatorial(4)}')