```python
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

# 부분 집합 초기값
subsets = [[]]

# 부분 집합 생성
for num in arr:
    for i in range(len(subsets)):
        subsets.append(subsets[i]+[num])

# 원소 합이 0인 부분 집합 출력
for item in subsets:
    hap = 0
    for i in item:
        hap += i

    if not hap:
        print(item)

```

> 부분집합 생성 + 합이 0인 부분집합 출력
