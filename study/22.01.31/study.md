```python
# 기본 변수 지정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '8854669b886a6c07c12ea947bcc2311d',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    # 보기 편하게 data.get('results')[영화 목록] 를 li로 지정
    li = data.get('results')
    n = len(li)

    # li 내부의 영화들에서 각각 vote_average 정보를 추출, 높은 순으로 버블정렬
    for i in range(n):
        for j in range(0, n - i -1 ):
            if li[j].get('vote_average') < li[j + 1].get('vote_average'):
                li[j], li[j + 1] = li[j + 1], li[j]

    # 정렬된 li에서 앞에서부터 순서대로 5개(1~5위) 까지 잘라 result 생성 
    result = li[:5]

    # result 반환    
    return result
```

