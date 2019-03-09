s,k=map(str,input().split())
if len(s)>len(k):
    p=s
    r=k
    print(p[0:len(r)]+r)
else:
    p=k
    r=s
    print(r[0:len(p)]+p)
#append
