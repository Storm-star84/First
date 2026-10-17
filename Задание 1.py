R_1=1000
for N in range(20,100):
    v=oct(N)[2:]
    if N%7==0:
        v=v+ v[-2:]
    else:
        v_2 = oct ((N%7) * 7) [2:]
        v=v_2 + v
    R=int(v,8)
    if R>500:
        if R<R_1:
            R_1=R
            print(N,R)

