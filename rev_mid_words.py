# your code goes 
# your code goes 
s=input()
k=s.split()
p=""
for i in range(1,len(k)-1):
	p=p+k[i][::-1]+" "
if len(k)==1:
	print(k[0])
elif len(k)==2:
	print(s)
else:
	print(k[0]+" "+p+k[-1])
#reverse
