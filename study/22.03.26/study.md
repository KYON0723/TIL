```python
# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # N : 한 변 길이 / M : 돌을 놓는 횟수
    N, M = map(int, input().split())

    # 진행 상황 저장용
    arr = [[0] * N for _ in range(N)]

    # 8가지 방향을 담음 (오른쪽 부터 대각선 포함 시계 방향)
    delta = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    # 중앙 위치 / 1 : 흑 / 2 : 백
    mid = N // 2

    # 중앙 4군데 기본 돌 배치
    arr[mid][mid] = 2
    arr[mid-1][mid-1] = 2
    arr[mid][mid-1] = 1
    arr[mid-1][mid] = 1

    # M 번 시행
    for _ in range(M):
        # 행렬 좌표 값이 설명 에서 나온 좌표 값과 반대 -> 설명은 (x, y)로 하지만 실제로 (y, x)로 주어짐
        # 따라서 반대로 y, x, 색 으로 정보를 입력 받음
        y, x, color = map(int, input().split())

        # 인덱스 : -1 값
        y -= 1
        x -= 1

        # 돌을 놓을 곳이 없다면 차례를 넘김
        if not arr[x][y]:
            arr[x][y] = color

            # 위에 설정한 8방향에 맞춰 검사 진행
            for i in range(8):
                dx, dy = delta[i]
                nx, ny = x + dx, y + dy

                # 뒤집을 좌표를 저장
                reverse = []

                while True:
                    # 경계값 이탈 확인
                    if nx < 0 or N - 1 < nx or ny < 0 or N - 1 < ny:
                        reverse = []
                        break

                    # 공백 확인
                    if arr[nx][ny] == 0:
                        reverse = []
                        break

                    # 같은 색을 만나면 멈춤
                    if arr[nx][ny] == color:
                        break

                    # 다른 색이면 좌표 저장
                    else:
                        reverse.append((nx, ny))
                    nx += dx
                    ny += dy

                # 검사 결과 대로 색을 바꿈
                for rx, ry in reverse:
                    arr[rx][ry] = color

    # 게임 진행이 끝남 -> 돌 개수 파악
    # 흰색, 검은색 개수 초기화
    W, B = 0, 0

    # 필드 전체를 돌며 갯수 파악
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                W += 1

            elif arr[i][j] == 2:
                B += 1

    # 형식에 맞춰 출력
    print(f'#{t} {W} {B}')
```

> 4615 - 오셀로 게임
