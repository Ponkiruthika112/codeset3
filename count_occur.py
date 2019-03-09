n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
k.sort(reverse=True)
c=[]
for i in k:
    c.append(l.count(i))
i=0
s=""
while i<len(c):
    p=c.index(max(c))
    s=s+str(k[p])+" "
    c[p]=0
    i=i+1
print(s.strip())
#count
