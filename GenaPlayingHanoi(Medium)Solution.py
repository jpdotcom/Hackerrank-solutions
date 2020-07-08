from queue import Queue
def create_new(val,curr,rod,idx):
    res=[]
    for i in range(1,5):
        if i!=val and i not in rod:
            new_pos=list(curr)
            new_pos[idx]=i
            new_pos=tuple(new_pos) 
            res.append(new_pos)
            
    rod.add(val)
    return res
def traverse_moves(a):
    q=Queue(maxsize=0)
    start=[1]*len(a)
    start=tuple(start)
    n=0
    position={start:0}
    q.put(start)
    while (q.qsize()!=0):
        
        curr=q.get()
        n+=1
        
        move=position[curr]+1
        if curr==a:

            print(n*10)
            return position[curr]

        rods=set([])
        
        for i in range(len(curr)):
            
            if len(rods)==4:
                break

            
            if curr[i] not in rods:
                additions=create_new(curr[i],curr,rods,i)
                
                if curr==(2,3,1):
                    print(additions)
                for new_pos in additions:
                    
                    if new_pos not in position:
                        
                        position[new_pos]=move
                        q.put(new_pos)
                
    
a=(3, 1, 1, 4, 4, 1, 2, 1, 1, 3)

print(traverse_moves(a))

    