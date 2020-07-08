from queue import Queue
def traverse_board(weights,adj,start,cities):

    q=Queue(maxsize=(10**5))
    edges={start:0}
    q.put(start)
    ans=0
    node=None
    edge=None
    
    while q.qsize()!=0:
        if node and len(adj[node])==0 and edge:
            print("A")
            ans-=weights[edge]
        node=q.get()
        
        for x in range(len(adj[node])):
            
            if adj[node][x] not in edges: 
                edge=node,adj[node][x]

                if edge not in weights:
                    edge=(edge[1],edge[0])
                    
                add=weights[edge]
                
                edges[adj[node][x]]= add+edges[node]
                
                
                
                ans+=add
            
                q.put(adj[node][x])
        
    return ans,edges




def jeanisRoute(k,roads,cities):
    adj={}
    weights={}
    for i in range(len(roads)):
        a,b,c = roads[i]

        weights[(a,b)]=c

        if a not in adj:
            adj[a]=[]
        
        if b not in adj:
            adj[b]=[]

        adj[a].append(b), adj[b].append(a)
    
    return traverse_board(weights,adj,cities[0],cities)

cities=[1,3,4]
roads=[[1,2,1],[2,3,2],[2,4,2],[3,5,3]]
k=len(cities)
print(jeanisRoute(k,roads,cities))
    
