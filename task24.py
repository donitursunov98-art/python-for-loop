n = int(input('n: '))
total = 0

for i in range(1, n + 1):
    ball = int(input(f'ball{i}: '))
    total += ball

print(total)
