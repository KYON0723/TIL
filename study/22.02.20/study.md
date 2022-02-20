```python
import sys

sys.stdin = open('input.txt', 'r')

# testcase 수
T = int(input())

for t in range(T):
    # 정수 N (노선의 수)
    N = int(input())

    # N개의 줄 정수 A1 B1, A2 B2 .... ( i번째 노선은 Ai 이상, Bi 이하의 모든 정류장을 다님)
    AB = [list(map(int, input().split())) for _ in range(N)]

    # 그 다음 정수 P
    P = int(input())

    # P개의 줄 정수 C1, C2 ......
    C = [int(input()) for _ in range(P)]
    print(C)
    # 0이 P+1개 만큼 있는 리스트 생성 (총 정류장이 P개, 0번째를 비움)
    road = [0]*(P+1)

    # 버스가 지나는 길을 +1
    for i in range(N):
        for j in range(AB[i][0], AB[i][1]+1):
            road[j] += 1

    # 형식에 맞게 결과 변환
    res = ''
    for j in range(P):
        res = res + str(road[C[j]]) + ' '

    # 형식에 맞춰 출력
    print(f'#{t+1} {res}')

```

> 6485 삼성시의 버스노선
