import random
import sys
n=0
sys.setrecursionlimit(10000)
weights={}
adj={}
path=[]
seen=set([])
def generate_random():
    res=[]
    for i in range(1000):
        for j in range(10):
            edge=[i,j,random.randint(1,1000)]
            res.append(edge)
    return res
penalty_paths=[float('inf')]
def ORsum(path):
    global n
    n+=1
    print(n)
    res=path[0]
    for i in range(1,len(path)):
        res=(res|path[i])
    return res

def traverse_graph(node,start,end):
    global n
    
    global seen
    global path
    global penalty_paths
    if node not in adj:
        return
    
    if node==end:
        
        penalty_paths.append(ORsum(path))
        path.pop()
        
        return 
    if node not in seen:
        seen.add(node)
        for i in range(len(adj[node])):
            
            if adj[node][i] not in seen:
                
                next_node=adj[node][i]
                edge=(node,next_node) if (node,next_node) in weights else (next_node,node)

                for j in range(len(weights[edge])):
                    
                    path.append(weights[edge][j])
                    traverse_graph(next_node,start,end)
    
    seen.remove(node)
    if len(path)!=0:
        path.pop()
    return

def beautifulPath(edges,A,B):
    global seen
    global adj
    global weights
    seen=set([])
    start=A
    end=B
    path=[]
    node=A
    for i in range(len(edges)):
        
        a,b,c=edges[i]

        if (a,b) not in seen and (b,a) not in seen:
            seen.add((a,b))
            weights[(a,b)]=[]
            if a not in adj:
                adj[a]=[]

            if b not in adj:
                adj[b]=[]

            adj[a].append(b),adj[b].append(a)
        
        if (a,b) in seen:
            weights[(a,b)].append(c)

        else:
            weights[(b,a)].append(c)
    seen=set([])
    print(len(adj),len(weights))
    traverse_graph(node,start,end)
    ans=min(penalty_paths) if min(penalty_paths)!=float("inf") else -1
    
    return ans

edges=generate_random()
A=1
B=2
                
print(beautifulPath(edges,A,B))
