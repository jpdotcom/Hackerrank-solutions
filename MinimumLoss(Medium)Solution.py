import random
import heapq
def generate_list():
    res=[]
    for i in range(10**5):
        num=random.randint(1,10**16)
        res.append(num)
    return res
def create_idx(price):
    indices={}
    for i in range(len(price)):
        indices[price[i]]=i
    return indices


def minimumLoss():
    n=0
    price=generate_list()
    ans=10**16
    indices=create_idx(price)
    for x in range(len(price)):
        price[x]=-1*price[x]
    
    heapq.heapify(price)
    reinsert=[]
    while len(price)!=1:

        n+=1
        current_price=-1*heapq.heappop(price)
        next_best_price=-1*price[0]
        
        
        
        if indices[current_price]<indices[next_best_price]:
            ans=min(ans,current_price-next_best_price)
            if reinsert:
                num=reinsert.pop(len(reinsert)-1)
                heapq.heappush(price,num)
        else:
            
            reinsert.append(-1*current_price)
    print(len(reinsert))
    return ans,n

print(minimumLoss())
