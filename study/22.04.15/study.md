```python
# 모든 정보 조회
SELECT * FROM (테이블 명)

# 데이터 삽입
INSERT INTO (테이블 명)
VALUES ('데이터 값', ....);

# 전체 튜플 수
SELECT COUNT(*) FROM (테이블 명)

# 조건 문 -> 조건은 여러개 가능
SELECT (표시할 속성)
FROM (테이블 명)
WHERE (조건);

# 조건
like 'a%'
-> a로 시작하는 모든

like '_a%'
-> 두번째 글자가 a로 시작하는 모든

등등

# orm 조건문
User.objects.order_by('balance', '-age')[:10]
-> order_by 에서 표시 x 는 오름차순, - 는 내림차순
-> [:] 슬라이싱으로 값을 잘라냄

# 같은 조건문
SELECT *
FROM users_user
ORDER BY balance DESC, age
LIMIT 10;
-> ORDER BY 의 기본값은 내림차순(asc), 오름차순은 desc
-> LIMIT 로 값을 잘라냄
-> LIMIT 1 OFFSET 4; 처럼 OFFSET을 추가 할 경우 4번 인덱스에 있는 데이터(5번째 데이터)를 반환함
```

