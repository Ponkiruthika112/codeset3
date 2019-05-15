s=input()
l=[]
for i in range(0,len(s)):
	for j in range(i+1,len(s)+1):
		k=s[i:j]
		if k==k[::-1]:
			l.append(k)
g=[]
for i in range(0,len(l)):
	g.append(len(l[i]))
print(l[g.index(max(g))])
#palindrome
