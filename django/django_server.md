```
# SOP (same origin policy)
- 동일 출처 정책
- 특정 출처(origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는것을 제한

# origin (출처)
- 두 URL의 Protocol, Port, Host가 모두 같아야 동일한 출처

# CORS (교차 출처 자원 공유)
- 추가 HTTP header를 사용, 특정 출처에서 실행중인 웹 어플이 
  다른 출철의 자원에 접근할 권할을 부여하도록 브라우저에 알려주는 체제
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야함
  
# django-cors-headers
- 응답에 CORS header를 추가해주는 라이브러리
- pip install django-cors-headers
- INSTALLED_APPS 및 MIDDLEWARE에 추가해야함

# 인증 / 권한
- 인증 : 유저 확인
- 권한 : 등급 확인(접근 권한)

# JWT
- JSON Web Token 
- JSON 포멧을 활용하여 요소간 정보를 안전하게 교환하기 위한 표준 포멧
- JWT 자체로 검증가능
- 자체적으로 필요한 정보가 모두 있으므로 다른 검증수단 필요 x

# dj-rest-auth / django-allauth 
- pip insatll dj-rest-auth
- pip install django-allauth



```

