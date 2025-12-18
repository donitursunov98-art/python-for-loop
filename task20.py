son = int(input(f'son1: '))
max_son = son
min_son = son

for i in range(2, 6):
    son = int(input(f'son{i}: '))
    if son > max_son:
        max_son = son
    if son < min_son:
        min_son = son
    total = (max_son + min_son)/2

print(total)
