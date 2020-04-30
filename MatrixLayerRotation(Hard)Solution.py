def perimeterMatrix(matrix,col_len_start,row_len_start,row_len_end,col_len_end):
    j=0
    perimeter=[]
  
 
    for i in range(row_len_start,row_len_end+1):
        perimeter.append(matrix[col_len_start][i])
    for k in range(col_len_start+1,col_len_end+1):
        perimeter.append(matrix[k][row_len_end])
    j=row_len_end-1
    while j >= row_len_start and col_len_start!=col_len_end:
        perimeter.append(matrix[col_len_end][j])
        j-=1
    j=col_len_end-1
    while j >= col_len_start+1 and row_len_start!=row_len_end:
        perimeter.append(matrix[j][row_len_start])
        j-=1
    return perimeter
def times_to_run(col_len_start,row_len_start,row_len_end,col_len_end,r):
    run=r%(2*(row_len_end-row_len_start+1)+2*(col_len_end-col_len_start+1)+1)
    return run
def rotations(r,matrix_part):
    
    while r!=0:
        b=matrix_part[0]
        matrix_part.pop(0)
        matrix_part.append(b)
        r-=1
    return matrix_part
def matrixRotation(matrix, r):
    copy_matrix=[0]*len(matrix)
    for i in range(len(matrix)):
        copy_matrix[i]=matrix[i]


    all_transformations=[]
    col_str=0
    col_end=len(matrix)-1
    row_str=0
    row_end=len(matrix[0])-1
    while row_end-row_str>=0 and col_end-col_str>=0:
        all_transformations.append(rotations(times_to_run(col_str,row_str,row_end,col_end,r), perimeterMatrix(matrix,col_str,row_str,row_end,col_end)))
        row_str+=1
        col_str+=1
        col_end-=1
        row_end-=1

    col_str=0
    col_end=len(matrix)-1
    row_str=0
    row_end=len(matrix[0])-1

    for transformations in all_transformations:
       
        copy_matrix=matrix_builder(transformations,col_str,row_str,row_end,col_end,copy_matrix)
              
        row_str+=1
        col_str+=1
        col_end-=1
        row_end-=1
 

    return copy_matrix


def matrix_builder(matrix_rotated,col_str,row_str,row_end,col_end,a_matrix):

    
    b=row_str
    x=0

    while b<=row_end:


        a_matrix[col_str][b]=matrix_rotated[x]
  
        x+=1
        b+=1

    b=col_str+1
    while b<=col_end:
        
       
        a_matrix[b][row_end]=matrix_rotated[x]
        x+=1
        b+=1
   
    b=row_end-1
    while b>=row_str and col_str!=col_end:
        
        a_matrix[col_end][b]=matrix_rotated[x]
        x+=1
        b-=1
    
    b=col_end-1
    while b>=col_str+1 and row_str!=row_end:
        a_matrix[b][row_str]=matrix_rotated[x]
        x+=1
        b-=1
    

    return(a_matrix)


def pretty_print(matrix):
    for x in matrix:
        print(" ".join(str(y) for y in x))









        

    


    
        



r=7
matrix=[[1,2,3,4],[7,8,9,10],[13,14,15,16],[19,20,21,22],[25,26,27,28]]

pretty_print(matrixRotation(matrix,r))
