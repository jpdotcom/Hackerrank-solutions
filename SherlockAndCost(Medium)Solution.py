def cost(B):
    dp=[[0]*len(B),[0]*len(B)] #the first list indicates that the ith position is 1 and second for B[i]
    for i in range(1,len(B)):

        dp[0][i]=max(dp[0][i-1],dp[1][i-1]+abs(B[i-1]-1))
        dp[1][i]=max(dp[1][i-1]+abs(B[i]-B[i-1]),dp[0][i-1]+abs(B[i]-1))
    return max(dp[1][len(B)-1],dp[0][len(B)-1])