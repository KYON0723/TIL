```python
# 0. import
import requests
from pprint import pprint

# 1. URL 및 요청변수 설정

# https://developers.themoviedb.org/3/movies/get-now-playing

# https://api.themoviedb.org/3/movie/now_playing?api_key=8854669b886a6c07c12ea947bcc2311d&region=KR&language=ko

# 기본 변수 지정
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'region': 'KR',
    'language': 'ko'
}

# 2. 요청 보낸 결과 저장
response = requests.get(BASE_URL+path, params=params)
print(response.status_code, response.url)
data = response.json()

# print(type(data)) # dict -> dict 값으로 저장되어 있음
# print(data.keys()) # dict_keys(['dates', 'page', 'results', 'total_pages', 'total_results']) -> dict 내부에 저장된 키값
# print(type(data.get('results'))) # list -> resutls(영화목록)은 list 형태로 저장되어 있음
# pprint(data.get('results')[0]) # list의 첫번째 구조
# print(type(data.get('results')[0])) # dict -> dict 형식으로 저장되어있음
# print(len(data.get('results'))) # 20개 -> len 함수로 총 갯수를 셈
```

