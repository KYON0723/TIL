def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n * f(n-1)

print(f(4))