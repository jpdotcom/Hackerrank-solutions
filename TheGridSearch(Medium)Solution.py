def row_scan(i,j,G,P,p_idx_i):
    
    p_idx_j=0
    prev_j=j
    
    while i<len(G) and j<len(G[0]) and p_idx_j< len(P[0]) and p_idx_i<len(P):
        if P[p_idx_i][p_idx_j]==G[i][j]:
            j+=1
            p_idx_j+=1
            
        else:
            return False
    if p_idx_i==len(P):
        return True
    if p_idx_j==len(P[0]):
        return row_scan(i+1,prev_j,G,P,p_idx_i+1)
    return False

def gridSearch(G,P):
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j]==P[0][0]:
                x=row_scan(i,j,G,P,0)
                if x:
                    return "YES"
    return "NO"