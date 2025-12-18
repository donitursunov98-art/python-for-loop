n = int(input('n: '))
total = 0

for i in range(1, n + 1):
    summa = int(input(f'telefon narxi{i}: '))
    if summa % 5 == 0:
        total += summa

print(total)
