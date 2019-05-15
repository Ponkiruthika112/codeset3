n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
	s1=0
	s2=0
	for j in range(0,i):
		s1=s1+l[j]
	for k in range(i+1,len(l)):
		s2=s2+l[k]
	if s1==s2:
		c=c+1
		break
if c>=1:
	print("yes")
else:
	print("no")
#prefix sum
