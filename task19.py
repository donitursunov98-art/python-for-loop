son = int(input(f'son1: '))
max_son = son

for i in range(2, 6):
    son = int(input(f'son{i}: '))
    if son > max_son:
        max_son = son
  
print(max_son)
