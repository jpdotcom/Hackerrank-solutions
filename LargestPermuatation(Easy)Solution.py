def index_to_num(arr):
    index_num=[0]*(10**5+1)
    for i in range(0,len(arr)):
        index_num[arr[i]]=i 
    
    return index_num


def largestPermutation(k,arr):
    index_number=index_to_num(arr)
    val=len(arr)
    i=0
    while k>0 and i<len(arr)-1:
        if arr[i]!=val:
            arr[index_number[val]]=arr[i]
            arr[i]=val
            
            index_number[arr[index_number[val]]]=index_number[val]
            index_number[val]=i
            
            k-=1
        val-=1
        i+=1
    return arr