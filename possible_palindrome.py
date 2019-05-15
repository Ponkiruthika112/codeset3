s=input()
l=[]
for i in range(0,len(s)):
	for j in range(i+2,len(s)+1):
		k=s[i:j]
		if k==k[::-1]:
			l.append(k)
l.sort()
for i in range(0,len(l)):
	print(l[i])
#possible palindrome
