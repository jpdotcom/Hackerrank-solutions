import math
x=[0]
n=101
i=0
while n!=0:
    
    x.append((4*x[i]+5))
    i+=1
    n-=1
    
print(x[len(x)-1])