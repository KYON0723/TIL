```
pip install django-seed

pip install djangorestframework

pip install psycopg2

# 더미 데이터 생성 방법
Dummy Data
	python manage.py seed articles --number=20

HTTP - Hyper Text Transfer Protocol
	- request - 요청 (GET, POST, PUT, DELETE)
	- response - 응답
	- resource - 자원
	- URL - Uniform Resouce Locator
		통합 자원 위치
		웹 주소, 링크 라고도 함
	- URN - Uniform Resource Name
		통합 자원 이름
		자원의 위치에 영향을 받지 않는 유일한 이름 역할
	- URI - Uniform Resouce Identifier
		통합 자원 식별자
		인터넷 자원을 식별하는 유일한 주소 - 하위개념 : URL, URN
		구조 
			- Scheme(protocol)
			- host(Domain name)
			- Port
			- Path
			- Query
			- Fragment
			
API - Application Programing Interface - 방식 : CLI, GUI 등

REST - REpresentational State Transfer - API 개발 설계 방법론
	
JSON - JavaScript Object Notation

Django Rest Framework
	pip install djangorestframework
	
	# installed_apps
	'rest_framework'
	
ModelSerializer - 모델에 맞춰 자동으로 필드 생성
	ex) from rest_framework import serializers
		...
		
		class ArticleSerializer(serializers.ModelSerializer):
			...
			
		der tes(response):
			articles = Article.objects.all()
			serializer = ArticleSerializer(articles, many=True)
			
			Return Response(serializer.data)
	
Django Rest Framework(DRF)

# 댓글 기능 관련 역참조
comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	- 역참조 필드 불러오기 -> pk만 가져옴
	
comment_set = Commentserializer(maney=True, read_only=True)
	- Nest 방식 역참조 필드 불러오기 -> 모든 내용을 가져옴 (1:N 에서 가능)

comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
	- 댓글 갯수 카운트
			
		
pip install drf-yasg

```



