```
# vuex
- 상태관리 패턴 + 라이브러리
- 상태를 전역 저장소로 관리 할 수 있도록 지원하는 라이브러리 -> 중앙 집중식 저장소 역할
- 기존 방식은 단방향 흐름에 의존하므로 프로젝트 규모가 커지면 데이터 관리가 불편해짐
- 이 방식은 중앙 저장소(store)에 상태를 모아놓고 관리
- 규모가 큰(중첩이 많음) 프로젝트에서 매우 효율적

# 시작하기
- vue add vuex -> 설치
- store 생성됨
- index.js 생성됨 => 함수가 작성되는 곳

# state
- 중앙에서 관리하는 모든 정보 (data)
- 모든 컴포넌트가 state를 참조함

# Mutations
- state를 실제로 조작하는 유일한 방법
- 동기적 함수
- 첫번째 인자는 항상 state
- Actions 에서 commit() 으로 호출

# Actions
- Mutations를 호출하여 사용 -> 간접적으로 state 조작
- 비동기 작업이 포함 될 수 있음
- context 객체 인자를 받음
- 컴포넌트에서 dispatch() 로 호출

# Getters
- state를 변경하지 않고 값을 이용 => 출력, 계산 등등
- computed 와 유사

# session storage
- tab을 닫으면 날아감

# local storage
- 사용자 컴퓨터에 데이터 저장
- 데이터베이스 역할을 함

# 전개구문
- '...' 을 사용
- key가 0개 이상인 iterable object를 하나의 object로 간단하게 표현
- ex) ...todo

# vuex-persistedstate
- 창 새로고침시에 상태 초기화 방지
- npm install vuex-persistedstate 필요
- 아래 상세설명 참조

# LocalStorage
- vuex-persistedstate
- 새로고침 해도 로컬 저장소에 데이터를 저장해 두어서 state를 유지함
- npm install vuex-persistedstate
- import createPersistedState from 'vuex-persistedstate'
- plugeins: [
		createdPersistedState(),
	]
- 위 3개 필수


```

