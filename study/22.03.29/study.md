```python
# 선택 정렬 (내림 차순)
def sel_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return


T = int(input())

for t in range(1, T+1):
    # N : 컨테이너 수 / M : 트럭 수
    N, M = map(int, input().split())

    # ww : 화물 무게 / tt : 적재 용량
    ww = list(map(int, input().split()))

    tt = list(map(int, input().split()))

    # ww 와 tt 를 정렬 (내림 차순)
    sel_sort(ww)
    sel_sort(tt)

    # 초기값 지정
    hap = 0
    i, j = 0, 0

    # 트럭 모두 사용시 중단
    while i < M:
        # 트럭에 실을수 있는 가장 큰 화물 발견
        if tt[i] >= ww[j]:
            # hap 에 합산
            hap += ww[j]

            # 다음 트럭
            i += 1

        # 다음 화물
        j += 1

        # 현재 가장 큰 트럭에 아무 것도 싣지 못함 -> 중단
        if j == N:
            break

    # 출력
    print(f'#{t} {hap}')
```

> 5201 - 컨테이너 운반



```
# 순열 생성
def shuffle(arr):
    # 첫 항은 본인
    result = [arr[:]]

    # arr 길이와 같은 빈 리스트 생성 (check 용)
    c = [0] * len(arr)

    # 시작 값은 0
    i = 0

    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0

        else:
            c[i] = 0
            i += 1

    return result


# 최소 사용량 경로 찾기
def find(res, arr):
    # 최소값 초기값 : 적당히 큰 값으로 지정
    min_hap = 987654321

    # res 안의 요소는 번호로 저장됨 -> index 는 -1
    for item in res:
        # 초기값 : 1 -> 첫번째 번호
        hap = arr[0][item[0]-1]

        # 이후 번호 순서 대로 값 저장
        for i in range(1, N-1):
            hap += arr[item[i-1]-1][item[i]-1]

        # 마지막 번호 -> 1번
        hap += arr[item[N-2]-1][0]

        # 최소값 변경
        if hap < min_hap:
            min_hap = hap

    # 최소값 반환
    return min_hap


# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # N : 크기
    N = int(input())

    # 관리 구역
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 2 ~ N 의 값을 가진 리스트 생성
    numbers = []
    for i in range(2, N+1):
        numbers.append(i)

    # numbers 로 순열 생성
    res = shuffle(numbers)

    # 함수 시행
    ans = find(res, arr)

    # 결과 출력
    print(f'#{t} {ans}')
```

> 5189 - 전자카트
