```python
# 상 하 좌 우 / 문제에 맞춰 0번 인덱스 비움
y = [0, -1, 1, 0, 0]
x = [0, 0, 0, -1, 1]

T = int(input())

for t in range(1, T+1):
    # 한 변 셀의 수 N, 격리 시간 M, 군집 개수 K
    N, M, K = map(int, input().split())

    # 군집의 정보
    arr = [list(map(int, input().split())) for _ in range(K)]

    for i in range(M):
        cnt = -1

        # 방문 여부 확인
        vis = [[0] * N for _ in range(N)]

        for j in arr:
            cnt += 1

            # 남은 미생물 존재
            if j[2]:
                # 세로 위치 이동
                ny = j[0] + y[j[3]]

                # 가로 위치 이동
                nx = j[1] + x[j[3]]

                # 약품 위치 도달
                if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                    # 미생물 수 절반
                    j[2] = j[2] // 2

                    # 방향 전환
                    if j[3] == 1 or j[3] == 3:
                        j[3] += 1

                    else:
                        j[3] -= 1

                else:
                    # vis 해당 위치에 값이 없음
                    if not vis[ny][nx]:
                        # 개체수 합 , 방향을 위한 최대 개체 표시 , 시행 횟수
                        vis[ny][nx] = [j[2], j[2], cnt]

                    # 값이 있음
                    else:
                        # 기존 최대 값 개체수 > 도착한 개체수
                        if vis[ny][nx][1] > j[2]:
                            # 개체수 합 증가
                            vis[ny][nx][0] += j[2]

                            # arr 의 미생물 수 변경
                            arr[vis[ny][nx][2]][2] = vis[ny][nx][0]

                            # 합친 후 기존 값 0 으로 변경
                            j[2] = 0

                        else:
                            # 개체수 합 증가
                            vis[ny][nx][0] += j[2]

                            # 최대 개채수 개체 변경
                            vis[ny][nx][1] = j[2]

                            # arr 의 미생물 수 변경
                            arr[vis[ny][nx][2]][2] = 0

                            # cnt 값 갱신
                            vis[ny][nx][2] = cnt

                            # 합산한 값으로 현재 미생물 수 변경
                            j[2] = vis[ny][nx][0]

                # 좌표 변경
                j[0] = ny
                j[1] = nx

    # 남은 미생물 수 합산
    hap = 0
    for i in arr:
        hap += i[2]

    # 출력
    print(f'#{t} {hap}')
```

> 2382 - 미생물 격리
