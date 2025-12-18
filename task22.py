narx = int(input(f'narx1: '))
max_narx = narx
min_narx = narx

for i in range(2, 6):
    narx = int(input(f'narx{i}: '))
    if narx > max_narx:
        max_narx = narx
    if narx < max_narx:
        min_narx = narx
    total = (max_narx + min_narx)/2

print(total)
