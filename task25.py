n = int(input('n: '))
total = 0

for i in range(1, n + 1):
    yosh = int(input(f'yosh{i}: '))
    total += yosh

print(total/5)
