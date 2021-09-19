
def abbreviation(a, b):
    dp=[]
    
    for i in range(len(b)+1):
        temp_list=[]
        for j in range(len(a)+1):
            
                
            
            temp_list.append(False)
        
        dp.append(temp_list)

    dp[0][0]=True
    for i in range(0,len(dp)):
        
        
        
        for j in range(0,len(dp[0])):
            
            if dp[i][j]:
                if j<len(a):
                    if a[j].islower():
                    
                        dp[i][j+1]=True
                    if i<len(b):
                        if b[i]==a[j].upper():
                    
                            dp[i+1][j+1]=True

    for i in range(len(dp)):
        print(dp[i])
    if dp[-1][-1]:
        return "YES"
    return "NO"

a="daBcd"                
b="ABC"
print(abbreviation(a,b))