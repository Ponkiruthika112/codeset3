# your code goes here
a,b=map(str,input().split())
c=0
for i in range(0,len(a)):
	for j in range(i+1,len(a)+1):
		k=a[i:j]
		if b.find(k)!=-1 and len(k)!=1:
			c=c+1
			break
if c!=0:
	print("yes")
else:
	print("no")
 #substr
