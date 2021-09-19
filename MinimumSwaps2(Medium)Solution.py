def minimumSwaps(arr):

    n=len(arr)
    indices_left=[False]*(n)
    ans=0
    for i in range(len(indices_left)):
        
        if not indices_left[i]:
            start=i
            
            cycle=0
            j=i
            while arr[j]-1!=start:
                
                j=arr[j]-1
                indices_left[j]=True
                cycle+=1
            
            indices_left[start]=True
            ans+=cycle
    return ans

arr=  [4, 3, 1 ,2]  
print(minimumSwaps(arr))