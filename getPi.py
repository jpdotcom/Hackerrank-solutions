import random
import math
def getPi(n):
    circle_points=0
    total_points=0
    for _ in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        
        dist=math.sqrt(x**2+y**2)
        
        if dist<=1:
            circle_points+=1
        
        total_points+=1
    
    res=4*circle_points/total_points
    
    return res

n=1000000
print(getPi(n))