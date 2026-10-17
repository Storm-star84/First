def dv(a):
    otv=''
    while a >0:
        otv=str(a%2) + otv
        a=a//2
    return otv
for N in range(1,10000):
    D=dv(N)
    if N%2==0:
        F='1'+str(D)+'0'
    else:
        F='11'+str(D) +'11'
    otv=int(F,2)
    if otv>52  and otv<60:
        print(otv)
