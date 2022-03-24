```python
# 패턴   n2 n3 n4 비율 : 대응 값
patt = {(2, 1, 1): 0,
        (2, 2, 1): 1,
        (1, 2, 2): 2,
        (4, 1, 1): 3,
        (1, 3, 2): 4,
        (2, 3, 1): 5,
        (1, 1, 4): 6,
        (3, 1, 2): 7,
        (2, 1, 3): 8,
        (1, 1, 2): 9}

# 16진수 2진수 변환용
ch_16 = {'0': '0000',
         '1': '0001',
         '2': '0010',
         '3': '0011',
         '4': '0100',
         '5': '0101',
         '6': '0110',
         '7': '0111',
         '8': '1000',
         '9': '1001',
         'A': '1010',
         'B': '1011',
         'C': '1100',
         'D': '1101',
         'E': '1110',
         'F': '1111'}

# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # 세로 : N, 가로 : M
    N, M = map(int, input().split())

    # 빈 리스트 생성
    arr = []

    # 데이터 선별 후 삽입
    for _ in range(N):
        # 데이터 값이 가로 길이 M을 넘어 가는 경우 잘라야 함 / 0으로 만 된 데이터 , 오른 쪽 0 모두 제거
        temp = input()[:M].rstrip('0')

        if temp and temp not in arr:
            arr.append(temp)

    # 중복 검색 방지용
    vis = []

    # 최종 결과
    res = 0

    # 16진수 -> 2진수 변환
    for i in range(len(arr)):
        # 변환된 데이터 저장용
        tem_num = ''

        # 각 요소별 시행
        for j in range(len(arr[i])):
            tem_num += ch_16[arr[i][j]]

        # 오른쪽 0 모두 제거 -> 암호 끝은 1 이므로 필요 없는 데이터 삭제
        ch_num = tem_num.rstrip('0')

        # 0과 1 카운트 해서 비율로 숫자 찾기
        n1 = n2 = n3 = n4 = 0
        num_li = []

        # 끝에서 부터 카운트
        for k in range(len(ch_num) - 1, -1, -1):
            # n4 카운트
            if ch_num[k] == '1' and n3 == 0:
                n4 += 1

            # n3 카운트
            elif ch_num[k] == '0' and n2 == 0:
                n3 += 1

            # n2 카운트
            elif ch_num[k] == '1' and n1 == 0:
                n2 += 1

            # n2, n3, n4 카운트 완료시 (n1은 카운트 할 필요 x)
            elif ch_num[k] == '0':
                if ch_num[k - 1] == '1':
                    # n2 n3 n4 중 최소값 찾기
                    n = n2

                    if n > n3:
                        n = n3

                    if n > n4:
                        n = n4

                    # 비율에 해당 하는 값 추가
                    num_li.append((patt[n2 // n, n3 // n, n4 // n]))

                    # 한 패턴 완료 -> 변수 초기화
                    n2 = n3 = n4 = 0

                    # 추출한 번호가 8개가 된 경우
                    if len(num_li) == 8:
                        # 암호의 조건 판별 : (홀수 합) * 3 + (짝수 합 ) + 판별용 수 (0번 인덱스) = 10의 배수
                        if not ((num_li[1] + num_li[3] + num_li[5] + num_li[7]) * 3 + (num_li[2] + num_li[4] + num_li[6]) + num_li[0]) % 10:
                            # 중복 검사
                            if num_li not in vis:
                                # num_li의 총합
                                for m in range(len(num_li)):
                                    res += num_li[m]

                                # 중복 판단용 list 에 추가
                                vis.append(num_li)

                        # 재사용 하기 위해 초기화
                        num_li = []

    # 형식에 맞게 출력
    print(f'#{t} {res}')

```

> 1242 - 암호 코드 스캔
