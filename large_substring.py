a,b=map(str,input().split())
k=min(a,b)
l=max(a,b)
r=[]
p=[]
for i in range(0,len(k)):
   for j in range(i+1,len(k)+1):
      if l.find(k[i:j])!=-1:
         p.append(k[i:j])
for i in p:
	r.append(len(i))
print(p[r.index(max(r))])
#largest substring
