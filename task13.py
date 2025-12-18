qavat_soni = int(input("Qavat soni: "))

umumiy_balandlik = 0

for i in range(1, qavat_soni + 1):
    balandlik = float(input(f'qavat balandligi {i}: '))
    umumiy_balandlik += balandlik 

print(umumiy_balandlik)
