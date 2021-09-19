import time
import random
def GridlandMetro():
    s=time.time()
    def getrandom():
        res=[]
        n=random.randint(1,10**9)
        m=random.randint(1,10**9)
        for i in range(1000):
            a=random.randint(1,n+1)
            b=random.randint(1,m+1)
            c=random.randint(b,m+1)
            res.append([a,b,c])
        return n,m,res,len(res)
    
    n,m,track,k=getrandom()

    rows={}
    space_taken=0
    for i in range(k):
        a,b,c=track[i]
        if a not in rows:
            rows[a]=[]
        
        rows[a].append((b,c))
    
    
    for key in rows:

        rows[key].sort(key=lambda x:x[1])
        
        combined=[rows[key][0]]
        for i in range(1,len(rows[key])):

            a=combined[-1]
            b=rows[key][i]
            
            if b[0]<=a[1]:
                combined.pop()
                if b[0]>a[0]:

                    combined.append((a[0],b[1]))
                
                else:
                    combined.append(b)
            else:
                combined.append(b)
        
        for e in combined:

            space_taken+=e[1]-e[0]+1
    print(time.time()-s)
    return n*m-space_taken


  
print(GridlandMetro())     


            






