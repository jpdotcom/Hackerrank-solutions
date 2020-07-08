# cook your dish here
import  random
def indices(a):
    
    indices_list={}
    for i in range(len(a)):
        indices_list[a[i]]=i
    return indices_list
def oddSwaps(a,x):
    swaps=[]
    x_idx=a.index(x)
    idx_list=indices(a)
    i=x_idx
    j=x_idx
    
    while (i>=2 or j<=len(a)-3):
        
        if a[i]==i+1 and a[j]==j+1:
            pass
        elif i!=x_idx and j!=x_idx:
           
            return
        if i>=2:
            i-=2
        if j<=len(a)-3:
            j+=2
        
    for i in range(10):
        for key in idx_list:
            if idx_list[key]!=key-1 and (idx_list[key]-idx_list[x])%2==1:
                
                
                idx_list[key],idx_list[x]=idx_list[x],idx_list[key]
                swaps.append([idx_list[key]+1,idx_list[x]+1])
                
    for key in idx_list:
        if idx_list[key]!=key-1:
            print("NO")
            return
    print("YES")
    print(len(swaps))
    for swap in swaps:
        print(swap)
    return
def generate():
    choose=[x for x in range(1,10**5+1)]
    x=[]
    while len(choose)!=0:
        y=random.choice(choose)
        x.append(y)
        choose.remove(y)
    
    return x

a=[2,1,3,4,5]
x=1
(oddSwaps(a,x))