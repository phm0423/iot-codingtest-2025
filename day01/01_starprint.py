n = int(input('최대 별크기 입력: '))
sum = 0
for i in range(n):
    print("*" * (i+1))
    sum += i+1
print(f'sum: {sum}')
