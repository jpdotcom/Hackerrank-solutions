import random
import sys
def getRandom():
    a=[]
    for i in range(10**5):
        a.append(random.randint(1,10**18))
    return a
sys.setrecursionlimit(10000)
def findValidCity(start,fuel,gas,n,cap):
    curr=0
    s=0
    
    for i in range(2*n):
        curr=min(fuel[i%n]+curr,cap)-gas[i%n]

        if curr<0:
            curr=0
            s=i+1
            if s==n:
                return -1
    return s
def travelAroundTheWorld(fuel,cost,cap):
    
    s=findValidCity(0,fuel,cost,len(fuel),cap)
    print(s)
    if s==-1:
        return 0
    ans=1
    need=[0]

    i=(s-1)%len(fuel) 
    while True:
        print(need)
        if len(need)==len(fuel):
            return ans
        
        val=max(0,need[-1]+cost[i]-min(fuel[i],cap))
        if val==0:
            ans+=1
        need.append(val)

        i=(i-1)%len(fuel)
    return ans


start=0
fuel=[3,1,3]
gas=[2,2,2]
n=len(fuel)
cap=3
print(travelAroundTheWorld(fuel,gas,cap))