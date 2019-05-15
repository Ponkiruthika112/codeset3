a,b=map(str,input().split())
p=list(set(list(a)))
q=list(set(list(b)))
p.sort()
q.sort()
if p==q:
	print("true")
else:
	print("false")
#same base letters
