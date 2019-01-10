#this is my code
def merge(a,b):
	k=[]
	while len(a)!=0 and len(b)!=0:
		if a[0]<b[0]:
			k.append(a[0])
			a.remove(a[0])
		else:
			k.append(b[0])
			b.remove(b[0])
	if len(a)==0:
		k=k+b
	else:
		k=k+a
	return k
	
def mergesort(x):
	if len(x)==0 or len(x)==1:
		return x
	else:
		mid=len(x)//2
		a=mergesort(x[:mid])
		b=mergesort(x[mid:])
	return merge(a,b)
n=int(input())
x=list(map(int,input().split()))
k=""
g=mergesort(x)
for i in range(0,n):
	k=k+str(g[i])+" "
print(k.rstrip())
