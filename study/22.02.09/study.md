```html
offset-(  )-( ) : col 과 col 사이에 특정 상황에 특정크기의 빈칸을 생성하고 싶을 때 사용
```



```
import sys

sys.stdin = open('파일명', 'r')
```

> '파일명' 에 들어간 파일을 호출함



```
N = int(input())
```

> 불러온 값을 숫자 1개로 받는 경우 사용
>
> 연속해서 사용하면 계속하여 다음 줄의 값을 불러온다.



```
N = list(map(int, input().split()))
```

> 불러온 값을 ' '를 기준으로 리스트로 쪼개서 받는 경우 사용
>
> 연속해서 사용하면 위와 마찬가지로 그다음 줄의 값을 불러온다.



```
N, M = map(int, input().split())
```

>  한줄에 적힌 값을 여러개의 변수에 나누어 저장할 때 사용



```
numbers = []
for i in range(N):
    numbers.append(input().split())
```

> 한줄에 적힌값을  ' ' 을 기준으로 나누어 하나의 요소로 갖는 list를 만든다.
>
> N줄만큼 반복한다.
