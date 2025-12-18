n = int(input('n ni kiriting: '))

Juft_yigindi = 0

for son in range(1, n+1):
    if son % 2 == 0:
        Juft_yigindi += son
    
print(f'Juft: {Juft_yigindi}')