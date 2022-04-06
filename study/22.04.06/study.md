```python
<h1>CREATE</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    {% endcomment %}

    <input type="submit">
  </form>
```

> 기본 방법



```
<h2>Rendering fileds manually</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>

    <input type="submit">
  </form>
```

> form 에서 표시하고 싶은 속성을 순서대로 표시



```
<h2>Looping over the form's fileds</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% for field in form%}
      {% if field.errors %}
        {% for error in field.errors %}
          <div class='alert alert-danger'> {{ error}} </div>
        {% endfor %}
      {% endif %}

      {{ field.errors }}
      {{ field.label_tag }}
      {{ field }}
    {% endfor%}

    <input type="submit">
  </form>
```

>  error 는 for 반복문으로 표시
