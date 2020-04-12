def fairRations(B):
    breads=0
    i=0
    j=len(B)-1
    while i<j:
        if B[i]%2==0:
            i+=1
        else:
            B[i]+=1
            B[i+1]+=1
            i+=1
            breads+=2
    if B[i]%2==0: 
        return breads
    return "NO"

B=[2,3,4,5,6]
print(fairRations(B))
        
