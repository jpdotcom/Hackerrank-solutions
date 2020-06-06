from queue import Queue 
def traverse_chessboard(pos,end_pos,n):
    
    k=0
    path=[[]]
    q=Queue(maxsize=n**2)
    q.put(pos)
    indices={pos:0}
    while q.qsize()!=0:
        i,j=q.get()
        b=path[k]
        if (i,j)==end_pos:
            
            return path[k],indices[(i,j)]
        x=indices[(i,j)]
        if i-2>=0 and j-1>=0 and (i-2,j-1) not in indices:
            q.put((i-2,j-1))
            c=b+["UL"]
            indices[(i-2,j-1)]=x+1
            path.append(c)
        if i-2>=0 and j+1<=n-1 and (i-2,j+1) not in indices:
            q.put((i-2,j+1))
            c=b+["UR"]
            path.append(c)
            indices[(i-2,j+1)]=x+1
        if j+2<=n-1 and (i,j+2) not in indices:
            q.put((i,j+2))
            c=b+["R"]
            path.append(c)
            indices[(i,j+2)]=x+1
        if i+2<=n-1 and j+1<=n-1 and (i+2,j+1) not in indices:
            q.put((i+2,j+1))
            c=b+["LR"]
            path.append(c)
            indices[(i+2,j+1)]=x+1
        if i+2<=n-1 and j-1>=0 and (i+2,j-1) not in indices:
            q.put((i+2,j-1))
            c=b+["LL"]
            indices[(i+2,j-1)]=x+1
            path.append(c)
        if j-2>=0 and (i,j-2) not in indices:
            q.put((i,j-2))
            c=b+["L"]
            path.append(c)
            indices[(i,j-2)]=x+1
        k+=1
    return [],"Impossible"
def printShortestPath(n, i_start, j_start, i_end, j_end):
    pos=(i_start,j_start)
    end_pos=(i_end,j_end)
    x=(traverse_chessboard(pos,end_pos,n))
    if len(x[0])!=0:
        print(x[1])
        print(x[0])
    else:
        print(x[1])

n=7
i_start=0
j_start=3
i_end=4
j_end=3
printShortestPath(n,i_start,j_start,i_end,j_end)




            
        
        

            
        
    
        
        
        



