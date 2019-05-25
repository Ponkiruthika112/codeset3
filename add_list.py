n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(0,len(a)):
    l.append(a[i]+b[i])
print(*l)
#add
