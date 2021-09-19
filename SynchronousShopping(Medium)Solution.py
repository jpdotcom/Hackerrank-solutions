

import math
import os
import random
import re
import sys
import heapq
import time
#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

def traverse(adj,table,bitOR):
    q=[(0,(1,bitOR[1]))]
    heapq.heapify(q)
    
    table[1][bitOR[1]]=0
    
    while len(q)!=0:
        x=heapq.heappop(q)
        
        time,v,OR=x[0],x[1][0],x[1][1]
        
        for u,travel_time in adj[v]:

            if time+travel_time<table[u][OR|bitOR[u]]:
                
                table[u][OR|bitOR[u]]=time+travel_time
                
                heapq.heappush(q,(time+travel_time,(u,OR|bitOR[u])))
        

    return 


def shop(n, k, centers, roads):
    
    found=0
    for j in range(1,k+1):
        found+=2**j
    
    bitOR=[0]*(n+1)
    adj={}
    table=[]
    
    for i in range(n+1):
        table.append([float('inf')]*2050)
    
    for i in range(len(centers)):
        
        nums=centers[i].split(' ')
        run=int(nums[0])
        
        for j in range(1,run+1):
            
            bitOR[i+1]=bitOR[i+1]|(2**int(nums[j]))
    
    for i in range(len(roads)):

        a,b,weight=roads[i]


        if a not in adj:
            adj[a]=[]
        if b not in adj:
            adj[b]=[]
        
        adj[a].append((b,weight)),adj[b].append((a,weight))
    
    
    traverse(adj,table,bitOR)
    ans=float('inf')
    start=time.time()
    for i in range(len(table[n])):
        for j in range(i,len(table[n])):
            
            
                
            if i|j==found:
                    
                ans=min(ans,max(table[n][i],table[n][j]))

    print(time.time()-start)
    return ans