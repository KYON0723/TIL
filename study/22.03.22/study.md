```python
# 기존 재귀 방식
def fibo(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)


# 동적 방식
def fibo2(n):
    val = [0, 1]

    if n < 2:
        return val[n]

    else:
        for i in range(2, n+1):
            val.append(val[i-1] + val[i-2])

        return val[n]

```

> 피보나치
