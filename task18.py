n = int(input('n ni kiriting: '))

toq_yigindi = 0

for son in range(1, n+1):
    if son % 2 == 1:
        toq_yigindi += son
    
print(f'Toq: {toq_yigindi}')