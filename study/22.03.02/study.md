```python
# 서버 킬땐 python manage.py runserver

1. 프로젝트 폴더 내부에 templets 폴더 내에 상속받을 django html 생성
2. settings.py 에 dict 로 상속받게 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

3. 사용

```

