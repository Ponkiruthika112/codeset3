n=int(input())
l=list(map(int,input().split()))
k=[]
p=""
for i in range(0,len(l)):
	k.append(l[i])
	p=p+str(min(k))+" "
print(p.strip())
#small
