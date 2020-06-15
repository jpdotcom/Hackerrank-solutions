
def maxSubarray(arr):
    max_subsequence=0
    found=False
    for i in range(len(arr)):
        if arr[i]>0:
            found=True
            max_subsequence+=arr[i]
    if not found:
        max_subsequence=max(arr)
    max_subarry=0
    i=len(arr)-2
    while i!=-1:
        if arr[i+1]>0:
            arr[i]+=arr[i+1]
        i-=1
    max_subarry=max(arr)
    print(max_subarry)
    print(max_subsequence)
    

arr=[-2,-3,-1,-4,-6]
(maxSubarray(arr))
    
