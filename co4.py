#this is my code
n=int(input())
s=" "
k=" "
l=list(map(int,input().split()))
l.sort()
for i in range(0,len(l)):
	s=s+str(l[i])+k
print(s.strip())
