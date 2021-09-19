path=[]
def DFS(adj,u,pivot,curr_path,visited,end,pivot_found):
    global path
    curr_path.append(u)
    
    visited.add(u)
    if u==end and pivot_found:
        path=curr_path.copy()
        return curr_path 
    
    for v in adj[u]:
        if v not in visited:
            if v==pivot:
            
                curr_path=DFS(adj,v,pivot,curr_path,set(),end,True)
            else:
                curr_path=DFS(adj,v,pivot,curr_path,visited,end,pivot_found)
    curr_path.pop()
    return curr_path


def create(edges,pivot,start,end):
    global path

    adj={}
    for i in range(len(edges)):
        a,b=edges[i]
        if a not in adj:
            adj[a]=[]
        if b not in adj:
            adj[b]=[]
        adj[a].append(b),adj[b].append(a)
    print(adj)
    curr_path=[]
    (DFS(adj,start,pivot,curr_path,set(),end,False))
    if len(path)==0:
        path=[pivot]
    print(path)
    return  




edges=[[1,2],[1,3],[2,4],[2,5],[3,6],[3,7]]
start=4
end=5
pivot=3
print(create(edges,pivot,start,end))
