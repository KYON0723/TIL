```python
import sys

sys.stdin = open('input.txt', 'r')

# 숫자 입력 받음
numbers = list(map(int, input().split()))

# 각 번호별 연결된 번호 저장용 list
temp = [[] for _ in range(10)]

# list 는 현재 번호, 연결된 번호 순으로 되어 있으므로 앞에서 2개 pop, num1 index에 num2값 추가 반복
while numbers:
    num1 = numbers.pop(0)
    num2 = numbers.pop(0)

    temp[num1].append(num2)

# 중복 되지 않는 번호를 저장할 list
stack = []

# temp 내의 각 index 별로 pop, 중복 값이 아니면 stack에 추가
for i in temp:
    while i:
        num = i.pop(0)
        if num not in stack:
            stack.append(num)

# 시작은 1번 부터
res = '1'

# stack 값을 하나씩 추출하여 결과 형식에 맞게 추가
while stack:
    res += '-' + str(stack.pop(0))

# 출력
print(res)
```

> BFS 구현
