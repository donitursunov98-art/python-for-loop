n = int(input('n: '))
a = int(input('a: '))
total = 0

for i in range(1, n + 1):
    darmoad = int(input(f'darmoad{i}: '))
    total += darmoad

print(total/a)
