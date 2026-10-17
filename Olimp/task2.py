a=[1,13,42,84,56,2,34]
if len(a)%2==1:
    b=sorted(a)
    print(b[(len(b)+1)//2-1])