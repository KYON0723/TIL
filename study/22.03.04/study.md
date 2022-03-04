```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

> setting 에서 static 지정시 사용



```
{% load static %}
```

> static 지정한 위치에서 불러올때 맨 위에 첨부



```
{% extends '받을 곳' %}
```

> 확장 받을 위치에서 확장 받음







