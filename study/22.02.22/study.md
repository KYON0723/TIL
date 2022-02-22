```python
import sys

sys.stdin = open('input.txt', 'r')

# 규칙 찾기
# 1   2   3   4   5   6 ...
# 1   3   5  11  21  43 ...
# A(n) = A(n-1) + 2 * A(n-2)
# A(1) = 1, A(2) = 3


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + 2 * paper(n-2)


# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # 바닥 = 20 x N
    N = int(input())

    n = N // 10

    res = paper(n)

    print(f'#{t} {res}')
```

> 4869 종이붙이기

> ![설명용](../../../../Desktop/설명용.jpg)

> 위 그림과 같은 규칙을 따른다.
