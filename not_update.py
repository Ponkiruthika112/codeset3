a,b=map(str,input().split())
k=min(a,b)
l=max(a,b)
r=[]
p=[]
for i in range(1,len(k)+1):
	if l.find(k[0:i])==0:
		p.append(k[0:i])
for i in p:
	r.append(len(i))
print(p[r.index(max(r))])
