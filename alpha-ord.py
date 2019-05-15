s=input()
l=s.split()
j=""
for i in l:
	k=list(i)
	k.sort()
	for i in k:
		j=j+i
	j=j+" "	
print(j.strip())
#alphabet order
