```python
import sys
sys.stdin = open('input.txt', 'r')

# 방향 (상 하 좌 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 초기 x좌표 / y좌표
def find(i, j):
    # 시작점 0으로 초기화
    dis[i][j] = 0

    # q 생성
    q = []
    q.append((i, j))

    while q:
        x, y = q.pop(0)

        # 4방향 진행
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 범위 확인
            if 0 <= nx < N and 0 <= ny < N:
                # 높이 차 초기화
                diff = 0

                # 높이 차 계산 ( 더 높은 곳으로 갈 경우만 )
                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]

                # 연료 소모량 비교
                if dis[x][y] + 1 + diff < dis[nx][ny]:
                    # 최소 소모량 변경
                    dis[nx][ny] = dis[x][y] + 1 + diff

                    # 조건 만족할 경우만 다음 으로 진행
                    q.append((nx, ny))

    # 도착 지점 값 return
    return dis[N-1][N-1]


# 테스트 케이스 수
T = int(input())
for t in range(1, T+1):
    # 가로 세로 값
    N = int(input())

    # 높이 데이터
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 아주 큰값 으로 채워진 최소 소모량 배열 생성
    tem = 987654321
    dis = [[tem] * N for _ in range(N)]

    # 결과 출력
    print(f'#{t} {find(0, 0)}')

```

> 5250 - 최소비용
