import math
def getprimes(n):

    end=int(math.sqrt(n))+1
    primes=[True]*(n+1)
    
    for i in range(2,end):
        if primes[i]:
            for j in range(i**2,len(primes),i):
                primes[j]=False 
    primes_num=[]
    for i in range(2,len(primes)):
        if primes[i]:
            primes_num.append(i)
    return primes_num
mod=10**9+7


primes=getprimes(99999)
prime_set=set(primes)
hidden_primes=[]
start=0
str_to_num={}
num_to_str={}      
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):

                s=str(i)+str(j)+str(k)+str(l)
                
                if len(s)==4:
                    
                    p1=sum(list(map(int,s)))
                    p2=sum(list(map(int,s[:3])))
                    p3=sum(list(map(int,s[1:])))
                   
                    
                    if p1 in prime_set and p2 in prime_set and p3 in prime_set:
                        hidden_primes.append(int(s))
                        str_to_num[s]=start 
                        num_to_str[start]=s 
                        
                        start+=1
                        

def isValid(s):
    p1=sum(list(map(int,s)))
                   
                    
    if p1 in prime_set and s[1:] in str_to_num:
        return True 
    return False
dp=[[0 for x in range(len(hidden_primes))] for x in range(4*10**5+1)]

for e in str_to_num:
    dp[4][str_to_num[e]]+=1
for i in range(5,10**5+1):
    for j in range(len(dp[0])):
        
        str_=num_to_str[j]
        
        for k in range(1,10):
            new_str=str_+str(k)
            
            valid=isValid(new_str)
            if valid:

                idx=str_to_num[new_str[1:]]
                
                dp[i][j]=(dp[i][j]%mod+dp[i-1][idx]%mod)%mod
    

print(sum(dp[4]))