```python
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    A = input()

    stack = []
    res = ''

    # 우선 순위 설정
    rank = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    for a in range(len(A)):
        if A[a] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            res += A[a]

        elif A[a] == '(':
            stack.append(A[a])

        elif A[a] == ')':
            while stack[-1] != '(':
                res += stack.pop()

            # ( 는 pop 처리
            stack.pop()

        else:
            while stack and rank[A[a]] <= rank[stack[-1]]:
                res += stack.pop()

            stack.append(A[a])

    while len(stack) != 0:
        res += stack.pop()

    print(f'#{t} {res}')

```

> 1224 - 계산기 3
