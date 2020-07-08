def hackerlandRadioTransmitters(x, k):
    x.sort()
    total_distance=0
    new_distance=None
    ans=0
    while i<=len(x)-1:
        while total_distance<=2*k:
            if i == len(x)-1:
                i+=1
                break
            new_distance=x[i+1]-x[i]
            if new_distance>k:
                i+=1
                break
            total_distance+=new_distance
            i+=1
        total_distance=0
        new_distance=None
        ans+=1
    return ans
