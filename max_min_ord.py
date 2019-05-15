n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
i=0
j=n-1
s=""
while i<j:
	s=s+str(l[i])+" "
	s=s+str(l[j])+" "
	i=i+1
	j=j-1
if i==j:
	s=s+str(l[i])
print(s.strip())
#max_min
