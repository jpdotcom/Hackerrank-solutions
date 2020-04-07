def insertionSort1(n, arr):
    sorter=arr[n-1]
    i=n-2
    while i>=0 and arr[i]>sorter:
        if arr[i]>sorter:
            arr[i+1]=arr[i]
        print(arr)
        i-=1
    arr[i+1]=sorter
    print(arr)
    return 
 

n=1
arr=[2]
insertionSort1(n,arr)
    
       