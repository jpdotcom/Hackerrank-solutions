from queue import Queue
def calculate_region(matrix,pos):
    n=len(matrix)
    m=len(matrix[0])
    moves=Queue(maxsize=n*m)
    moves.put(pos)
    indices={pos:None}
    ans=0
    while moves.qsize()!=0:
        idx=moves.get()
        i,j=idx
        ans+=1
        
        
        if i+1<=n-1 and (i+1,j) not in indices and matrix[i+1][j]==1:
            
            moves.put((i+1,j))
            indices[(i+1,j)]=None
            
        if i-1>=0 and (i-1,j) not in indices and matrix[i-1][j]==1:
            moves.put((i-1,j))
            indices[(i-1,j)]=None
        
        
        if j+1<=m-1 and (i,j+1) not in indices and matrix[i][j+1]==1:
            moves.put((i,j+1))
            indices[(i,j+1)]=None

        if j-1>=0 and (i,j-1) not in indices and matrix[i][j-1]==1:
            moves.put((i,j-1))
            indices[(i,j-1)]=None

        if j-1>=0 and i-1>=0 and (i-1,j-1) not in indices and matrix[i-1][j-1]==1:
            moves.put((i-1,j-1))
            indices[(i-1,j-1)]=None
        
        if j+1<=m-1 and i+1<=n-1 and (i+1,j+1) not in indices and matrix[i+1][j+1]==1:
            moves.put((i+1,j+1))
            indices[(i+1,j+1)]=None
        
        if j-1>=0 and i+1<=n-1 and (i+1,j-1) not in indices and matrix[i+1][j-1]==1:
            moves.put((i+1,j-1))
            indices[(i+1,j-1)]=None
        if j+1<=m-1 and i-1>=0 and (i-1,j+1) not in indices and matrix[i-1][j+1]==1:
            moves.put((i-1,j+1))
            indices[(i-1,j+1)]=None
    return ans
   
    
    
   

def connectedCell(matrix):
    res=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                
                
                
                pos=(i,j)
                
                res=max(res,calculate_region(matrix,pos))
                
                
    return res

matrix=[[1,1,0],[1,0,0],[0,0,1]]

print(connectedCell(matrix))
