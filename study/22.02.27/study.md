```python
import sys

sys.stdin = open('input.txt', 'r')

# 테스트 케이스 수
T = 10

for t in range(1, T+1):
    A = int(input())

    numbers = list(map(int, input().split()))

    # 무한 반복 탈출용 장치
    sw = 1

    # for 문 : 1 사이클 / while 문 : 조건을 만족 할 때 까지 반복
    while sw == 1:
        for i in range(5):
            # 맨 앞 숫자 추출
            temp = numbers.pop(0)
            temp -= i+1

            # 0 보다 작으면 0으로 변환
            if temp < 0:
                temp = 0

            # 맨 뒤에 붙임
            numbers.append(temp)

            # 0 인 경우 for 문 중단 + while 문도 중단
            if temp == 0:
                sw = 0
                break

    # 형식에 맞게 변환
    res = ''
    for i in numbers:
        res += str(i) + ' '

    # 결과 출력
    print(f'#{t} {res}')

```

> 1225 - 암호 생성
