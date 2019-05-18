s=input()
k=""
for i in range(0,len(s)):
	for j in range(i+1,len(s)+1):
		if len(s[i:j])==2:
			k=k+s[i:j]+" "
print(k.strip())
#subset
