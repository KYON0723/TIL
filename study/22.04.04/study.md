```python
# 방향 ( 상 하 좌 우 )
di, dj = (1, -1, 0, 0), (0, 0, -1, 1)

# 테스트 케이스 수
T = int(input())

for t in range(1, T + 1):
    # 원자 수
    N = int(input())

    # 정보 ( x좌표, y좌표 , 방향, 에너지 )
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 결과값 초기화
    ans = 0

    # 좌표 * 2
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2

    for _ in range(4002):
        # 좌표 이동
        for i in range(len(arr)):
            arr[i][0] += dj[arr[i][2]]
            arr[i][1] += di[arr[i][2]]

        # 중복 되면 삭제
        ddel, v = set(), set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]

            if (cj, ci) in v:
                ddel.add((cj, ci))

            v.add((cj, ci))

        for i in range(len(arr) - 1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                ans += arr[i][3]
                arr.pop(i)

    print(f'#{t} {ans}')
```

> 5648  - 원자 소멸 시뮬레이션
