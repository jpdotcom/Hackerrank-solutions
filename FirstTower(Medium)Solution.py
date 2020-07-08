def findFirstTower(k,arr):
    x=0
    i=0
    found=False
    while i<k:
        if arr[i]==1:
            found=True
            x=i
        i+=1
    if not found:
        return -1
    return x
def pylons(k, arr):
    curr_tower=findFirstTower(k,arr)
    
    if curr_tower==-1:
        return -1
    ans=1
    while curr_tower+k<len(arr):
        
        indx=curr_tower
        prev_indx=indx
        
        while (indx<prev_indx+2*k) and (indx<len(arr)):
            
            if arr[indx]==1:
              curr_tower=indx
              
            indx+=1
        
        if curr_tower==prev_indx:
            return -1
        
        
        ans+=1
    return ans