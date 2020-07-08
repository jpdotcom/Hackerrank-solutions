from queue import Queue
def merge_sort(arr,low,middle,high):
    while low<high:
        
        list_1=merge_sort(arr,low,int((low+middle)/2),middle)
        list_2=merge_sort(arr,middle+1,int((middle+high)/2),high)
        
        
        

    q=Queue(maxsize=high-low+1)
    for x in range(low,high+1):
        q.put(arr[x])
    return q

arr=[2,3,4,512]
low=0
high=len(arr)-1
middle=int((low+high)/2)
print(merge_sort(arr,low,middle,high))