# 주석

# for 문

# for 변수명 range(시작점, 끝점, 증가값) -> 증가값이 1이면 생략가능
for i in range(1, 10, 2) :
    # 블라블라
    pass # 형식만 잡고 내용을 넣기 싫을 때

for i in range(1, 10) : 
    # 블라블라
    pass

for i in range(1, 10):
    for j in range(1, 10):
        pass


# while 문
while i < 10 :
    pass

# do while x / switch case x

# 함수 지정 ( 한글명 변수 가능 )

def 함수이름(변수, 쓸거) :

    return 변수 + 쓸거 # return 필수 아님


# 파이썬은 입력할떄 알아서 형식을 맞춤 -> 시작할떄 지정 필요 x
i = 10
i = '사람'
i = {10, '사람'}

# list -> [] / dict -> {key : value} / tuple -> ()

# print
print('블라블라')

# str 으로 만들기 -> f'' 사용
a = f' 내용물 {i}'
print(a, f'{i}', '사람')


# 문서 읽는법  
import sys # sys 기능 불러오겠다

# sys 에서 stdin 기능안에 open 을 쓰겠다 -> open('파일명' , 'r') r -> 읽기
sys.stdin = open('intput.txt', 'r')

# 조건문 추가 -> 범위조건은 한줄로, 이어쓰기는 and or 
if 0 < a < 10 and 0 < a < 10 :
    pass

# 조건문 추가 -> if / elif / else
if a :
    pass

elif not a :
    pass

else :
    pass

# 테스트 케이스 수 읽기
input() # 한줄 통으로 읽어 오겠다
int() # 안에 내용물을 int로 바꾸겠다

T = int(input())

# global -> 전역변수 선언

# map('바꿀 형식', input().split()) -> str 외의 다른것으로 읽을경우
N, M = map(int, input().split())

# 둘다 str일 경우
N, M = input().split()

# list 가 붙으면 list 형식으로 받겠다
arr_M = list(map(int, input().split()))

arr_M[-1]