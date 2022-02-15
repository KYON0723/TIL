```python
import sys

sys.stdin = open('input.txt', 'r')

# testcase 수
T = int(input())

for t in range(T):
    # N, M
    N, M = map(int,(input().split()))

    # N x N 격자
    cw = [list(map(int, input().split())) for _ in range(N)]

    res = 0

    for i in range(N):
        cnt = 0

        # 행을 검사
        for j in range(N):
            if cw[i][j] == 1:
                cnt += 1

            # 0을 만나거나 끝에 도달하면 cnt 초기화
            if cw[i][j] == 0 or j == N - 1:
                # 종료시 칸이 M만큼 있으면 res에 추가
                if cnt == M:
                    res += 1
                cnt = 0

        # 열을 검사
        for j in range(N):
            if cw[j][i] == 1:
                cnt += 1

            # 0을 만나거나 끝에 도달하면 cnt 초기화
            if cw[j][i] == 0 or j == N - 1:
                # 종료시 칸이 M만큼 있으면 res에 추가
                if cnt == M:
                    res += 1
                cnt = 0

    print(f'#{t+1} {res}')


```

> 어디에 단어가
