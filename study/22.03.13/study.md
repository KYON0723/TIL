# PJT 

```python
from turtle import title
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
```

> model은 필요한 형식에 따라 작성한다.
>
> 데이터를 저장할 틀을 지정한다.



```
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)
```

> admin은 관리자 계정을 지칭한다.
>
> python manage.py createsuperuser 커맨드를 통해 관리자 계정을 생성할 수 있다.
