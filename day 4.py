for i in range(1,6):
    print("*"*i)
print("\n")
for i in range(5,0,-1):
    print("*"*i)
print("\n")
l=[7,3,2,6,4,0,1,5]
n=len(l)
for i in range(n-1):
    j=i+1
    if(l[i]>l[j]):
        print(l[j])
    else:
        print(l[i])
