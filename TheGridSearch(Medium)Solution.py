
def gridSearch(G, P):
    pattern_len=len(P[0])-1
    str_len=len(G[0])-1
    i=0
    j=0
    row_check=0
    col_check=0
   
    i_cop=0
    j_cop=1
    where_reset=(i_cop,j_cop)


    while i<=len(G)-1 and j<=str_len:
            

        if G[i][j]==P[row_check][col_check]:
            if col_check==0 and row_check==0:
                if j_cop!=str_len-1:
                    j_cop+=1
                else:
                    j_cop=0
                    i_cop+=1
                where_reset=(i_cop,j_cop)
                

                
            if col_check!=pattern_len and j!=str_len:
                    

                j+=1
                if row_check==0:
                    j_cop+=1
                    where_reset=(i_cop,j_cop)  
            
                col_check+=1
            elif j==str_len and col_check!=pattern_len:
                col_check=0
                row_check=0

            else:
                i+=1

                row_check+=1
                col_check=0

                j-=pattern_len
                   
                    
            if row_check==len(P):
                return "YES"
            
               
        else:
            row_check=0
            col_check=0
                

            i=where_reset[0]
            j=where_reset[1]+1
            if j_cop!=str_len-1:
                j_cop+=1
            else:
                j_cop=0
                i_cop+=1
            where_reset=(i_cop,j_cop)
                
            
               


    return "NO"
                    
                    
    
            
G=['999999', '121211']      
P=["99","11"]
print(gridSearch(G,P))
    