import time

def playWithWords(s):
  dp=[]
  start=time.time()
  for i in range(len(s)):
    temp_list=[]
    for j in range(len(s)):
      temp_list.append(0)
    dp.append(temp_list)

  for i in range(len(dp)-1,-1,-1):
    for j in range(len(dp)):
      if i>j:
        dp[i][j]=-float('inf')
      else:
        if s[i]==s[j]:
          add=2 if i!=j else 1
          dp[i][j]=add
          first=0 if i==len(dp)-1 or j==0 else add+dp[i+1][j-1]
          second=0 if j==0 else dp[i][j-1]
          
          dp[i][j]=max(dp[i][j],first,second)
        else:
           dp[i][j]=max(dp[i][j],dp[i][j-1],dp[i+1][j])
  ans=0
  for i in range(len(dp)):
    A=dp[0][i]
    B2=0 if i==len(s)-1 else dp[i+1][len(s)-1]
    ans=max(ans,A*B2)
    
  return ans,(time.time()-start)

s="r"*3000
print(playWithWords(s))