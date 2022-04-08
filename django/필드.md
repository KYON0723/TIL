```
FileField()
-> 파일 업로드에 사용
-> upload_to / storage 두개의 선택 인자


ImageField()
-> 이미지 업로드에 사용
-> FileField의 서브 클레스 ( 모든 속성, 메서드 사용 가능 )
-> 길이 100자의 문자열로 DB에 생성됨, max_lenth로 최대길이 변경 가능
-> 사용시 Pillow 라이브러리 필요


작성
-> upload_to='images/' : 경로 지정
-> blank=True : 사진을 넣지 않아도 됨 (False -> 무조건 사진 필요)

null=True 금지
-> 문자열 기반 ex ) TextField


null, blank 허용
-> 문자열 기반이 아닌것 ex ) DateField


black -> 빈값 허용 / null -> 빈값 허용이 아님, DB 입력 관련


ImageField 사용전 세팅
-> settings.py 에 MEDIA_ROOT , MEDIA_URL 설정
-> upload_to 로 업로드 된 파일에 사용할 MEDIA_ROOT 설정
	ex) MEDIA_ROOT = BASE_DIR / 'media'

-> MEDIA_URL = '/media/' -> static_url과 다른 경로로 지정해야 함


url.py 설정
-> from django.conf import settings / from django.conf.urls.static import static

-> urlpatterns 마지막에 
+ static(settings.MEDIA_URL, document_root=settings.MEIDA_ROOT) 추가



models 추가
-> image = models.ImageField(upload_to='images/, blank=True')


설치
pip install Pillow

python manage.py makemigrations
python manage.py migrate

pip freeze > requirements.txt


form 에 추가
-> method='POST' 뒤에 enctype='multipart/form-data' 추가


POST로 보낼시 file은 넘어가지 않음
-> 추가로 FILES 인자를 받게 해야함


표시
-> <img src = "{{ article.image.url }}" alt = "{{ article.image }}">


이미지 수정
-> 일부수정 x , 다른 파일로 덮어 쓰는 방식 사용


이미지 크기 조정
pip install Pillow (위에서 이미 함)

pip install django-imagekit

installed_apps 에 'imagekit' 추가

model.py 에
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFil

image = ProcessedImageField(upload_to='images/',
	blank=True,
	upload_to='thumnails/'
	processors=[ResizeToFill(200, 300)],
	format='JPEG',
	options={'quality': 60}) 로 수정 -> 원본 저장 x , 설정한 사이즈로 저장

```



