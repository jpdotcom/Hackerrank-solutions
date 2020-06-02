def swap(parent_node,heap,element_node,total_swaps):
    
    
    if heap[element_node]>heap[parent_node]:
        total_swaps+=1
        prev_node=heap[parent_node]
        heap[parent_node]=heap[element_node]
        heap[element_node]=prev_node
        return swap(int((parent_node-1)/2),heap,parent_node,total_swaps)
    return total_swaps,heap

def create_heap(arr):
    total_swaps=0
    heap=[]
    for i in range(len(arr)):
        heap.append(arr[i])
        operation=swap(int((i-1)/2),heap,i,total_swaps)
        heap=operation[1]
        total_swaps=operation[0]
        
    
        
    return total_swaps
arr=[3,4,2,5,1]
print(create_heap(arr))