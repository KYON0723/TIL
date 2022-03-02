```python
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    # 노선 수
    N = int(input())

    # 버스 정보
    bus = [list(map(int, input().split())) for _ in range(N)]

    # 길 만들기
    road = [0] * 1001

    for i in range(N):
        # bus[i][0] -> 버스 번호 / bus[i][1] -> 시작 위치 / bus[i][2] -> 도착 위치
        if bus[i][0] == 1:
            for j in range(bus[i][1], bus[i][2]+1):
                road[j] += 1

        elif bus[i][0] == 2:
            # 홀수
            if bus[i][1] % 2:
                road[bus[i][1]] += 1
                for j in range(bus[i][1]+1, bus[i][2]):
                    if j % 2:
                        road[j] += 1
                road[bus[i][2]] += 1

            # 짝수
            else:
                road[bus[i][1]] += 1
                for j in range(bus[i][1]+1, bus[i][2]):
                    if not j % 2 :
                        road[j] += 1
                road[bus[i][2]] += 1

        elif bus[i][0] == 3:
            # 홀수
            if bus[i][1] % 2:
                road[bus[i][1]] += 1
                for j in range(bus[i][1]+1, bus[i][2]):
                    if not j % 3 and j % 10:
                        road[j] += 1
                road[bus[i][2]] += 1

            # 짝수
            else:
                road[bus[i][1]] += 1
                for j in range(bus[i][1]+1, bus[i][2]):
                    if not j % 4:
                        road[j] += 1
                road[bus[i][2]] += 1

    max_num = 0

    for i in road:
        if i > max_num:
            max_num = i

    print(f'#{t+1} {max_num}')

```

> 버스 문제
