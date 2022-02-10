```python
import sys

sys.stdin = open('input.txt', 'r')

# testcase는 10개 주어짐
for t in range(10):
    # 상자를 옮길 수 있는 횟수
    N = int(input())

    # 상자 높이 list
    box_li = list(map(int, input().split()))

    # list의 길이(인덱스 접근용)
    cnt_box = 0
    for i in box_li:
        cnt_box += 1

    # N번 반복함
    for work in range(N):
        # 가장 높은 높이, 낮은 높이 초기화
        max_box = 1
        min_box = 1000

        # 가장 높은 높이, 낮은 높이 찾기
        for box in box_li:
            if box > max_box:
                max_box = box

            if box < min_box:
                min_box = box

        # 가장 높은 박스 -1
        for i in range(cnt_box):
            if box_li[i] == max_box:
                box_li[i] -= 1
                break

        # 가장 낮은 박스 + 1
        for j in range(cnt_box):
            if box_li[j] == min_box:
                box_li[j] += 1
                break

    # 결과 출력
    print(f'#{t+1} {max_box-min_box}')
```

> 1208_Flatten 풀이
