import time
def getPrimes(n):


    prime=[True]*(n+1)
    prime[0],prime[1]=False,False

    for p in range(2,len(prime)):

        if prime[p]==True:

            for i in range(p*p,len(prime),p):
                prime[i]=False
    
    return prime
    

def primeXor(a):
    
    mod=10**9+7
    n=8191
    primes=getPrimes(n)
    dp=[]
    for i in range(2):
        dp.append([0]*8192)

   

    freq={}

    for e in a:
        if e not in freq:
            freq[e]=0
        freq[e]+=1
    for i in range(3500,4501):
        if i not in freq:
            freq[i]=0
    
    flag=1
    dp[0][0]=1
    dp[0][3500]=int((freq[3500]+1)/2)
   
    s=time.time()
    for i in range(3501,4501):
        for j in range(8192):
            
            
            a=int((freq[i]+1)/2)
            b=int(((freq[i]+2)/2))
            
            dp[flag][j]=(dp[flag^1][j]*b)%mod+(dp[flag^1][j^i]*a)%mod
            
            
            
        flag=flag^1
        
    
    ans=0        
    for i in range(len(dp[0])):
        if primes[i]:
            
            ans+=dp[flag^1][i]
            
            ans%=mod
    print(time.time()-s)
    return ans

a=[3500]
print(primeXor(a))