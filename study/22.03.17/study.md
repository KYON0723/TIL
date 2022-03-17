```python
import sys

sys.stdin = open('input.txt', 'r')


def cal(n):
    # 범위 초과시
    if n >= N:
        return

    # 왼쪽
    if tree[n][2]:
        cal(tree[n][2])

    # 오른쪽
    if tree[n][3]:
        cal(tree[n][3])

    # 연산자에 맞춰 계산
    if tree[n][1] == '+':
        tree[n][1] = tree[tree[n][2]][1] + tree[tree[n][3]][1]

    elif tree[n][1] == '-':
        tree[n][1] = tree[tree[n][2]][1] - tree[tree[n][3]][1]

    elif tree[n][1] == '*':
        tree[n][1] = tree[tree[n][2]][1] * tree[tree[n][3]][1]

    elif tree[n][1] == '/':
        tree[n][1] = tree[tree[n][2]][1] / tree[tree[n][3]][1]


T = 10

for t in range(1, T+1):
    # 정점의 수
    N = int(input())

    # 0 제외 1 ~ N 까지 인덱스 사용
    tree = [[0]*4 for _ in range(N+1)]

    # 값 입력
    for i in range(N):
        temp = list(input().split())

        # 숫자 이면 숫자로 저장
        if temp[1].isdigit():
            tree[int(temp[0])][1] = int(temp[1])

        # 연산자 이면 연산자, 왼쪽, 오른쪽 자식 으로 저장
        else:
            # 연산자
            tree[int(temp[0])][1] = temp[1]

            # 왼쪽 자식
            tree[int(temp[0])][2] = int(temp[2])

            # 오른쪽 자식
            tree[int(temp[0])][3] = int(temp[3])

    # 함수 실행
    cal(1)

    # 형식에 맞춰 출력
    print(f'#{t} {int(tree[1][1])}')

```

> 1232 - 사칙연산
