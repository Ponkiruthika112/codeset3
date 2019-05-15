n=int(input())
k=3
s=0
while k<n:
   for i in range(2,k):
      if k%i==0:
         break
   if i==k-1:
      s=s+k
   k=k+10
print(s)
#prime
