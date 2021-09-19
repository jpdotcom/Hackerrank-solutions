def stones(n, a, b):

    add1=0
    add2=n-1
    total=set()
    while add1!=n:
        total.add(a*add1+b*add2)
        add1+=1
        add2-=1
    total=list(total)
    total.sort()
    return total

n,a,b=3,1,2
print(stones(n,a,b))