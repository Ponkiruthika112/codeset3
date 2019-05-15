# your code goes here
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
j="1:"
y="2:"

q=[]
for i in range(0,len(p)):
	if d.count(p[i])!=r.count(p[i]):
		q.append([l.index(p[i]),p[i]])
q.sort()
for i in range(0,len(q)):
	if d.count(q[i][1])>r.count(q[i][1]):
		j=j+str(q[i][1])+" "
	else:
		y=y+str(q[i][1])+" "
if len(j)==2:
	print(y.strip())
elif len(y)==2:
	print(j.strip())
else:
	print(j.strip())
	print(y.strip())
#code
