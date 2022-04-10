```python
# 위 오 아 왼
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def cal(x, y):
    # 가지 치기
    if vis[y][x] > vis[N - 1][N - 1]:
        return

    # 종료 조건
    if x == N-1 and y == N-1:
        return

    # 4방향 진행
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 확인
        if 0 <= nx < N and 0 <= ny < N:
            # vis 값 변경
            if vis[y][x] + arr[ny][nx] < vis[ny][nx]:
                vis[ny][nx] = vis[y][x] + arr[ny][nx]

                # 재귀
                cal(nx, ny)


# 테스트 케이스 수
T = int(input())
for t in range(1, T+1):
    # N * N 행렬
    N = int(input())

    # 데이터 입력 받음
    arr = []
    for i in range(N):
        tem_1 = input()
        tem_2 = []
        for j in tem_1:
            tem_2.append(int(j))
        arr.append(tem_2)

    # 값 저장용 vis 생성
    temp = 987654321
    vis = [[temp for _ in range(N)] for _ in range(N)]

    # 시작 위치 초기화
    vis[0][0] = 0

    # 함수 시행
    cal(0, 0)

    # 결과 출력
    print(f'#{t} {vis[N-1][N-1]}')

```

> 1249 - 보급로
