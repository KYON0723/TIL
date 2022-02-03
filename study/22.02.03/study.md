```python
# 반환값
    result = []

    # 중복 값이 없게 set을 만들기
    word_set = set(word)
    
    # 중복 값이 없는 set을 이용, 중복값이 있는 list에서 갯수를 세어 result에 저장
    for i in word_set:
        if word.count(i) > 1:
            result.append(i)
```



```python
# len 대용
    cnt = 0
    for i in word:
        cnt += 1

    # 반환값
    result = ''

    # 짝수는 소문자, 홀수는 대문자로
    for i in range(cnt):
        if not i%2:
            result += word[i].lower()
        else:
            result += word[i].upper()
```



```python
a1 = [61, 34, 95, 25]
print('a1 :', a1)
# a1 : [61, 34, 95, 25]
a2 = a1.sort()

print('a1 :', a1)
# a1 : [25, 34, 61, 95]

print('a2 :', a2)
# a2 : None

b1 = [61, 34, 95, 25]
print('b1 :', b1)
# b1 : [61, 34, 95, 25]
b2 = sorted(b1)

print('b1 :', b1)
# b1 : [61, 34, 95, 25]

print('b2 :', b2)
# b2 : [25, 34, 61, 95]
```

> sort()의 경우, 원본 list를 정렬하는 함수로, 반환값이 존재하지 않는다.
>
> sorted의 경우, 원본 list는 그대로 있고, 정렬된 list를 반환하는 메서드이다.



```python
# 모음군 설정
	vowels = 'aeiou'
    total = 0
    
    # 모음군에 속하는 글자가 있는지 검사
    for vowel in vowels:
        total += word.count(vowel)
```



보기 중 옳지 않은 것을 고르시오.

(1) 함수는 오직 하나의 객체만 반환할 수 있으므로 'return a, b'와 같이 쓸 수 없다.
(2) 함수에서 return 을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 매개변수 (parameter) 는 함수를 선언할 때 설정한 값이며,
	전달 인자 (argument) 는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 함수 선언 시 매개변수 앞에 * 을 붙이고 ,
	이 때는 함수내에서 tuple 로 처리 된다

> (1) 객체는 하나만 반환되지만 값은 여러개 반환해도 된다.
