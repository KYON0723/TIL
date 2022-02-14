```python
import sys

sys.stdin = open('input.txt', 'r')

# testcase 수
T = int(input())

for t in range(T):
    # 행 열 길이
    N = int(input())

    # N행 N열의 빈 행렬 생성(값을 전부 0으로 채움)
    result = [[0] * N for i in range(N)]

    i, j, index = 0, -1, 0
    dir = ["Right", "Down", "Left", "Up"]
    value = 1

    # 각 자리에 K 숫자를 넣음
    for k in range(N * N):
        # 오른쪽으로 진행 / 천장에 막혀 되돌아 오면 다시 오른쪽으로 진행
        if dir[index] == "Right":
            j += 1
            if j >= N or result[i][j] != 0:
                i += 1
                j -= 1
                index = 1

        # 벽에 막히면 아래로 진행
        elif dir[index] == "Down":
            i += 1
            if i >= N or result[i][j] != 0:
                i -= 1
                j -= 1
                index = 2

        # 바닥에 막히면 왼쪽으로 진행
        elif dir[index] == "Left":
            j -= 1
            if j < 0 or result[i][j] != 0:
                i -= 1
                j += 1
                index = 3

        # 벽에 막히면 위로 진행
        elif dir[index] == "Up":
            i -= 1
            if i < 0 or result[i][j] != 0:
                i += 1
                j += 1
                index = 0
        result[i][j] = value
        value += 1

    print(f'#{t+1}')
    for i in range(N):
        print(*result[i])

```

> snail 문제
