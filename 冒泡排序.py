import random
a=[]
for i in range(100):
    a.append(random.choice(range(100)))
print(a)
n=len(a)
for i in range(n):
    flag=True
    for j in range(0,n-i-1):
        if(a[i]<a[j]):
            a[j],a[i]=a[i],a[j]
            flag=False
    if(flag==True):
        break
print(a)