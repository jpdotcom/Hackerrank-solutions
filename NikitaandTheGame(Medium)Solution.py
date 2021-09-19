import random
import time
import sys
sys.setrecursionlimit(10000)
arr_global=[0 for x in range(10**5)]

def partitions(i,j,init_sum,depth):
    print(depth)
    left_sum=0
    prev_i=i

    
    ans=0

    while i<=j:
        
        
        if left_sum!=init_sum:
            
            left_sum+=arr_global[i]
            init_sum-=arr_global[i]
            i+=1
        else:    
            
            right_sum=left_sum
            ans+=max(partitions(prev_i,i-1,left_sum,depth+1),partitions(i,j,right_sum,depth+1))
            break
    
    if i>j: #no solution found
        
        return depth
    
    
    return ans
start=time.time()
print(partitions(0,len(arr_global)-1,sum(arr_global),0))

print(time.time()-start)