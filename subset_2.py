s,l=map(str,input().split())
k=""
for i in range(0,len(s)):
	for j in range(i+1,len(s)+1):
		if len(s[i:j])==int(l):
			k=k+s[i:j]+" "
print(k.strip())
#subset
