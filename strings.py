n=int(input())
l=list(map(str,input().split()))
s=input()
j=len(s)
c=0
for i in l:
    if s==i[0:j]:
        c=c+1
print(c)
    
#xcvbn
