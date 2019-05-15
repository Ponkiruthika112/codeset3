# your code goes here
a=input()
b=input()
s=a+b
l=list(set(list(s)))
if len(l)==26:
	print("complementary")
else:
	print("non-complementary")
#complementary
