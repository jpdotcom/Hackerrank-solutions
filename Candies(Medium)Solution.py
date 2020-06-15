def traverse(key,idx,x):
    if idx[key]:
        x+=1
        return traverse(idx[key][0],idx,x)
    return x
def candies(n,arr):
    ans=len(arr)
    indices={}
    for i in range(len(arr)):
        indices[i]=[]
        if i!=0 and arr[i]>arr[i-1] :
            indices[i].append(i-1)
        if i!= len(arr)-1  and not indices[i] and arr[i]>arr[i+1]:
            indices[i].append(i+1)
    print(indices)
    for key in indices:
        x=0
        ans+=traverse(key,indices,x)


        
        
    return ans


n=3
arr= [1,2,3]
print(candies(n,arr))