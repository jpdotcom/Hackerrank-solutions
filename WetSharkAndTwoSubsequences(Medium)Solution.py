def twoSubsequences(x, r, s):
    num=int((r+s)/2)
    second_sum=int((r-s)/2)
    dp=[]
    mod=10**9+7
    for j in range(105):
        temp2_list=[]
        for k in range(105):
            temp3_list=[]
            for l in range(2005):
              temp3_list.append(0)
            temp2_list.append(temp3_list)
        dp.append(temp2_list)
    dp[0][0][0]=1
    for i in range(1,len(x)+1):
        for j in range(0,i+1):
            for k in range(2005):
                dp[i][j][k]=dp[i-1][j][k]
                if x[i-1]<=k and j>=1:
                    dp[i][j][k]+=dp[i-1][j-1][k-x[i-1]]
                dp[i][j][k]%=mod
    ans=0
    for i in range(1,len(x)+1):
        ans+=dp[len(x)][i][num]*dp[len(x)][i][second_sum]
        ans%=mod
    return ans