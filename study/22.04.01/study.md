```python
# 깊이 우선 탐색
def DFS(n):
    # 방문 처리
    vis[n] = 1

    # 출력
    print(n, end=' ')

    # 노드 최대 번호 + 1 까지
    for j in range(8):
        # 방문 안함 + 연결 된 지점 탐색
        if arr_M[n][j] and vis[j] == 0:
            DFS(j)


# 입력에 , 으로 구분 되어 있음
temp = list(map(int, input().split(',')))

# (노드 최대 번호 + 1) ^ 2 의 행렬
arr_M = [[0] * 8 for _ in range(8)]

# 방향이 없음 -> 양쪽 다 표시
for i in range(len(temp)//2):
    n1, n2 = temp[i*2], temp[i*2+1]

    arr_M[n1][n2] = 1
    arr_M[n2][n1] = 1

# 방문 여부
vis = [0] * 8

# 함수 시행
DFS(1)
```

> 깊이 우선 탐색 (DFS) - 그래프의 경우(방향 x)
