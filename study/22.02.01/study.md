```python
BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'query' : title, # 입력 받은 title정보 추가
        'api_key': '8854669b886a6c07c12ea947bcc2311d',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    # id 변수 초기화
    id = 0

    # 검색결과가 빈리스트가 아니면 실행
    if data.get('results') != []:
        for i in data.get('results'):
            if i.get('title') == title:
                id = i.get('id')

    # 검색결과가 없어서 위의 if문을 수행하지 않은경우 None 반환
    if id == 0:
        return None
    

    # if문의 결과로 얻은 id를 사용하여 변수 재지정
    path2 = '/movie/' + f'{id}' + '/credits'
    response = requests.get(BASE_URL+path2, params=params)
    data2 = response.json()

    # 배우 정보를 담을 빈 리스트 생성
    actor = []

    # cast 내의 cast_id가 10 이하인 배우들만 리스트에 추가
    for i in data2.get('cast'):
        if i.get('cast_id') <= 10:
            actor.append(i.get('name'))
    
    # 감독 정보를 담을 빈 리스트 생성
    director = []

    # known_for_department 가 Directing 인 사람만 골라 리스트에 추가
    for i in data2.get('cast'):
        if i.get('known_for_department') == 'Directing':
            director.append(i.get('name'))
    
    # 반환용 dict 생성
    result = {'cast':actor, 'crew':director}

    # result 반환
    return result
```

