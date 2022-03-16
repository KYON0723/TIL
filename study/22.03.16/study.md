```python
import sys

sys.stdin = open('input.txt', 'r')


# 중위 순회
def calcul(t, idx):
    temp = ''

    # 왼쪽
    if idx*2 < len(t):
        temp += calcul(t, idx * 2)

    # 루트
    temp += t[idx]

    # 오른쪽
    if idx*2+1 < len(t):
        temp += calcul(t, idx * 2 + 1)

    # 문자열 완성 후 반환
    return temp


for t in range(1, 11):
    # 총 정점 수
    N = int(input())

    # 계산 편의상 0번을 비우고 1번 ~ N번 으로 사용
    tree = [''] * (N + 1)

    # 1부터 시작
    for i in range(1, N + 1):
        s = list(input().split())

        # 인덱스 = 노드 번호, 값 = 노드 값
        tree[int(s[0])] = s[1]

    s = calcul(tree, 1)

    print(f'#{t} {s}')
```

> 1231 - 중위 순회
