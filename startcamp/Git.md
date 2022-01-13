# Git



## 버전관리?

* 작업한 결과물을 작업한 시간에 따라 버전을 나누어 관리 하는 것
* ex) 레포트 최종, 레포트 Fianl 등등



## Git을 이용한 버전 관리

* 중앙집중형
* 분산형



## Git

* `untracked` : 빨간색, 처음으로 관리대는 대상
* `tracked` : 관리되고 있는 대상
  * `modified` : 녹색
  * `unmodified` 



* `git config --global user.email "메일주소"` : Git 허브 메일 주소 설정
* `git config --global -l` : 정보를 보여줌
* `git config --global user.name "유저이름"` : 유저 네임 설정



* `git commit` :  commit 실행창 
  * `i` : insert 활성화
  * `esc` : 뒤로 가기
  * `:wq` : 종료



* `git commit -m "내용"` : 실행창 없이 메세지만 넣기



* `git remote add origin https://github.com/닉네임/폴더.git` : 업로드 위치 지정
* `git push -u origin master` : 로그인창
* `git push` : Git 허브에 저장



* `Git 연결하기` : `cd ssafy7/TIL`

* `커밋 순서` : `git add . ` => `git commit -m '메세지'` => `git push` 