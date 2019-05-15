# your code goes here
a=input()
b=input()
if a.isdigit()==True and b.isdigit()==True:
	d=list(a)
	r=list(b)
else:
	d=a.split()
	r=b.split()
l=d+r
p=list(set(l))
j=""
q=[]
for i in range(0,len(p)):
	if d.count(p[i])!=r.count(p[i]):
		q.append([l.index(p[i]),p[i]])
q.sort()
for i in range(0,len(q)):
	j=j+str(q[i][1])+" "
print(j.strip())
#missing_ele
