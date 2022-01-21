```
변수명1 = open('파일위치/파일명.json', encoding='UTP8')
변수명2 = json.load(변수명1)

or

변수명3 = '파일위치' + f'{파일명}' + '.json'
변수명4 = open(변수명3, encoding='UTF8')
```

> 위와 같은 방법으로 Json 파일을 불러 올 수 있다.