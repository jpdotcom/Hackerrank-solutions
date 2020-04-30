def index_move(A,i,j,k):
    if k==len(A)-1:
        i=0
        j=1
        k=2
    else:
        i+=1
        j+=1
        k+=1
    return i,j,k


def larrysArray(A):
    n=len(A)**2
    A_sorted=list(A)
    A_sorted.sort()
    i=0
    j=1
    k=2
    while n!=0:
        if A[i]!=i+1:
            A_min=min(A[i],A[j],A[k])
            if A_min==A[i]:
                x=index_move(A,i,j,k)
                i=x[0]
                j=x[1]
                k=x[2]
            if A_min==A[j]:
                prev_i=A[i]
                prev_k=A[k]
                A[i]=A[j]
                A[j]=prev_k
                A[k]=prev_i
                x=index_move(A,i,j,k)
                i=x[0]
                j=x[1]
                k=x[2]
            elif A_min==A[k]:
                prev_i=A[i]
                prev_j=A[j]
                A[i]=A[k]
                A[j]=prev_i
                A[k]=prev_j
                x=index_move(A,i,j,k)
                i=x[0]
                j=x[1]
                k=x[2]
        else:
            x=index_move(A,i,j,k)
            i=x[0]
            j=x[1]
            k=x[2]
        n-=1
        print(A)  
    if A[len(A)-2]>A[len(A)-1]:
        return "NO"
    return "YES"

A=["Insert List Here"]
print(larrysArray(A))          
            
