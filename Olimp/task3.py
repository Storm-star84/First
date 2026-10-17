def fib(n):
    a=[0]*(n+1)
    for i in range(1, n + 1):
        if i <=1:
            a[i]=i
        else:
            a[i]=a[i-1]+a[i-2]
    return(a[n])
print(fib(40))
