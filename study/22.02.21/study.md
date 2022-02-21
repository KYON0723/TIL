```python
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # N
    N = int(input())

    # N x N 행렬
    A = [[0]*N for _ in range(N)]

    # 파스칼 삼각형 구현
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                A[i][j] = 1

            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]

    # 형식에 맞게 출력
    print(f'#{t}')

    for i in range(N):
        temp = ''
        for j in range(i+1):
            temp += str(A[i][j]) + ' '

        print(temp)

```

> 2005 파스칼의 삼각형
