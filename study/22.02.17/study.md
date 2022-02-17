```python
import sys

sys.stdin = open('input.txt', 'r')

# testcase 수
T = int(input())

for t in range(T):
    # 표시된 문자열 입력
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    res = 1

    # 가로 검증
    for i in range(9):
        if len(set(sudoku[i])) != 9:
            res = 0

    # 세로 검증
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(sudoku[j][i])

        if len(set(temp)) != 9:
            res = 0

    # 구역 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for k in range(3):
                for l in range(3):
                    temp.append(sudoku[k+i][l+j])

            if len(set(temp)) != 9:
                res = 0

    # 형식에 맞춰 출력
    print(f'#{t+1} {res}')

```

> 1974 스도쿠 검증



```python
import sys

sys.stdin = open('input.txt', 'r')

# testcase 수
T = int(input())

for t in range(T):
    # 학생 수
    N = int(input())

    # 현 위치 / 가야할 위치 저장된 list
    A = [list(map(int, input().split())) for _ in range(N)]

    # 길이가 400인 빈 list
    B = [0]*400

    # 빈 리스트에 가야할 길 표시
    for i in range(N):
        for j in range(A[i][0]-1, A[i][1]):
            B[j] += 1

    # 중복된 길중 가장 수치가 높은 것을 찾음
    cnt = 0
    for i in range(400):
        if B[i] > cnt:
            cnt = B[i]

    # 형식에 맞춰 출력
    print(f'#{t+1} {cnt}')

```

> 4408 자기방으로 돌아가기
