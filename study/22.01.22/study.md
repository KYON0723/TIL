```python
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print('--- 기본형태 ---')
for i in lst:
    print(i)

# 전치
print('--- 전치행렬 ---')
lst2 = list(map(list, zip(*lst)))
for i in lst2:
    print(i)
    
    
print('--- 반시계 90도 ---')
lst3 = list(zip(*lst))[::-1]
for i in lst3:
    print(i)
    
    
print('--- 시계 90도 ---')
lst4 = list(zip(*lst[::-1]))
for i in lst4:
    print(i)
```

