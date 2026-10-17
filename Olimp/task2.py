a=[1,13,42,84,56,2,34]
a1=[1,45,14,90]
if len(a)%2==1:
    b=sorted(a)
    print(b[(len(b)+1)//2-1])
if len(a1)%2==0:
    b=sorted(a1)
    print((b[len(b)//2-1]+b[len(b)//2+1-1])/2)