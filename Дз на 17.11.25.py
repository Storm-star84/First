# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x<=y) and z and (not(w))):
#                     print(x,y,z,w,'1')
# for N in range(1,1000):
#     F=bin(N)[2:]
#     k=0
#     for i in F:
#         k+=int(i)
#     if k%2==0:
#         F=F+'0'
#         F='10'+F[2:]
#     else:
#         F = F + '1'
#         F = '11' + F[2:]
#     R=int(F,2)
#     if R>480:
#         print(N)
#         break
from itertools import product
alf="АГЕМНРТУ"
x=product(alf,repeat=4)
k=0
for i in x:
    S=''.join(i)
    k+=1
    F=''.join(sorted(S))
    if (S[0]!=S[1] and S[0]!=S[2] and  S[0]!=S[3] and S[1]!=S[2] and S[1]!=S[3] and S[2]!=S[3] and S==F):
        print(k)