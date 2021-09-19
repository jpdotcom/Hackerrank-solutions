def winningLotteryTicket(tickets):
    ans=0
    cnt=[0]*(1025)

    for s in tickets:
        m=0
        for c in s:
            m=m|(1<<ord(c)-ord('0')) 
        cnt[m]+=1 
    
    for i in range(len(cnt)):
        for j in range(i,len(cnt)):

            if i|j==1023:
                if i==j:
                    ans+=((cnt[i])*(cnt[i]-1))/2 
                else:
                    ans+=(cnt[i])*(cnt[j])
    return ans

