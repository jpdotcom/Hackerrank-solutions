def traverse(adj,node,vertices):
    for i in range(len(adj[node])):
        if adj[node][i] not in vertices:
            vertices.add(adj[node][i])
            traverse(adj,adj[node][i],vertices)
    return vertices

def create_list(edges):
    ans={}
    for i in range(len(edges)):
        if edges[i][0] not in ans:
            ans[edges[i][0]]=[]
        if edges[i][1] not in ans:
            ans[edges[i][1]]=[]
        
        ans[edges[i][0]].append(edges[i][1])
        
        ans[edges[i][1]].append(edges[i][0])
    return ans

def roadsAndLibraries(n, c_lib, c_road, cities):
    vertices=set([])
    adj_list=create_list(cities)
    res=0
    if c_lib>c_road:
        for key in adj_list:
            
            if key not in vertices:
                
                prev_len=len(vertices)
                
                vertices.add(key)
                traverse(adj_list,key,vertices)
                
                res+=(len(vertices)-prev_len-1)*c_road+c_lib
        
        single_components=(n-len(vertices))*c_lib
        return res+single_components
   
    return n*c_lib 

cities=[[1,3],[3,4],[2,4],[1,2],[2,3],[5,6]]


print(roadsAndLibraries(6,2,5,cities))