```python
# 너비 우선 탐색
def BFS(n):
    res = [n]
    q = [n]

    while q:
        a = q.pop(0)

        for i in range(8):
            if arr_M[a][i]:
                if i not in res:
                    res.append(i)
                    q.append(i)

    return res


# 입력에 , 으로 구분 되어 있음
temp = list(map(int, input().split(',')))

# (노드 최대 번호 + 1) ^ 2 의 행렬
arr_M = [[0] * 8 for _ in range(8)]

# 방향이 없음 -> 양쪽 다 표시
for i in range(0, len(temp)-1, 2):
    arr_M[temp[i]][temp[i+1]] = 1
    arr_M[temp[i+1]][temp[i]] = 1

# 함수 시행
tem = BFS(1)

# 출력
for i in tem:
    print(i, end=' ')
```

> 너비 우선 탐색 (BFS) - 그래프의 경우(방향 x)
