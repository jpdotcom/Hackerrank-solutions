from queue import Queue
def traverse_chessboard(n,i_move,j_move):
    indices={(0,0):0}
    all_moves=Queue(maxsize=n**2)
    all_moves.put((0,0))

    while all_moves.qsize()!=0:
        i,j=all_moves.get()
        
        x=indices[(i,j)]
        if (i+i_move)<=n-1 and (j+j_move)<=n-1 and (i+i_move,j+j_move) not in indices:
            all_moves.put((i+i_move,j+j_move))
            indices[(i+i_move,j+j_move)]=1+x
        
        if i-i_move>=0 and (j+j_move)<=n-1 and (i-i_move,j+j_move) not in indices:
            indices[(i-i_move,j+j_move)]=1+x
            all_moves.put((i-i_move,j+j_move))

        if (i+i_move)<=n-1 and (j-j_move)>=0 and (i+i_move,j-j_move) not in indices:
            indices[(i+i_move,j-j_move)]=1+x
            all_moves.put((i+i_move,j-j_move))

        if (i-i_move)>=0 and (j-j_move)>=0 and (i-i_move,j-j_move) not in indices:
            indices[(i-i_move,j-j_move)]=1+x
            all_moves.put((i-i_move,j-j_move))

        if i+j_move<=n-1 and j+i_move<=n-1 and (i+j_move,j+i_move) not in indices:
            indices[(i+j_move,j+i_move)]=1+x
            all_moves.put((i+j_move,j+i_move))

        if i-j_move>=0 and j+i_move<=n-1 and (i-j_move,j+i_move) not in indices:
            indices[(i-j_move,j+i_move)]=1+x
            all_moves.put((i-j_move,j+i_move))


        if i+j_move<=n-1 and j-i_move>=0 and (i+j_move,j-i_move) not in indices:
            indices[(i+j_move,j-i_move)]=1+x
            all_moves.put((i+j_move,j-i_move))

        if i-j_move>=0 and j-i_move>=0 and (i-j_move,j-i_move) not in indices:
            indices[(i-j_move,j-i_move)]=1+x
        
            all_moves.put((i-j_move,j-i_move))
    if (n-1,n-1) in indices:
        return indices[(n-1,n-1)]
    return -1
def knightlOnAChessboard(n):
    res=[]
    for i in range(1,n):
        temp_list=[]
        for j in range(1,n):
            
            temp_ans=traverse_chessboard(n,i,j)
            temp_list.append(temp_ans)
        res.append(temp_list)
    return res
n=25
print(knightlOnAChessboard(n))