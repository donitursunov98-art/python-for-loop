n = int(input('n: '))
total = 0

for i in range(1, n +1):
    narx = float(input(f'mahsulot narxi{i}: '))
    chegirma_narx = narx * 0.9   
    total += chegirma_narx
           
print(total)
