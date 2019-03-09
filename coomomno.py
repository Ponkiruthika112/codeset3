a,b=map(int,input().split())
s=list(map(int,input().split()))
c=[]
d=[]
k=""
for i in range(0,a):
    c.append(s[i])
    c.sort()
for i in range(a,len(s)):
    d.append(s[i])
    d.sort()
for i in range(0,len(c)):
    if d.count(c[i])>=1:
        k=k+str(c[i])+" "
        d.remove(c[i])
print(k.strip())
#common nos
