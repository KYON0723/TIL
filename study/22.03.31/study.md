```python
# 현재 위치 / 남은 배터리 / 교체 횟수
def find(a, b, cnt):
    # 가장 적은 횟수 저장용
    global min_cnt

    # cnt 가 min_cnt 초과 -> 종료
    if cnt > min_cnt:
        return

    # 도착한 경우
    if a == arr[0]:
        # 비교
        if cnt < min_cnt:
            min_cnt = cnt
        return

    # 도착 x 배터리 x
    if not b:
        return

    # 도착 x, 배터리 o
    else:
        # 배터리 교체 x
        find(a+1, b-1, cnt)

        # 배터리 교체 o -> 마지막 정류장 배터리 x
        if a+1 < arr[0]:
            find(a+1, arr[a+1], cnt+1)


# 테스트 케이스 수
T = int(input())
for t in range(1, T+1):
    # 0번 : 정류장 수 , 1번 ~ : 정류장 별 충전지 정보
    arr = list(map(int, input().split()))

    # 가장 적게 교체한 횟수 저장용
    min_cnt = 987654321

    # 함수 실행
    find(1, arr[1], 0)

    # 결과 출력
    print(f'#{t} {min_cnt}')

```

> 5208 - 전기버스



```
def quick_sort(arr):
    # 길이 1 이하 : 종료
    if len(arr) <= 1:
        return arr

    # pivot 값 : 중간값
    pivot = arr[len(arr) // 2]

    # 더 작은 값 / 같은 값 / 더 큰 값
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        # pivot 보다 작으면 작은 곳에
        if num < pivot:
            lesser_arr.append(num)

        # 크면 큰 곳에
        elif num > pivot:
            greater_arr.append(num)

        # 같으면 같은 곳에
        else:
            equal_arr.append(num)

    # 재귀 반복
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # 원소 수
    N = int(input())

    # 정렬할 list
    arr = list(map(int, input().split()))

    # 함수 실행
    res = quick_sort(arr)

    # 중간 index 값
    mid = N // 2

    # 출력
    print(f'#{t} {res[mid]}')
```

> 5202 - 퀵정렬
