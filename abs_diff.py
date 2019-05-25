n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if abs(l[i]-l[j])==k:
            c=c+1
print(c)
#abs_diff
