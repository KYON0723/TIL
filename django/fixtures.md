```
fixtures - 공유용 데이터 베이스

git에 DB를 올리지 않으므로 공동작업시 DB를 매번 새로 만들 필요가 있음
-> fixtures를 사용하여 해결

dumpdata - 데이터 추출
-> python manage.py dumpdata --indent 4 articles.article > articles.json
-> 추출 후 (app이름)/fixtures/ 경로를 만들어 넣어줌

데이터 사용
-> python manage.py loaddata articles/articles.json
```



