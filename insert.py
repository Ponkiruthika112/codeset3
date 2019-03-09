k=input()
s=k[::-1]
y=""
for i in range(0,len(s)-1):
    y=y+s[i]+"-"
y=y+s[-1]
print(y)
#insert sym
