def dv(a):
    otv=''
    while a >0:
        otv=str(a%2) + otv
        a=a//2
    return otv
k=0
for N in range(1000000, 1000000000):
    M=dv(N)
    o=N % 4
    O=dv(o)
    M=M+O
    R=int(M,2)
    if R>1100000000 and R<1987653210:
        k+=1
print(k)