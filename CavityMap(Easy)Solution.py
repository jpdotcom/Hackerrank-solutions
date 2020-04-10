def cavityMap(grid):
    cavitys=[]

    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            
            middle=int(grid[i][j])
            top=int(grid[i-1][j])
            bottom=int(grid[i+1][j])
            left=int(grid[i][j-1])
            right=int(grid[i][j+1])
            if middle>top and middle>bottom and middle>left and middle>right:
                b=(i,j)
                cavitys.append(b)
    for tuples in cavitys:
        a,b=tuples
        grid[a]=list(grid[a])
        grid[a][b]="X"
        
        grid[a]="".join(grid[a])
    return grid
    
    
    
        
        
    

grid=["1122","1912","1892","1234"]
print(cavityMap(grid))





            