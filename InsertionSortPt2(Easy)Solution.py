def insertionSort1(n, arr):
    sorter=arr[n-1]
    i=n-2
    while i>=0 and arr[i]>sorter:
        if arr[i]>sorter:
            arr[i+1]=arr[i]
        i-=1
    arr[i+1]=sorter
    return arr

def insertionSort2(n,arr):
   
    arr_seg=[arr[0]]
    for i in range(1,len(arr)):
        arr_seg.append(arr[i])
        insertionSort1(len(arr_seg),arr_seg)
        for j in range(0,len(arr_seg)):
            arr[j]=arr_seg[j]
        print(" ".join(str(x) for x in arr))
    if len(arr)==1:
        print(" ".join(str(x) for x in arr))


    
arr=[1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5,1,2,4,5]
n=110

insertionSort2(n,arr)

        