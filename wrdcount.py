s=input()
a=0
b=0
k=[]
c=[]
for i in range(0,len(s)):
    if s[i]==" ":
        b=i
        k.append(s[a:b])
        a=i+1
k.append(s[a::])
for i in k:
    c.append(len(i))
l=max(c)
print(k[c.index(l)])

#word count
