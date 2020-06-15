from queue import Queue
def isSmaller(k,x,arr):
    visited=0
    q=Queue(maxsize=len(arr))
    q.put(arr[0])
    i=1
    while visited <= k and q.qsize()!=0:
        node=q.get()
        visited+=1
        if visited==k and node==x:
            return "both are equal"
        if node<x:
            try:
                q.put(arr[2*i-1])
            except:
                pass
            try:
                q.put(arr[2*i])
            except:
                pass
        
        i+=1

    if q.qsize()==0:
        return "kth element is greater"
    
    return "x is greater"
k=3
arr=[1,2,3,4,5,6,7]
x=2
print(isSmaller(k,x,arr))