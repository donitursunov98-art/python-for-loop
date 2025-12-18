total = 0

for i in range(1, 8):
    yosh = int(input(f'yosh {i}: '))
    if yosh < 21:
        total += 1

print(f"21 yoshdan kichik talabalar soni: {total}")
