```python
# 패턴       0          1          2          3          4          5          6          7          8          9
patt = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


def find():
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j]:
                return i, j


T = int(input())

for t in range(1, T+1):
    # 세로 : N, 가로 : M
    N, M = map(int, input().split())

    # N x M 빈 행렬 생성
    arr = [[0]*M for _ in range(N)]

    # 값 채워 넣기
    for i in range(N):
        temp = list(input())

        for j in range(M):
            arr[i][j] = int(temp[j])

    # a : 세로 인덱스 / b : 가로 인덱스
    a, b = find()

    # 새로 저장할 리스트 생성
    arr2 = [0 for _ in range(56)]

    # 맨 끝부터 채워 넣음
    for i in range(55, -1, -1):
        arr2[i] = arr[a][b]
        b -= 1

    # 자리수 별로 데이터 삽입 할 빈 리스트 생성
    tem = [0 for _ in range(8)]

    # 앞에서 부터 해독
    idx = 7
    while arr2:
        # 앞에서 부터 1글자씩 추출 7개 원소의 새 리스트 생성
        res = ''
        for i in range(7):
            res += str(arr2.pop(0))

        # 일치 하는 패턴이 있으면 idx 번 인덱스 위치 번호 삽입
        for j in range(len(patt)):
            if res == patt[j]:
                tem[idx] = j
                idx -= 1
                break

    # 검증
    p = (tem[7] + tem[5] + tem[3] + tem[1]) * 3 + (tem[6] + tem[4] + tem[2]) + tem[0]

    dap = 0

    if not p % 10:
        for i in range(8):
            dap += tem[i]

    # 형식에 맞게 출력
    print(f'#{t} {dap}')

```

> 1240 - 단순 2진 암호 코드
