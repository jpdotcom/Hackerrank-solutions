def grid_pattern_str(G,P):
    grid_str="" 
    patttern_str=""
    for strings in G:
        grid_str+=strings
    for strings in P:
        patttern_str+=strings
    return grid_str,patttern_str

def gridSearch(G, P):
    count=0
    return_back=1
    i=0
    pattern_scan=grid_pattern_str(G,P)[1]
    grid_str=grid_pattern_str(G,P)[0]

    while i<=len(grid_str):
        if grid_str[i]==pattern_scan[count]:
            count+=1
            print(i,count)
            b=count%(len(P[0]))
            c=len(G[0])-len(P[0])+1
            if count==len(pattern_scan):
                return "YES"
            if b==0 and count!=0 and i+c<=len(grid_str)-1:
                i+=c
            elif b!=0:
                i+=1
            else:
                i=return_back
                return_back+=1
                count=0
        else:
            count=0
            i=return_back
            return_back+=1
           
        
    return "NO"

G=  ["123412", "561212", '123612', '781234']

P= ["123412"]
print(gridSearch(G,P))
        