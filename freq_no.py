n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,len(l)):
   k.append(l.count(l[i]))
print(l[k.index(max(k))])
#frequent numbers
