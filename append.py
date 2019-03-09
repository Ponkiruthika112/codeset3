s,k=map(str,input().split())
if len(s)>len(k):
    p=s
    r=k
else:
    p=k
    r=s
print(p[0:len(r)]+r)
#append
