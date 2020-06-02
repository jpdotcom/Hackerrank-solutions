import math
def O_counter(grid):
    O_index=set([])
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            
            if grid[i][j]=="O":
                O_index.add((i,j))
                try:
                    grid[i+1][j]
                    O_index.add((i+1,j))
                    
                except IndexError:
                    pass
                try:
                    grid[i-1][j]
                    O_index.add((i-1,j))
                except IndexError:
                    pass
                try:
                    grid[i][j+1]
                    O_index.add((i,j+1))
                except IndexError:
                    pass
                try:
                    grid[i][j-1]
                    O_index.add((i,j-1))
                except IndexError:
                    pass
    return O_index
def bomberMan(n, grid):
    bomb_grid=["O"*len(grid[0])]*len(grid)]
    
    copy_grid=[]



    while n!=0:
        bombs=O_counter(grid) 
        for i in range(len(grid)):
            copy_grid.append([])
            for j in range(len(grid[0])):
                if (i,j) in bombs:
                    copy_grid[i].append(".")
                else:
                    copy_grid[i].append("O")
            copy_grid[i]="".join(copy_grid[i])

        
        grid=copy_grid
        copy_grid=[]
        n-=1
    return grid
grid=["...",".O.","..."]
n=15
print(bomberMan(n,grid))
    
    


        
                    
                
