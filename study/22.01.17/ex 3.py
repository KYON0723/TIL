# 1~30 중 홀수만

# 1-1. 반동
numbers = []
for i in range(1, 31):
    if i % 2 == 1:
        numbers.append(i)
print(numbers)

numbers_2 = [ i for i in range(1, 31) if i % 2 == 1]
print(numbers_2)
