def create_freq(expenditure,d):
    freq=[0]*201
    for j in range(d):
        freq[expenditure[j]]+=1
    return freq
def median_even(table,d):
    ans=0
    first=False
    median_val=(d/2,d/2+1)
    median_hit=False
    sumof=0

    for i in range(len(table)):
        sumof+=table[i]
        if sumof>=median_val[0] and not first:
            ans+=i
            first=True
            if sumof>=median_val[1]:
                ans+=i
                return ans/2
        if sumof>=median_val[1]:
            ans+=i
            return ans/2
def median_odd(table,d):
    sumof=0
    median_val=int(d/2)+1
    for i in range(len(table)):
        sumof+=table[i]
        if sumof>=median_val:
            return i


    
def activityNotifications(expenditure, d):
    res=0
    freq_table=create_freq(expenditure,d)
    medians=[]
    i=0
    while i+d<=len(expenditure)-1:
        if d%2==1:
            x=median_odd(freq_table,d)
        else:
            x=median_even(freq_table,d)
        medians.append(x)
        freq_table[expenditure[i]]-=1
        freq_table[expenditure[i+d]]+=1
        i+=1
    i=0
    
    for j in range(d,len(expenditure)):
        if expenditure[j]>=2*medians[i]:
            res+=1
        i+=1
    return res