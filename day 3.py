import numpy as np
np.random.seed(0)
a=np.random.rand(40)
print(a)
a=sorted(a)
a=reversed(a)
a=list(a)
print(a[:10:1])

b=[4,7,2,4,8,8,10,4]
del b[3:8]
c=[6,6,8,8,10,4]
b+=c
print(b)

b=sorted(b)
c={}
for i in range(len(b)):
    k=str(b[i])
    if k in c:
        c[k]+=1
    else:
        c[k]=1
print(c)