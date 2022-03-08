# Model 변경사항 저장하기

```python
class Article(models.Model):
    title = model.CharField(max_length=10)
    content = models.TextField()
```

 Model 의 변경사항을 저장하기 위한 명령어

> python manage.py migrate



이로 인해 생성된 마이그레이션 파일에 대응되는 SQL 문을 확인하기 위한 명령어와
출력결과를 작성 (app 의 이름은 articles)

> python manage.py sqlmigrate articles 0001 
>
>```
>BEGIN;
>--
>-- Create model Article
>--
>CREATE TABLE "articles_article"
>("id" integer NOT NULL PRIMATY KEY AUTOINCREMENT,
>"title" varcar(10) NOT NULL, "content" text NOT NULL);
>COMMIT;
>```

