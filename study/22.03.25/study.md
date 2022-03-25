```python
# 2진수 -> 10진수
def two_ten(li):
    res = 0
    n = 1
    for i in range(len(li)-1, -1, -1):
        res += li[i] * n
        n *= 2

    return res


# 2진수 -> 10진수
def three_ten(li):
    res = 0
    n = 1
    for i in range(len(li) - 1, -1, -1):
        res += li[i] * n
        n *= 3

    return res


# 탐색
def find(m_2, m_3):
    for i in range(len(m_2)):
        # 초기 값 저장 용
        t_2 = m_2[i]

        # 자리 값 + 1 , 1을 넘어 가면 0으로 초기화
        m_2[i] += 1
        if m_2[i] > 1:
            m_2[i] = 0

        for j in range(len(m_3)):
            # 초기 값 저장 용
            t_3 = m_3[j]

            # 자리 값 + 1 , 2를 넘어 가면 0으로 초기화
            m_3[j] += 1
            if m_3[j] > 2:
                m_3[j] = 0

            # 10진수 변환
            res_2 = two_ten(m_2)
            res_3 = three_ten(m_3)

            # 값이 같으면 return
            if res_3 == res_2:
                return res_2

            # 3진수 쪽 한번 더 시행
            m_3[j] += 1
            if m_3[j] > 2:
                m_3[j] = 0

            res_2 = two_ten(m_2)
            res_3 = three_ten(m_3)

            if res_3 == res_2:
                return res_2

            # 탐색 실패시 해당 자리 값을 원래 대로 변경
            m_3[j] = t_3

        # 탐색 실패시 해당 자리 값을 원래 대로 변경
        m_2[i] = t_2


# 테스트 케이스 수
T = int(input())
for t in range(1, T+1):
    # 일단 str 로 입력 받음
    tem_2 = input()
    tem_3 = input()

    # 한 글자 씩 int 로 변환, list 로 저장
    m_2 = []
    for i in tem_2:
        m_2.append(int(i))

    m_3 = []
    for i in tem_3:
        m_3.append(int(i))

    # 함수 시행
    res = find(m_2, m_3)

    # 결과 출력
    print(f'#{t} {res}')

```

> 4366 - 정식이의 은행업무
