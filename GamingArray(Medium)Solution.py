def create_idx(arr):
    indices={}
    
    for i in range(len(arr)):
        
        indices[arr[i]]=i
    return indices
def edit_set(tracked,i,j):
    for k in range(i,j):
        tracked.add(k)
    return tracked
def gamingArray(arr):
    indices=create_idx(arr)
    tracked=set([])
    arr_sorted=sorted(arr,reverse=True)
    i=0
    turns=0
    j=len(arr_sorted)
    while i<=len(arr_sorted)-1:
        
        if indices[arr_sorted[i]] not in tracked:
            
            
            
            turns+=1
            tracked=edit_set(tracked,indices[arr_sorted[i]],j)
            j=indices[arr_sorted[i]]
        i+=1
    print(turns)
    if turns%2==0:
        return "Andy"
    return "Bob"

arr=[5,2,6,3,4]
print(gamingArray(arr))