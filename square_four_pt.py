# your code goes here
import math
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
d1=math.sqrt((abs(x3-x1))**2+(abs(y3-y1))**2)
d2=math.sqrt((abs(x4-x2))**2+(abs(y4-y2))**2)
if d1==d2:
	print("yes")
else:
	print("no")
#four point
