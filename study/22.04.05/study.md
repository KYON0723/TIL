```python
def digkstra():
    while Q:
        now, dist = Q.pop()

        if D[now] < dist:    # 주어진 거리보다 이미 저장된 거리가 더 작으면 skip
            continue

        visited[now] = True
        # 현재 정점의 인접 정점을 선택하여 그 인접 정점을 확인
        for v in range(len(adj[now])):
            n_v, n_dist = adj[now][v]
            if not visited[n_v]:
                if dist + n_dist < D[n_v]:
                    D[n_v]= dist + n_dist
                    Q.append((n_v, D[n_v]))



V, E = map(int, input().split())
# 인접 리스트
adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    adj[s].append((e, d))

INF = 987654321
D = [INF] * (V+1)
D[0] = 0
# 시작 정점에서 인접한 정점 거리를 저장
for v, d in adj[0]:
    D[v] = d

visited = [False] * (V+1)
visited[0] = True

Q = [*adj[0]]
digkstra()
print(D)
```

> digkstra 방식



```
def find_set(x):
    # loop 활용
    while x != P[x]:
        x = P[x]
    return x

    # 재귀
    # if x == P[x]:
    #     return x
    # else:
    #     return find_set(P[x])

V, E = map(int, input().split())
edge = []
for _ in range(E):
    s, e, d = map(int, input().split())
    edge.append((d, s, e))   # 거리를 앞에 넣어서 sort 함수로 편하게 정렬가능
# 거리를 기준으로 오름차순
edge.sort()

P = [i for i in range(V+1)]  # 부모 원소 초기화
count = 0   # 선택된 정점의 수
total = 0   # 거리의 합

for d, s, e in edge:
    x = find_set(s)
    y = find_set(e)
    if x != y:       # 사이클을 형성하지 않음
        count += 1
        total += d
        P[y] = x     # 부모 원소를 갱신

        if count == V:
            break

print(total)
```

> kruskal 방식



```
def prim(start):
    D[start] = 0

    for _ in range(V):
        # MST 에 포함되지 않은 정점 중에서 거리가 최소인 정점을 찾는
        min_v = 0
        min_d = INF
        for i in range(1, V+1):
            if MST[i] == 0:
                if D[i] < min_d:
                    min_d = D[i]
                    min_v = i

        MST[min_v] = 1   # MST에 등록
        for v in range(V+1):
            # 연결되지 않은 정점 중에서
            # 선택된 정점 min_v와 연결된 정점들을 찾아서 거리를 확인
            if adj[min_v][v] != 0 and MST[v] == 0:
                if D[v] > adj[min_v][v]:
                    D[v] = adj[min_v][v]
                    P[v] = min_v

    return sum(D[start:]), P


V, E = map(int, input().split())
INF = 987654321

adj = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    adj[s][e] = d
    adj[e][s] = d


MST = [0] * (V+1)    # MST 구성 여부
D = [INF] * (V+1)    # 최소 거리
P = [0] * (V+1)      # 연결된 부모

res = prim(1)
print(res)
```

>  prim 방식
