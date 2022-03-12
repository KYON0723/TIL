# PJT 

```python
{% for movie in movies %}
  <a href="{% url 'movies:detail' movie.id %}">{{ movie.title }}</a>
  {{ movie.score }}
  <hr>
{% endfor %}
```

> for 문으로 같은 형식 반복



```
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
```

> movie 라는 인자 넘겨주기
