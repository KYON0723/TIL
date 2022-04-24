```python
# 스켈레톤 코드가 주어짐

# 용어 설명
API - Application Programing Interface - 방식 : CLI, GUI 등

REST - REpresentational State Transfer - API 개발 설계 방법론
	
JSON - JavaScript Object Notation

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

            
# DB 불러오기
fixtures - 공유용 데이터 베이스

git에 DB를 올리지 않으므로 공동작업시 DB를 매번 새로 만들 필요가 있음
-> fixtures를 사용하여 해결

dumpdata - 데이터 추출
-> python manage.py dumpdata --indent 4 articles.article > articles.json
-> 추출 후 (app이름)/fixtures/ 경로를 만들어 넣어줌

데이터 사용
-> python manage.py loaddata articles/articles.json
            
            
# 가상 환경 세팅
$ python -m venv venv
$ source venv/Scripts/activate


# 설치
$ pip install -r requirements.txt


# 댓글 기능 관련 역참조
comment_set 
= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	- 역참조 필드 불러오기 -> pk만 가져옴
	
comment_set 
= Commentserializer(maney=True, read_only=True)
	- Nest 방식 역참조 필드 불러오기 -> 모든 내용을 가져옴 (1:N 에서 가능)

comment_count 
= serializers.IntegerField(source='comment_set.count', read_only=True)
	- 댓글 갯수 카운트


# 아래 2개는 포함되어 있을 것?
$ pip install django-seed => django_seed
	=> 사용법 : python manage.py seed (앱이름) --number=(생성할만큼)
        
$ pip install djangorestframework => rest_framework
	=> from rest_framework import serializers => 시리얼라이저 생성

		class ReviewSerializer(serializers.ModelSerializer):

    		class Meta:
       			model = Review
        		fields = '__all__'

        		read_only_fields = ('movie',)
                => FK 로 사용하는 필드는 read_only로 사용
                
        class ActorSerializer(serializers.ModelSerializer):
    		class MovieTitle(serializers.ModelSerializer):

        		class Meta:
            		model = Movie
            		fields = ('title',)
                    
    			movies = MovieTitle(read_only=True, many=True)
                => 1:N 참조

    		class Meta:
        		model = Actor
        		fields = '__all__'
                
               => 2중 필드 정의

            
# model 주의점 2개            
actors = models.ManyToManyField(Actor, related_name='movies')
=> M:N 필드 생성
    
movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
=> FK 생성


# url 경로 정의
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
]


# url 설정
from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),

    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>', views.movie_detail),

    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.create_review),
]


# views 설정
@api_view(['GET']) 
=> from rest_framework.decorators import api_view 필요

actors = get_list_or_404(Actor) 
=> from django.shortcuts import get_list_or_404 필요

return Response(serializer.data)
=> from rest_framework.response import Response 필요

if selializer.is_valid(raise_exception=True)
=> 조건 부합시 400 에러 발생

return Response(data, status=status.HTTP_204_NO_CONTENT)
=> from rest_framework import status 필요


# 리스트 정보 불러오기
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    # 1:N 관계 -> many=True
    serializer = ActorListSerializer(actors, many=True)

    return Response(serializer.data)


# 단일 정보 불러오기
@api_view(['GET'])
def actor_detail(request, actor_pk):
    # 단일정보 -> pk 설정 필요
    actor = get_object_or_404(Actor, pk=actor_pk)
    selializer = ActorSerializer(actor)

    return Response(selializer.data)


# 단일정보 불러오기 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE',])
def review_detail(request, review_pk):
    # 단일정보 -> pk 필요
    review = get_object_or_404(Review, pk=review_pk)

    # 불러 오기
    if request.method == 'GET':
        selializer = ReviewSerializer(review)

        return Response(selializer.data)

    
    # 수정
    elif request.method == 'PUT':
        # request.data를 통해 data를 집어넣음
        selializer = ReviewSerializer(review, request.data)
		
        # 형식에 부합하면 저장 -> 부합 x 시 400 에러
        if selializer.is_valid(raise_exception=True):
            selializer.save()

            return Response(selializer.data)


    # 삭제
    elif request.method == 'DELETE':
        review.delete()
		
        # 삭제 메세지 출력 여부는 명세서 참조
        data = {
            'msg' : f'delete : review {review_pk} is deleted'
        }
        
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    
# 단일 데이터 작성
@api_view(['POST'])
def create_review(request, movie_pk):
    # FK의 정보 불러옴 -> pk 필요
    movie = get_object_or_404(Movie, pk=movie_pk)
	
    # data=request.data 로 데이터 설정
    selializer = ReviewSerializer(data=request.data)
	
    # 부합 여부 판단
    if selializer.is_valid(raise_exception=True):
        # FK의 정보를 같이 저장 (movie=movie)
        selializer.save(movie=movie)

        return Response(selializer.data, status=status.HTTP_201_CREATED)
```

> 0424 시험 대비 Rest API 정리
