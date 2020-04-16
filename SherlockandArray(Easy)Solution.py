def balancedSums(arr):
    i=0
    left_side=0
    right_side=sum(arr)-arr[0]
    while i!=len(arr):
        if i!=0:
            left_side+=arr[i-1]
            right_side-=arr[i]
        if right_side==left_side:
            return "YES"
        i+=1
    return "NO"
arr=[0,0,2,0]
print(balancedSums(arr))

            