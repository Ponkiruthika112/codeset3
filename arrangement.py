# your code goes here
z,o=map(int,input().split())
k=["011","110","101"]
n=z+o
c=0
l=[]
for i in k:
	p=n*i
	s=p[0:n]
	if s.count("0")==z and s.count("1")==o:
		c=c+1
		l.append(s)
		
if c==0:
    print(-1)
else:
    l.sort()
    print(l[0])
#sd
