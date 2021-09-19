import random
import time
from queue import Queue
def create_reach(n):
    ans=[]
    for i in range(n+1):
        temp_list=[]
        for j in range(0,2048):
            temp_list.append(False)
        ans.append(temp_list)
            
    return ans

def process_edge(weight,edge,reached):
    v,u=edge
    
    for i in range(len(reached[v])):
        if reached[v][i]:
            
            reached[u][i|weight]=True
    return


def traverse_graph(A,B,edge_weights,adj,n):
    q=Queue(maxsize=0)
    q.put(A)
    processed=[False]*(n+1)
    reached=create_reach(n)
    reached[A][0]=True
    discovered=[False]*(n+1)
    discovered[A]=True
    while q.qsize()!=0:
        
        v=q.get()
        if v in adj:
            for u in adj[v]:
                
                if not processed[u]:
                    
                    weight=None
                    
                    if (u,v) in edge_weights:
                        
                        weight=edge_weights[(u,v)][-1]
                        edge_weights[(u,v)].pop()
                        
                    else:
                        weight=edge_weights[(v,u)][-1]
                        edge_weights[(v,u)].pop()
                    if not discovered[u]:

                        q.put(u)
                        discovered[u]=True
                process_edge(weight,(v,u),reached)
                

        processed[v]=True
    
    for i in range(len(reached[B])):
        
        if reached[B][i]:
            return i
    
    return -1

def beautifulPath(edges,A,B):
    start=time.time()
    edge_weights={}
    adj={}
    for edge in edges:
        
        a,b,c=edge

        if a not in adj:
            adj[a]=[]

        if b not in adj:
            adj[b]=[]
        if a!=b:
            adj[a].append(b),adj[b].append(a)
        else:
            adj[a].append(b)
        if (a,b) not in edge_weights and (b,a) not in edge_weights:
            edge_weights[(a,b)]=[]
        
        if (b,a) in edge_weights:
            edge_weights[(b,a)].append(c)
        
        else:
            edge_weights[(a,b)].append(c)
    
    ans=traverse_graph(A,B,edge_weights,adj,1000)
    print(time.time()-start)
    return ans

def create_graph():
    graph=[]
    for i in range(10**4):
        v1=random.randint(1,10**3)
        v2=random.randint(1,10**3)
        c=random.randint(1,1025)
        graph.append([v1,v2,c])
    A=random.randint(1,10**3-1)

    return graph,A
   
edges,A=create_graph()
B=2
print(beautifulPath(edges,A,B))


