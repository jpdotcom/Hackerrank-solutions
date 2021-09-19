import math
import random
import time
def findRectangles(arr):
    arr=list(set(arr))
    prop={} #(dist,m_x,m_y)--> num lines of length dist (no square root since the function is one to one and creates float inaccuracy) with midpoint (x,y)
    ans=0
    
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            x1,y1=arr[i]
            x2,y2=arr[j]
            
            midpoint_x=(x1+x2)/2 
            midpoint_y=(y1+y2)/2 
            dist=(x2-x1)**2+(y2-y1)**2

            line_prop=(dist,midpoint_x,midpoint_y)
            if line_prop not in prop:
                prop[line_prop]=0 
            prop[line_prop]+=1 
            ans+=prop[line_prop]-1
    
    return ans 
s=time.time()
arr=[]
for i in range(10):

    x_i=random.randint(1,5)
    y_i=random.randint(1,5)
    arr.append((x_i,y_i))
print(findRectangles(arr),time.time()-s)  
