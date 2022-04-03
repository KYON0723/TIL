```python
def cal():
    global res

    # 큐가 빌 떄 까지 반복
    while q:
        a, cnt = q.popleft()

        # 계산 완료
        if a == M:
            res = cnt

            # 함수 종료
            return

        # 4 가지 경우를 각각 실행
        for i in range(4):
            if i == 0:
                # 범위 1 ~ 100만 이하 자연수 / 연산 결과 값이 아직 나온적 없음
                if 1 <= a + 1 <= 1000000 and vis[a+1] == 0:
                    # 현재 상황 저장 ( 현재 값, 연산 횟수 )
                    q.append((a+1, cnt+1))

                    # 이 값은 나온적 있음 표시
                    vis[a+1] = 1

            elif i == 1:
                if 1 <= a-1 <= 1000000 and vis[a-1] == 0:
                    q.append((a-1, cnt+1))
                    vis[a-1] = 1

            elif i == 2:
                if 1 <= a*2 <= 1000000 and vis[a*2] == 0:
                    q.append((a*2, cnt+1))
                    vis[a * 2] = 1

            elif i == 3:
                if 1 <= a-10 <= 1000000 and vis[a-10] == 0:
                    q.append((a-10, cnt+1))
                    vis[a-10] = 1


# 테스트 케이스 수
T = int(input())
for t in range(1, T+1):
    # N : 초기 값 / M : 원하는 값
    N, M = map(int, input().split())

    # 결과
    res = 0

    # 사용 여부
    vis = [0] * 1000001

    # 초기 값
    q = deque()
    q .append((N, 0))

    # 함수 시행
    cal()

    # 결과 출력
    print(f'#{t} {res}')
```

> 5247  - 연산
