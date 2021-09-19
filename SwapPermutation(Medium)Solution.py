import os
import sys
import time
#
# Complete the swapPermutation function below.
#


def swapPermutation(n,k):
  s=time.time()
  mod=10**9+7
  arr=[i for i in range(1,n+1)]
  
  dp=[]
  prefix=[]
  for i in range(len(arr)+1):
    
    prefix.append([0]*(k+1))
    dp.append([0]*(k+1))
  
  prefix[0][0]=1
  dp[0][0]=1
  
  
  for i in range(len(dp)):
    
    
    for j in range(len(dp[0])):
        
        if j>=i and i>0 and j>0:
          dp[i][j]=(prefix[i-1][j]-prefix[i-1][j-i])
          dp[i][j]%=mod
          
        elif i>0:
          dp[i][j]=prefix[i-1][j]
          dp[i][j]%=mod 
        
        
        
        
        prefix[i][j]=(dp[i][j]+prefix[i][j-1])%mod if j>0 else (dp[i][j])%mod
        prefix[i][j]%=mod
        
        
  
  res1=0

  
  for i in range(0,k+1):
    if((i&1)==(k&1)):
      res1 += dp[-1][i]
      res1%=mod
  #second problem
  
  dp=[]
  
  for i in range(len(arr)+1):
    
    
    dp.append([0]*(k+1))
  
  dp[0][0]=1
  
  for i in range(len(dp)):
    for j in range(len(dp[0])):

      if i>0:
        dp[i][j]+=dp[i-1][j]
        dp[i][j]%=mod
        
        if j>0:

          dp[i][j]+=(i-1)*dp[i-1][j-1]
          dp[i][j]%=mod
    
  res2=0
  
  for i in range(0,k+1):
   
    res2 += dp[-1][i]   
    res2%=mod  
    
  print(time.time()-s)
  return res1,res2

n=2500
k=2500
print(swapPermutation(n,k))
