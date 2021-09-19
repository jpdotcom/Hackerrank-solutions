def fairCut(arr,k):
    
    n=len(arr)
    p_sums=[[(0,0) for i in range(k+1)] for j in range(n+1)]
    dp=[[float('inf') for i in range(k+1)] for j in range(n+1)]


    dp[0][0]=0
    
    arr=sorted(arr)
    for i in range(len(dp)):
        for j in range(len(dp[0])):

            
            if i>0: 
                
                a,b=p_sums[i-1][j][0],p_sums[i-1][j][1] 

                if j*arr[i-1]-a+dp[i-1][j]<dp[i][j]:
                    
                    dp[i][j]=j*arr[i-1]-a+dp[i-1][j]
                    p_sums[i][j]=(a,b+arr[i-1])
                
                if j>0 and i>=j:

                    a,b=p_sums[i-1][j-1][0],p_sums[i-1][j-1][1]

                    if (i-j)*arr[i-1]-b+dp[i-1][j-1]<dp[i][j]:
                        
                        dp[i][j]= (i-j)*arr[i-1]-b+dp[i-1][j-1]

                        p_sums[i][j]=(a+arr[i-1],b)
    
    return dp[n][k]
    
    


arr=[1,2,100,400,1000]



k=3
print(fairCut(arr,k))