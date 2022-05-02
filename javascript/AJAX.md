```
# AJAX
- Asynchronous JavaScript And XML 비동기식 JavaScript 와 XML

- 서버와 통신하기 위해 XMLHttpRequest 객체 활용

- 순서대로 처리하는 동기 방식과 달리 비동기 방식은 순서와 상관없이 실행함

- 페이지 새로고침 없이 서버에 요청 + 데이터 받고 작업 수행

# zero delays
- 최소 지연시간으로 실행, 실제론 0ms는 아님

# 순차적 비동기
- Async callbacks
	- 백그라운드에서 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
	
- promise-sytle
	- modem Web APls에서의 새로운 코드 스타일
	- XMLHttpRequest 객체를 사용하는 구조보다 조금 더 현대적 버전
	
# Callback function
- 다른 함수에 인자로 전달된 함수

- 동기 비동기 모두 사용됨

- 비동기 로직을 수행할 시 필수적으로 사용

- JS의 함수는 일급객체
	- 다른 객체에 적용할 수 있는 연산을 모두 지원하는 객체
	- 인자로 넘길수 있음
	- 함수 반환값으로 사용 가능
	- 변수에 할당 가능
	
# Async callbacks
- 백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수

# callback hell
- 순차적 연쇄 비동기 작업을 처리하기위해 callback을 연속적으로 사용할 경우
 너무 많은 연쇄작업을 거쳐 지나치게 길어지면 가독성이 떨어지고 디버깅에 문제가 생김
 
- 코드 길이를 얕게 유지하거나 모듈화, 단일오류 처리 등의 방법으로 해결

- 가장 좋은 방법은 Promise callback 방식 사용

# promise object
- 비동기 작업의 최종완료 또는 실패를 나타내는 객체

- .then() -> 성공시
	- 각각의 then은 서로 다른 promise 반환
	- 여러개를 사용하여 연쇄 작업 수행 가능
	- 반드시 반환값이 있어야 함
	
- .catch() -> 하나라도 실패시 (오류 발생시)

- .finally()
	- promise 객체 반환
	- 결과와 상관없이 무조건 지정된 함수가 실행
	- 어떤 인자도 전달 받지 않음

# Axios
- 브라우저를 위한 Promise 기반의 클라이언트

- 예시
axios.get(URL)
	.then(function (response) {
		console.log(response)
		return response.data
	})
	
	.then(function (data) {
		return data.title
	})
	
	.then(function (title) {
		console.log(title)
	})
	
	.catch(function (error) {
		console.log(error)
	})
	
	.finally(function () {
		console.log('무조건 실행됨')
	})
	
# async & await
- 비동기 코드를 작성하는 새로운 방법

- 기존 promise 구조의 then chanining을 제거, 보다 동기 코드처럼 표현


```

