```pytyon
a = [
    [1, 2, 3, 4],
    [4, 5, 6, 4],
    [7, 8, 9, 5],
]
print(len(a))
for i in range(len(a[0])):
    print('i :', i)
    print('a[0] : ', a[0])
    
    for j in range(len(a)):
        print('j :', j)
        print('a[j][i] : ', a[j][i])
    print('------')
```

> 열 정보 추출



```python
def lonely(li):
    # len 대체
    cnt = 0
    for i in li:
        cnt += 1

    # 옆의 요소 비교 하여 값이 같으면 ''로 변환
    # 마지막 요소는 다음 값이 없으니 cnt-1까지만 진행
    for i in range(cnt-1):
        if li[i] == li[i+1]:
            li[i] = ''

    # '' 로 치환한 값 모두 제거
    while '' in li:
        li.remove('')

    return li
```

> 같은값이 인접해 있으면 모두 제거하기