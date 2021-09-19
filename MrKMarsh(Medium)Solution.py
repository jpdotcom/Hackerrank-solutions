import time
def getUp(grid):
  up=[]
  for i in range(len(grid)):
    temp_list=[]
    for j in range(len(grid[0])):
      temp_list.append(0)
    up.append(temp_list)
  for j in range(len(grid[0])):
    up[0][j]=-1 if grid[0][j]=="x" else 0
  
  for i in range(1,len(up)):
    for j in range(len(up[0])):
      if grid[i][j]==".":
        up[i][j]=up[i-1][j]+1
      else:
        up[i][j]=-1
  return up

def getLeft(grid):
  left=[]
  for i in range(len(grid)):
    temp_list=[]
    for j in range(len(grid[0])):
      temp_list.append(0)
    left.append(temp_list)
  for j in range(len(grid)):
    left[j][0]=-1 if grid[j][0]=="x" else 0
  
  for i in range(len(left)):
    for j in range(1,len(left[0])):
      if grid[i][j]==".":
        left[i][j]=left[i][j-1]+1
      else:
        left[i][j]=-1
  return left

def kMarsh(grid):
  n=0
  up=getUp(grid)
  left=getLeft(grid)
  
  ans=0
  for row1 in range(0,len(grid)):
    for row2 in range(row1+1,len(grid)):
      col1=0
      col2=1
      while col2<len(grid[0]):
        dist_up=row2-row1
        dist_left=col2-col1
        
        a=dist_up<=up[row2][col1]
        b= dist_up<=up[row2][col2]
        c=dist_left<=left[row1][col2] 
        d=dist_left<=left[row2][col2]
        
        if a and b and c and d and col1!=col2 :
          ans=max(ans,2*((row2-row1)+(col2-col1)))
          
          
          
        elif col1!=col2 and  (not c or not d or not a ):
          col1+=1
        col2+=1
        n+=1  
      
  if ans==0:
    print("impossible")
  
  else:
    print(ans,n)
  return

grid=[]
for i in range(100):
  grid.append("."*(500))