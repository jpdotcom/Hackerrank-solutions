
class Queue:


    def __init__(self,size):

        self.arr=[None]*size
        self.cap=size

        self.size=0
        self.insert_p=0
        self.pop_p=0
    def qsize(self):
        return self.size

    def insert(self,val):

        p=self.insert_p
        if self.arr[p]!=None:
            print("Error: Too many items in Queue")
            return
        
        self.arr[p]=val
        self.insert_p=(self.insert_p+1)%self.cap
        self.size+=1
        return
    def remove(self):
        p=self.pop_p
        
        if p==self.insert_p:
            print("Error:Removing null from queue")
            return
        
        self.pop_p=(self.pop_p+1)%self.cap
        val=self.arr[p]
        self.arr[p]=None
        self.size-=1
        return val
        
def make_adj(edges):

    adj={}
    for a,b in edges:

        if a not in adj:
            adj[a]=[]
        if b not in adj:
            adj[b]=[]

        adj[a].append(b),adj[b].append(a)
    return BFS(adj,1)

def BFS(adj,start):
    seen=set([start])
    q=Queue(50)
    q.insert(start)
    
    while q.qsize()!=0:
        print(q.qsize())
        v=q.remove()
        
        for u in adj[v]:
            if u not in seen:
                

                q.insert(u)
                seen.add(u)
    return
edges=[[1,2],[1,3],[2,4],[4,3]]
(make_adj(edges))