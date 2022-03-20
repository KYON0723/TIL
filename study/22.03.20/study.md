```python
MTV -> model - template - view
 
django-admin startproject firstpjt . -> . 의 의미 (all)

_init_.py -> 디렉토리를 하나의 패키지로 다루도록 지시

settings.py -> 어플리케이션의 모든 설정 포함

uls.py -> 사이트의 url과 views 연결

manage.py -> 커맨드라인 유틸리티

python manage.py startapp articles -> 앱 이름은 복수로 사용

앱생성시 1. 생성하고 2. INSTALLD_APPS 에 등록해야 한다.

urls -> 요청을 view에 전달

view -> 요청을 수신하고 원하는 작업을 수행할 함수를 작성하는 공간

templates -> 실제 보여주는 내용

언어 -> ko-kr , 지역 -> asia/Seoul

필터 사용법 -> {{ variable|filter }} ex) name|lower

태그 사용법 -> {% tag %}

코멘트 사용법 -> {# comment #}

확장 사용법 -> {% extends '' %}
    
참조 사용법 -> {% include '' %}

url 위치로 보낼때 사용 -> form action = 'url'
    
보내는 방법 지정 -> method = 'POST'

입력 타입 지정 -> input type='type'
    
request.GET.get('')
    
url 링크 방법 -> {% url '' %}
    
Migration -> [makemigrations / migrate / sqlmigrate / showmigrations]
    			  생성		  반영	 sql구문 확인	 전체 상태 확인
  
python manage.py  명령어 
    -> sqlmigrate app_name 0001 -> 얘만 다름
    
auto_now_add -> 최초 입력시 시간을 저장해줌(작성시간)

auto_now - 최종 입력 시간을 저장해줌(수정시간)
    
migration 3단계 - models.py(변경사항 반영) 
    -> python manage.py makemigrations 
    -> python manage.py migrate 순으로 진행

classname.objects.all() -> 모든 정보 불러오기
    
classname.save() -> 데이터 입력 후 이걸 사용 해야 저장됨
    
데이터 저장법 1
name = classname()
name.요소1 = '내용1'
name.요소2 = '내용2'
name.save()
    
데이터 저장법 2
name = classname(요소1='내용1', 요소2='내용2')
name.save()

데이터 저장법 3
classname.objects.create(요소1='내용1', 요소2='내용2')

위 3가지 방법으로 가능
    
.all() -> 모든 정보
    
.get('조건') -> 특정 정보 -> 1개인 경우만 정상, 없거나 둘 이상이면 오류 발생 (pk로 검색해야함)

.filter('조건') -> 특정 정보 -> 여러개 가능

데이터 수정
name = classname.objects.get(pk=1)
name.요소1 = '변경내용'
name.save()

데이터 삭제
name.delete()

관리자 계정
python manage.py createsuperuser - admin 계정 생성
    -> admin.py 에 admin.site.register(classname) 작성 필요
    
```

> 시험 대비 요점 정리
