# your code goes here
z,o=map(int,input().split())
k=["110","101"]
n=z+o
c=0
for i in k:
	p=n*i
	s=p[0:n]
	if s.count("0")==z and s.count("1")==o and s[0]=="1" and s[-1]=="1":
		c=c+1
		l=s
		break
if c==0:
	print(-1)
else:
	print(l)
#g
