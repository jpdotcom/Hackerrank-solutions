def getMinimumCost(k, c):
    c.sort(reverse=True)
    freq,ans,k_indx=[0]*k,0,0
    
    for i in range(len(c)):
        ans+=c[i]*(freq[k_indx]+1)
        freq[k_indx]+=1
        k_indx=(k_indx+1)%k
    return ans