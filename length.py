n=int(input())
i=0
c=0
if n==0:
    print("1")
else:
    while c<n:
        c=2**i
        i=i+1
    if c==n:
        print(i)
    else:
        print(i-1)
    
    
#length
