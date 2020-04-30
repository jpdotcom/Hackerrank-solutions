def swapPositions(arr, pos1, pos2): 
      
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1] 
    return arr

def segment_unsorted(arr):
    indices=[]
    swap_or_reverse=None
    y=0
    e=0
    b=list(arr)
    arr_sort=sorted(arr)
    
    for i in range(len(arr)):
        
        if b[i]!=arr_sort[i]:
            
            if e==1:
                indices.append(i)
                e=0
                
            indices.append(i+1)
        else:
            if len(indices)>1:
                e+=1
            print(i)
            
    

            
    print(indices)

    if len(indices)==2:
        y=1
        swap_or_reverse=(indices[0],indices[1])
        #swap 
    elif (len(indices)-1)==indices[len(indices)-1]-indices[0]:
        y=2
        swap_or_reverse=(indices[0],indices[len(indices)-1])
    else:
        return False
    return swap_or_reverse,y



def almostSorted(arr):
    arr_sorted=sorted(arr)
    if arr==arr_sorted:
        print("yes")
        return
    x=segment_unsorted(arr)


    
    if x==False:
        print("no")
        return 
    if  x[1]==2:
        i=x[0][0]-1
        j=x[0][1]-1
        x=((i+1,j+1),x[1])
        while i<=j:
            arr=swapPositions(arr,i,j)
            i+=1
            j-=1
        if arr==arr_sorted:
            print("yes")
            print("reverse "+ " ".join(str(b) for b in x[0]))
            return
    else:
        arr=swapPositions(arr,x[0][0]-1,x[0][1]-1)
        if arr==arr_sorted:
            print("yes")
            print("swap "+ " ".join(str(b) for b in x[0]))
            return
    print("no")
    return
arr=[1,2,3,4,7,6,5]
almostSorted(arr)
    
             

            
            
