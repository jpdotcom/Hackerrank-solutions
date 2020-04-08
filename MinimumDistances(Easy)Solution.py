def minimumDistances(a):
    i=0
    j=i+1
    min_distance=10**3
    while i<len(a)-1:
        inital_value=a[i]
        if inital_value==a[j]:
            min_distance=min(j-i,min_distance)
            i+=1
            j=i+1
        elif j==len(a)-1:
            i+=1
            j=i+1
        else:
            j+=1
    if min_distance==10**3:
        return -1
    return min_distance


a=["Insert list here"]

print(minimumDistances(a))

    