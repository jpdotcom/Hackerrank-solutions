def isValid(i_up,i_down,j_left,j_right,grid,indices,i,j):
    if (i_up>=-1 and i_down<=len(grid) and j_left>=-1 and j_right<=len(grid[0])) and ((i_up,j) not in indices and (i_down,j) not in indices and (i,j_left) not in indices and (i,j_right) not in indices):
        return True
    return False
def twoPluses(grid):
    ans=[]
    all_G=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="G":
                all_G.append((i,j))
    for i in range(len(all_G)):
        for j in range(i,len(all_G)):
            x=True
            y=True
            plus1=set([all_G[i]])
            plus2=set([all_G[j]])
            
            plus1_starti=all_G[i][0]
            plus1_startj=all_G[i][1]
            plus2_starti=all_G[j][0]
            plus2_startj=all_G[j][1]
            
            plus1_up=all_G[i][0]+1
            plus1_down=all_G[i][0]-1
            plus1_left=all_G[i][1]-1
            plus1_right=all_G[i][1]+1
            
            plus2_up=all_G[j][0]+1
            plus2_down=all_G[j][0]-1
            plus2_left=all_G[j][1]-1
            plus2_right=all_G[j][1]+1
            while x or y:
                if isValid(plus1_up,plus1_down,plus1_left,plus1_right,grid,plus2,plus1_starti,plus1_startj):
                    plus1.add((plus1_up,plus1_startj))
                    plus1.add((plus1_down,plus1_startj))
                    plus1.add((plus1_starti,plus1_left))
                    plus1.add((plus1_starti,plus1_right))
                    plus1_up+=1
                    plus1_down-=1
                    plus1_right+=1
                    plus1_left-=1
                else:
                    x=False
                if isValid(plus2_up,plus2_down,plus2_left,plus2_right,grid,plus1,plus2_starti,plus2_startj):
                    plus2.add((plus2_up,plus2_startj))
                    plus2.add((plus2_down,plus2_startj))
                    plus2.add((plus2_starti,plus2_left))
                    plus2.add((plus2_starti,plus2_right))
                    plus2_up+=1
                    plus2_down-=1
                    plus2_right+=1
                    plus2_left-=1
                else:
                    y=False
            print(plus1,plus2)
            ans.append((2*(plus1_right-plus1_left)-1)*(2*(plus2_right-plus2_left)-1))
    return max(ans)
grid=["GGGGGG","GBBBGB","GBBBGB","GBBBGB","GBBBGB"]
print(twoPluses(grid))


            
            