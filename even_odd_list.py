n=int(input())
l=list(map(int,input().split()))
s=""
while len(l)!=0:
    k=(len(l)//2)-1
    if len(l)%2!=0:
        print(l[k+1])
        l.pop(k+1)
    else:
        p=l[k]+l[k+1]
        print(p//2)
        l.pop(k)
        l.pop(k)
#even odd
