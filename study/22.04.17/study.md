```python
Foreign Key - 외래키 
	다른 테이블에서 참조하는 키
    해당 테이블의 PK를 사용 -> 유일성 만족 해야함(참조 무결성) -> 반드시 PK일 필요는 없음
    하나의 외래키를 여러번 참조 가능
    models.ForeignKey('self', on_delete=models.CASCADE) -> self에 참조할 대상
    1:N 역참조 : article.comment_set -> _set 사용 / related_name='이름' -> 별명 지정
    N:1 참조 : comment.article
           
is_authenticated -> 로그인 여부 확인
AUTH_USER_MODEL -> 기본 양식 USER
AbstractUser -> 사용자 양식 USER
	from django.contrib.auth.models import AbstractUser

	class User(AbstractUser):
        pass
    
    # settings.py
    AUTH_USER_MODEL = 'accounts.User'
    
   # admin.py
	from django,contrib,auth.admin import UserAdmin
   	from .models import User
    
    admin.site.register(User, UserAdmin)
    
User 모델 참조시
	django.contrib.auth.get_user_model() -> 현재 설정한 usermodel 반환
    
fields = ('속성', '속성') -> 표시할 항목만 설정
exclude = ('속성') -> 제외할 항목 설정

article = form.save(commit=False)
article.user = request.user
article.save()
	-> commit을 한번 보류한 뒤 게시글의 user 정보를 입력후 저장
    
if request.user == article.user -> views 에서 본인여부 확인

if user == article.user -> detail 창에서 본인여부 확인

comment = comment_form.save(commit=False)
commnet.article = artice -> 댓글이 달릴 게시글 표시
comment.user = request.user -> 댓글 작성자 표시
comment.save()
    
```

> 0418 시험 대비 DB 정리
