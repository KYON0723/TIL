```python
import sys

sys.stdin = open('input.txt', 'r')

# testcase 수
T = int(input())

for t in range(T):
    # 정수 N (N x N 배열)
    N = int(input())

    # N X N 배열 채우기
    BOX = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전 (N x N 빈 배열을 만들고 채워 넣음)
    BOX_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            BOX_90[i][j] = BOX[N-(j+1)][i]

    # 180도 회전 (N x N 빈 배열을 만들고 채워 넣음)
    BOX_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            BOX_180[i][j] = BOX[N-(i+1)][N-(j+1)]

    # 270도 회전 (N x N 빈 배열을 만들고 채워 넣음)
    BOX_270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
           BOX_270[i][j] = BOX[j][N-(i+1)]

    # 형식 맞게 출력
    print(f'#{t+1}')
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += str(BOX_90[i][j])
        temp += ' '

        for j in range(N):
            temp += str(BOX_180[i][j])
        temp += ' '

        for j in range(N):
            temp += str(BOX_270[i][j])

        print(temp)
```

> 1961 숫자 배열 회전
