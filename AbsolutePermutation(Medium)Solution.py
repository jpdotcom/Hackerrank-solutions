def absolutePermutation(n, k):
    index_num=None
    index_shift=[0]*(10**5+2)
    list_to_consider=[]
    for i in range(1,n+1):
        list_to_consider.append(i)
    j=0
    while j<=len(list_to_consider)-1:
        first_sol=(list_to_consider[j]-k)
        sec_sol=list_to_consider[j]+k
        x=first_sol>0 and first_sol<len(list_to_consider)+1
        y=sec_sol>0 and sec_sol<len(list_to_consider)+1
        index_num=min(first_sol if x  else 10**5+2 , sec_sol if y else 10**5+2)
        if index_num==10**5+2:
            return -1
        if index_shift[index_num]!=0:
            if index_num==sec_sol and x :
                index_num=first_sol
            elif index_num==first_sol and y:
                index_num=sec_sol
        if index_shift[index_num]!=0:
            return -1
        index_shift[index_num]=list_to_consider[j]
        index_num=None
        j+=1
    for i in range(1,len(index_shift)):
    
        if index_shift[i]!=0:
            list_to_consider[i-1]=index_shift[i]
        
        
    return list_to_consider
    
n=100
k=2
print(absolutePermutation(n,k))