```python
# 병합 정렬
def merge_sort(arr):
    # 문제 조건인 합칠 때 왼쪽 끝 > 오른쪽 끝 카운트 용
    global cnt

    # 길이가 1 이하면 반환
    if len(arr) < 2:
        return arr

    # 중간값 설정
    mid = len(arr) // 2

    # 중간값 기준 왼쪽 / 오른쪽 분할
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # 결과 저장용
    merged_arr = []

    # 변수 초기화 (l: low 인덱스 / h : high 인덱스)
    l = h = 0

    # 조건 카운트
    if low_arr[-1] > high_arr[-1]:
        cnt += 1

    # 각 list 중 하나 라도 원소를 모두 사용할 때 까지 진행
    while l < len(low_arr) and h < len(high_arr):
        # 더 작은 쪽의 원소를 넣고 해당 list index + 1
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    # 남아 있는 원소가 있다면 merged_arr 에 추가
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    # 결과 반환
    return merged_arr


# 테스트 케이스 수
T = int(input())
for t in range(1, T+1):
    # N : 원소 개수
    N = int(input())

    # 원본 list
    arr = list(map(int, input().split()))

    # 조건 카운트 변수 초기화
    cnt = 0

    # 함수 실행
    res = merge_sort(arr)

    # 중간값
    mid = N // 2

    # 형식에 맞게 결과 출력
    print(f'#{t} {res[mid]} {cnt}')

```

> 5204 - 병합정렬
